import sys
import pygame.camera

pygame.camera.init()

def webcam_take_photo(file_name, num_photos, interval)
    #find, open and start low-res camera
    cam_list = pygame.camera.list_cameras()
    webcam = pygame.camera.Camera(cam_list[0],(32,24))
    webcam.start()

    for i in range(0, num_photos-1):
        #grab image, scale and blit to screen
        imagen = webcam.get_image()
        #imagen = pygame.transform.scale(imagen,(640,480))
        pygame.image.save(imagen, file_name+str(i)+"jpg")
        system.sleep(interval)

    webcam.stop()

