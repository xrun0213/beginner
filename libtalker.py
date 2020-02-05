#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import time, platform
import roslibpy

system = platform.system()
d = {'Darwin':'macOS', 'Linux':'Linux'}

client = roslibpy.Ros(host='10.1.1.3', port=9090)
talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')

def start_talking():    
    while client.is_connected:
        talker.publish( roslibpy.Message( {'data': 'talker from' + d[system]} ) )
        print('Sending message...')
        time.sleep(1)

    talker.unadvertise()


client.on_ready(start_talking)
client.run_forever()