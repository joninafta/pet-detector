import sys
import pygame.camera

pygame.camera.init()


#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(32,24))
webcam.start()

#grab image, scale and blit to screen
imagen = webcam.get_image()
imagen = pygame.transform.scale(imagen,(640,480))
pygame.image.save(imagen, "image.jpg")
webcam.stop()
sys.exit()
