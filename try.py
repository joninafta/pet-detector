import picamera
import time

with picamera.PiCamera() as camera:
    camera.resolution = (2048, 1536)
    #camera.ISO = 800
    #Camera warm-up time
    #camera.shutter_speed = int(5e6)
    camera.rotation = 180
    #camera.exposure_mode = 'night'
    camera.capture('foo.jpg',use_video_port=False)
    


