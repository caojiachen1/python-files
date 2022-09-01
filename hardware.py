import pywifi
from pywifi import const
import sys,ctypes,time
from __future__ import print_function

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
        global w,wireless
        w = pywifi.PyWiFi()
        wireless = w.interfaces()[0]
        wireless.disconnect()
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
                return True
            else:
                return False
        else:
            print("已有wifi连接")
        self._update()

    def disconnect(self):
        if self.status == 'CONNECTED':
            w = pywifi.PyWiFi()
            wireless = w.interfaces()[0]
            wireless.disconnect()
    

        