
import time
import sys
sys.path.append("/home/pi/.local/lib/python2.7/site-packages/")
import picamera

with picamera.PiCamera() as camera:
    #camera.resolution = (2048, 1536)
    
    #Camera warm-up time
    #camera.shutter_speed = int(5e6)
    camera.rotation = 180
    camera.start_preview()
    camera.ISO = 100
    camera.led = False
    camera.sharpness = 50
    while (True):
        time.sleep(1)
        
    
    #camera.capture('foo.jpg',use_video_port=False)
    


