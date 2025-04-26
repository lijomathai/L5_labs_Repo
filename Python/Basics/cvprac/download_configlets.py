from cvprac import cvp_client as cvp_client
import requests
import os


from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

cvp1 = "192.168.0.5"

cvp_user = 'arista'
cvp_pw = 'aristacnyc'

client = cvp_client.CvpClient()

client.connect([cvp1], cvp_user, cvp_pw)

configlets = client.api.get_configlets(start=0, end=0)

directory = 'configs'
exists = os.path.exists(directory)
if exists == False:
    os.makedirs(directory)

for configlet in configlets['data']:
    file_path = directory+'/'+configlet['name']+'.cfg'
    file = open(file_path, 'w')
    file.write(configlet['config'])
    file.close()
