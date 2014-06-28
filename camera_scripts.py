import sys
import pygame.camera
import time

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

