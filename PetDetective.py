#!/usr/bin/python
import smtplib, os
import subprocess
import thread

import RPi.GPIO as GPIO
import time
import sys

import PIL
from PIL import Image

sys.path.append("/home/pi/.local/lib/python2.7/site-packages/")

from gmail import send_mail_image
from camera_scripts import webcam_take_photo, picamera_take_photo

    
def image_resize(file_name, width): #pixels
    basewidth = width
    img = Image.open(file_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    #img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img = img.resize((basewidth, hsize))
    img.save(file_name)    

try:        
    GPIO.setmode(GPIO.BCM)
    PIR_PIN = 7
    GPIO.setup(PIR_PIN, GPIO.IN)
    print "PetDetective Started (CTRL+C to exit)"
    time.sleep(2)
    print "Ready"
    
    detection_cntr = 0
    file_name = "intruder"
    process = subprocess.Popen("sudo rm -rf intruder*.jpg", shell=True, stdout=subprocess.PIPE)
    process.wait()                
    UseWebCam = True
    num_photos_after_detect = 4

# Focus DSLR
    if UseWebCam == False:
        process = subprocess.Popen("sudo pktriggercord-cli --timeout 2 -f -o 'intruder'", shell=True, stdout=subprocess.PIPE)
        process.wait()
    
    while True:
        if GPIO.input(PIR_PIN) == 0:
            time.sleep(0.50)
            continue
        print "Motion Detected!" + " (" + str(detection_cntr) + ")"
        time.sleep(0.2)
        if GPIO.input(PIR_PIN) == 1:
            if UseWebCam == True:
                #webcam_take_photo("intruder",num_photos_after_detect,1)
                picamera_take_photo("intruder",num_photos_after_detect,1)
                
            else:
                process = subprocess.Popen("sudo pktriggercord-cli --timeout 2 -o 'intruder' --af_mode=AF.S --flash_mode=Manual", shell=True, stdout=subprocess.PIPE)
                process.wait()
                image_resize(file_name, 1024)
            send_mail_image(file_name,num_photos_after_detect)
            detection_cntr = 0
            process = subprocess.Popen("sudo rm -rf intruder*.jpg", shell=True, stdout=subprocess.PIPE)
            process.wait()                

                    
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()










