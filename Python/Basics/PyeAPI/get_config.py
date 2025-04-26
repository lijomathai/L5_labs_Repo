#Part-2 of Python Lab
#----------------------------

import pyeapi
import yaml
import os

pyeapi.load_config('eapi.conf')


file = open('switches.yml','r')
switches_dict = yaml.safe_load(file)

directory = 'configs'
exists = os.path.exists(directory)
if exists == False:
    os.makedirs(directory)

for switch in switches_dict['devices']:
    print(switch)
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    config_file_path = directory+'/'+switch+'.cfg'
    print(config_file_path)
    file = open(config_file_path, 'w')
    file.write(running_config)
    file.close()
    print(f"Backed up {switch}")



