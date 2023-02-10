from WakeOnLan_api import *

def boot_computer():
    try:
        mac = MAC
        print('正在向 ', mac, ' 发送魔法唤醒包！')
        mac = format_mac(mac)
        send_data = create_magic_packet(mac)
        send_magic_packet(send_data)
        return f'成功向{mac}发送唤醒包！'
    except Exception as e:
        print(e)

if __name__ == '__main__':
    boot_computer()
