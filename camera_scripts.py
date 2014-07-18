import pygame.camera
import time
import picamera
pygame.camera.init()

def webcam_take_photo(file_name, num_photos, interval):
    #find, open and start low-res camera
    cam_list = pygame.camera.list_cameras()
    webcam = pygame.camera.Camera(cam_list[0],(640,480))
    webcam.start()
    for i in range(1, num_photos+1):
        #grab image, scale and blit to screen
        imagen = webcam.get_image()
        pygame.image.save(imagen, file_name+str(i)+".jpg")
        time.sleep(interval)
    webcam.stop()
    
def picamera_take_photo(file_name, num_photos, interval):
    with picamera.PiCamera() as camera:
        for i in range(1, num_photos+1):
            camera.resolution = (800, 600)
            #camera.ISO = 800
            #Camera warm-up time
            #camera.shutter_speed = int(5e6)
            camera.rotation = 180
            #camera.exposure_mode = 'night'
            camera.capture(file_name+str(i)+".jpg",use_video_port=False)
            time.sleep(interval)
        

