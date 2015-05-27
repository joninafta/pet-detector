#!/usr/bin/python
import os
import time
import sys

from PetDetectorEmailClass import email
from PetDetectorGpioClass import gpio
from PetDetectorCameraClass import camera


sys.path.append("/home/pi/.local/lib/python2.7/site-packages/")


try:
    sensor = gpio(7)       
    cam = camera('piCamera','intruder')
    mail = email('gmail','defaults.cfg')
    
    print "PetDetective Started (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"
    
    while True:
        if sensor.MovementDetected() == False:
            time.sleep(0.25)
            continue
        print "Motion Detected!"
        time.sleep(0.2)
        if sensor.MovementDetected() == True:
            #TakePhoto
            cam.takePhoto(4,1)
            mail.login()
            mail.sendMail('Movement Detected','',cam.photosFileList)
            cam.cleanLocalFiles()
                    
except KeyboardInterrupt:
    print "Quit"










