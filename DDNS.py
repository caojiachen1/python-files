from baidubce.bce_client_configuration import *
from baidubce.services.dns import dns_client
from baidubce.auth.bce_credentials import *
from baidubce.exception import *
import socket

AK = 'e785a3c14c8f4f17983173db18244488'
SK = '39735f09986a480785c1687fd9bed092'

class domain():
    def __init__(self , domain):
        self.domain = domain
        self.AK = AK
        self.SK = SK
        self.config = BceClientConfiguration(credentials = BceCredentials(self.AK, self.SK), endpoint = 'dns.baidubce.com')
        self.client = dns_client.DnsClient(self.config)

    def get_current_ip():
        IPs = socket.getaddrinfo(socket.gethostname() , 80)
        host_list = [IP[4][0] for IP in IPs]
        host_dict = {'ipv4' : None , 'ipv6' : []}
        for i in host_list:
            if i.startswith('192'):
                host_dict['ipv4'] = i
            else:
                host_dict['ipv6'].append(i)
        return host_dict

    def domain_list(self):
        return self.client.list_zone()

    def info_list(self):
        result = self.client.list_record(zone_name = self.domain).records
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
        self.client.create_record(zone_name = self.domain , create_record_request = create_record_request)

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
        self.client.update_record(zone_name = self.domain , update_record_request = update_record_request , record_id = record_id)

    def delete_dns(self , name):
        if name not in list(self.info_list().keys()):
            print('Record does not exist!')
            return
        self.client.delete_record(zone_name = self.domain , record_id = self.info_list()[name]['id'])

    def delete_all_dns(self):
        for name in list(self.info_list().keys()):
            self.client.delete_record(zone_name = self.domain , record_id = self.info_list()[name]['id'])

mine = domain('visitcjc.top')
mine.delete_all_dns()





