from __future__ import print_function
import string , pywifi , sys , ctypes , time , datetime , psutil , platform , wmi
from pywifi import const
from bluetooth import *
from bluetooth.windows import discover_devices
#pip install comtypes wmi psutil pywifi pybluez2 pypiwin32
# from winrt.windows.devices import radios

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def get_admin():
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None , "runas" , sys.executable , __file__ , None , 1)

class wifi():
    def __init__(self) -> None:
        global w,wireless,wifi_status,constlist
        constlist = ['DISCONNECTED' , 'SCANNING' , 'INACTIVE' , 'CONNECTING' , 'CONNECTED']
        self.__update()
    
    def __update(self):
        global w,wireless,wifi_status
        w = pywifi.PyWiFi()
        wireless = w.interfaces()[0]
        wifi_status = wireless.status()
        self.status = constlist[wifi_status]

    def connect(self , ssid , password):
        self.__update()
        if self.status == 'DISCONNECTED':
            wifi_file = pywifi.Profile()
            wifi_file.ssid = ssid
            wifi_file.auth = const.AUTH_ALG_OPEN
            wifi_file.akm.append(const.AKM_TYPE_WPA2PSK)
            wifi_file.cipher = const.CIPHER_TYPE_CCMP
            wifi_file.key = password
            wireless.remove_all_network_profiles()
            tep_profile = wireless.add_network_profile(wifi_file)
            wireless.connect(tep_profile)
            time.sleep(3)
            if wireless.status() == const.IFACE_CONNECTED:
                self.__update()
                return True
            else:
                self.__update()
                return False
        else:
            print("Already WiFi Access")
        self.__update()

    def disconnect(self):
        if self.status == 'CONNECTED':
            w = pywifi.PyWiFi()
            wireless = w.interfaces()[0]
            wireless.disconnect()
            time.sleep(2)
            self.__update()

    def scan(self):
        wireless.scan()
        time.sleep(2)
        results = wireless.scan_results()
        wifi_results = []
        for profiles in results:
            d = {'ssid': profiles.ssid, 'key': profiles.key}
            if d['ssid'] != '':
                wifi_results.append(d)
        wifi_results = [dict(t) for t in {tuple(d.items()) for d in wifi_results}]
        return wifi_results
    
class bluetooth():
    def __init__(self) -> None:
        global scanned,scanlist
        scanned = []
        scanlist = {}
        self.devices_nearby = {}
        self.found = False
        self.connected = False

    def scan(self):
        global already,results,loop_time
        loop_time = 0
        try:
            while (loop_time := loop_time + 1) and (a := discover_devices(lookup_names = True , duration = 5)) and (loop_time <= 3):
                if a.__len__ > 0:
                    break
            time.sleep(2)
        except Exception:
            return None
        already = []
        results = []
        for (addr , name) in a:
            if name not in already:
                if name == '':
                    name = 'Hidden'
                results.append({'Device:' : name , 'Mac:' : addr})
                already.append(name)
                self.devices_nearby[name] = addr
        if not results:
            results = None
            self.devices_nearby = None
        return results

    def get_mac(self , name):
        self.scan()
        try:
            addr = self.devices_nearby[name]
        except Exception:
            return None
        return addr

    def find(self, target_name : string):
        self.scan()
        self.found = target_name in self.devices_nearby.keys()
        return self.found

    def connect(self , target_name , target_address) -> bool:
        self.find(target_name)
        if not self.found:
            return False
        sock = BluetoothSocket(RFCOMM)
        try:
            sock.connect((target_address , 1))
            data_dtr = ""
            while True:
                data = sock.recv(1024)
                data_dtr = data_dtr + data.decode()
                if '\n' in data.decode():
                    print(datetime.datetime.now().strftime("%H:%M:%S")+"->" + data_dtr[:-2])
                    data_dtr = ""
        except Exception as e:
            sock.close()
            self.connected = False
        self.connected = True
        return self.connected

class hardware():
    def __init__(self):
        cpuinfo = wmi.WMI()
        cpu = cpuinfo.Win32_Processor()[0]
        self.cpu_name = cpu.Name
        self.processor = platform.processor()
        self.cpu_core_num = psutil.cpu_count()
        self.frequency = psutil.cpu_freq()
        self.cpu_percent = cpu.LoadPercentage
        self.free_memory = psutil.virtual_memory().free / 1024 ** 3
        self.total_memory = psutil.virtual_memory().total / 1024 ** 3
        self.memory_percent = psutil.virtual_memory().percent
        self.system = platform.system()
        self.platform = platform.platform()
        self.system_version = platform.version()
        self.cpu_producer = platform.machine()
        self.pc_name = platform.node()
        self.info = platform.uname()
        self.system_bit = platform.architecture()[0]
        self.processorid = cpu.ProcessorId.strip()
        self.max_frequency = cpu.MaxClockSpeed