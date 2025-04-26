#Part-1 of Python Lab
#----------------------------

import yaml
import pyeapi

file = open('vlans.yml','r')
vlan_dict = yaml.safe_load(file)
# to print first VLAN in the file - vlans.yml
#print(vlan_dict['vlans'][0]['id'])

# to print the list of switches 
#print(vlan_dict['switches'])

#to print list of switches in line by line fashion
# for switch in vlan_dict['switches']:
#     print(switch)

# connect to eapi, using eapi to perform changes on EOS

# load peapi into memory

pyeapi.load_config('eapi.conf')

# connect = pyeapi.connect_to('leaf1')
# vlan_api = connect.api('vlans')
# vlan_api.create('10')
# vlan_api.set_name('10', 'DMZ')

# 1st Loop: Loop thru list iof switches & add vlans from list

for switch in vlan_dict['switches']:
    print(f"Connecting to {switch}:")
    connect = pyeapi.connect_to(switch)
    for vlan in vlan_dict['vlans']:
        vlan_api = connect.api('vlans')
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding vlan {vlan_id} with name {vlan_name}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)

