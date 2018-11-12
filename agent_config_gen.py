#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import boto3
import json
import os

ip=[]

client = boto3.client('ec2', region_name='us-west-2')
response = client.describe_instances( Filters = [ 
    {'Name': 'tag:Service',
     'Values': ['conusl']
        }
    ]
)


for i in response['Reservations']:
    ip.append(str(i['Instances'][0]['PrivateIpAddress']))


config = {
    "datacenter": "aws",
    "data_dir": "/var/consul",
    "domain": "consul",
    "enable_script_checks": bool('true'),
    "leave_on_terminate": bool('true'),
    "rejoin_after_leave": bool('true'),
    "server": bool(0),
    "start_join": [
        str(i) for i in ip
    ]
}

# config_json = json.dumps(
#     config, sort_keys=True, indent=4, separators=(',', ': '))
# print (config_json)

with open('./prom-monitor-dyn/consul/agent/consul.json', 'w') as outfile:
    json.dump(config, outfile, sort_keys=True,indent=4, separators=(',', ': '))

os.system('sudo docker-compose -f docker-compose-agent.yml up')
