#!/usr/bin/python
import smtplib, os
import subprocess
import thread

import RPi.GPIO as GPIO
import time

import PIL
from PIL import Image

from gmail import send_mail_message, send_mail_image

    
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
        cntr=0
        detection_cntr = 0
        file_name = "intruder-0000.jpg"
        os.remove(file_name) if os.path.exists(file_name) else None
        UseWebCam = True

# Focus DSLR
        if UseWebCam == False:
            process = subprocess.Popen("sudo pktriggercord-cli --timeout 2 -f -o 'intruder'", shell=True, stdout=subprocess.PIPE)
            process.wait()
        
        while True:
            GPIO.wait_for_edge(PIR_PIN, GPIO.RISING)
            print "Motion Detected!" + " (" + str(detection_cntr) + ")"
            time.sleep(0.50)
            if GPIO.input(PIR_PIN) == 1:
                if UseWebCam == True:
                    command = "fswebcam -r 640x480 -d /dev/video0 " + file_name
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                    process.wait()
                  #  image_resize(file_name, 480)
                else:
                    process = subprocess.Popen("sudo pktriggercord-cli --timeout 2 -o 'intruder' --af_mode=AF.S --flash_mode=Manual", shell=True, stdout=subprocess.PIPE)
                    process.wait()
                    image_resize(file_name, 1024)
                send_mail_image(file_name)
                detection_cntr = 0
                os.remove(file_name) if os.path.exists(file_name) else None

                

                    
except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()










