from ast import expr_context
import sys , os
import uiautomator2 as u

os.system('adb devices')
path = sys.argv[1]
error_wire = False
error_wireless = False
try:
    d = u.connect('74b96459')
    error_wire = False
except:
    error_wire = True

try:
    d = u.connect('192.168.31.15:6666')
    error_wireless = False
except:
    error_wireless = True

if not error_wireless and not error_wire:
    d.push(path , '/sdcard/')