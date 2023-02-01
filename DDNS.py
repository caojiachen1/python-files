from baidubce.bce_client_configuration import *
from baidubce.services.dns import dns_client
from baidubce.auth.bce_credentials import *
import socket , requests

class domain():
    def __init__(self , domain):
        self.domain = domain
        self.__AK = 'e785a3c14c8f4f17983173db18244488'
        self.__SK = '39735f09986a480785c1687fd9bed092'
        self.__config = BceClientConfiguration(credentials = BceCredentials(self.__AK, self.__SK), endpoint = 'dns.baidubce.com')
        self.__client = dns_client.DnsClient(self.__config)

    def get_current_all_ip():
        IPs = socket.getaddrinfo(socket.gethostname() , 80)
        host_list = [IP[4][0] for IP in IPs]
        host_dict = {'ipv4' : None , 'ipv6' : []}
        for i in host_list:
            if i.startswith('192'):
                host_dict['ipv4'] = i
            else:
                host_dict['ipv6'].append(i)
        return host_dict

    def get_current_public_ipv6(self):
        return requests.get('https://v6.ident.me').text

    def domain_list(self):
        a = self.__client.list_zone().zones
        return [
            {'id' : zone.id ,
            'name' : zone.name , 
            'status' : zone.status , 
            'product_version' : zone.product_version , 
            'create_time' : zone.create_time , 
            'expire_time' : zone.expire_time} 
            for zone in a
        ]

    def info_list(self):
        result = self.__client.list_record(zone_name = self.domain).records
        info = {
            record.rr: {'id': record.id, 'value': record.value}
            for record in result
        }
        return info

    def create_dns(self , name , type , value):
        if name in list(self.info_list().keys()):
            self.update_dns(name, type, value)
            return
        create_record_request = {
            'rr': name,
            'type': type,
            'value': value
        }
        self.__client.create_record(zone_name = self.domain , create_record_request = create_record_request)

    def update_dns(self , name , type , value):
        if name not in list(self.info_list().keys()):
            print('Record does not exist!')
            return
        if value == self.info_list()[name]['value']:
            print('Do not need to change!')
            return
        update_record_request = {
            'rr': name,
            'type': type,
            'value': value
        }
        record_id = self.info_list()[name]['id']
        self.__client.update_record(zone_name = self.domain , update_record_request = update_record_request , record_id = record_id)

    def delete_dns(self , name):
        if name not in list(self.info_list().keys()):
            print('Record does not exist!')
            return
        self.__client.delete_record(zone_name = self.domain , record_id = self.info_list()[name]['id'])

    def delete_all_dns(self):
        if not self.info_list():
            return
        for name in list(self.info_list().keys()):
            self.__client.delete_record(zone_name = self.domain , record_id = self.info_list()[name]['id'])

    def ddns(self, name):
        if self.info_list().keys().__len__() == 1:
            a = list(self.info_list().keys())
            if a[0] == name:
                print('yes')
                if self.info_list()[name]['value'] != self.get_current_public_ipv6():
                    self.update_dns(name , 'AAAA' , self.get_current_public_ipv6())
        else:
            self.delete_all_dns()
            self.create_dns(name , 'AAAA' , mine.get_current_public_ipv6())

mine = domain('visitcjc.top')

mine.ddns('www')
