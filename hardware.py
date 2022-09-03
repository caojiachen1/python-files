from __future__ import print_function
import pywifi
from pywifi import const
import sys,ctypes,time
from bluetooth import *
from bluetooth.windows import discover_devices

def get_admin():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None , "runas" , sys.executable , __file__ , None , 1)

class wifi():
    def __init__(self) -> None:
        global w,wireless,wifi_status,constlist
        constlist = ['DISCONNECTED' , 'SCANNING' , 'INACTIVE' , 'CONNECTING' , 'CONNECTED']
        self._update()
    
    def _update(self):
        global w,wireless,wifi_status
        w = pywifi.PyWiFi()
        wireless = w.interfaces()[0]
        wifi_status = wireless.status()
        self.status = constlist[wifi_status]

    def connect(self , ssid , password):
        self._update()
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
                self._update()
                return True
            else:
                self._update()
                return False
        else:
            print("Already WiFi Access")
        self._update()

    def disconnect(self):
        if self.status == 'CONNECTED':
            w = pywifi.PyWiFi()
            wireless = w.interfaces()[0]
            wireless.disconnect()
            time.sleep(2)
            self._update()

    def scan(self):
        wireless.scan()
        time.sleep(2)
        results = wireless.scan_results()
        wifi_results = []
        for profiles in results:
            d = {}
            d['ssid'] = profiles.ssid
            d['key'] = profiles.key
            if d['ssid'] != '':
                wifi_results.append(d)
        wifi_results = [dict(t) for t in set([tuple(d.items()) for d in wifi_results])]
        return wifi_results
    
class bluetooth():
    def __init__(self) -> None:
        global scanned,scanlist
        scanned = []
        scanlist = {}
        self.devices_nearby = {}

    def scan(self):
        global already,results
        a = discover_devices(lookup_names = True)
        already = []
        results = []
        for (addr , name) in a:
            if name not in already:
                if name == '':
                    name = 'Hidden'
                results.append({'Device:' : name , 'Mac:' : addr})
                already.append(name)
                self.devices_nearby[name] = addr
        return results

    def get_mac(self , name):
        self.scan()
        return self.devices_nearby[name]

        