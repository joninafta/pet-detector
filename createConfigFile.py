# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:01:21 2015

@author: Joni
"""
import ConfigParser
config = ConfigParser.ConfigParser()

config.add_section('gmail')
config.set('gmail','addr',"SenderEmailAddress@gmail.com")
config.set('gmail','pass',"MyPassword")
configfile = open("defaults.cfg", 'wb')
config.write(configfile)
