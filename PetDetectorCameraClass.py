
import os
import time
import subprocess

import PIL
from PIL import Image
############################################################################

def image_resize(file_name, width): #pixels
    basewidth = width
    img = Image.open(file_name)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    #img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img = img.resize((basewidth, hsize))
    img.save(file_name)          


class camera():
    #hardware: {PentaxDSLR, WebCam, PiCamera}
    #numBurstPhotos: Number of photos taken when takePhoto method is called

    def __init__(self, hardware, fileNamePrefix):
        self.hardware = hardware
        self.fileNamePrefix = fileNamePrefix
        self.photosFileList = []
        self.cleanLocalFiles()

        
        # Focus DSLR
        if self.hardware == 'PentaxDSLR':
            process = subprocess.Popen("sudo pktriggercord-cli --timeout 2 -f -o 'dummmyPhoto'", shell=True, stdout=subprocess.PIPE)
            process.wait()
    
    def cleanLocalFiles(self):
        delCommand = 'sudo rm -f '+self.fileNamePrefix+'*.jpg'
        process = subprocess.Popen(delCommand , shell=True, stdout=subprocess.PIPE)
        process.wait()
        
    def takePhoto(self,numBurstPhotos, delayBetweenPhotos):
        self.photosFileList = []
        
        if self.hardware =='PentaxDSLR':
            for i in range(1,numBurstPhotos+1):
                command = "sudo pktriggercord-cli --timeout 2 -o "+ self.fileNamePrefix + str(i) + " --af_mode=AF.S --flash_mode=Manual"
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                process.wait()
                image_resize(file_name, 1024)
                
                
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                process.wait()
                time.sleep(delayBetweenPhotos)

         if self.harware == 'WebCam':
            #find, open and start low-res camera
            cam_list = pygame.camera.list_cameras()
            webcam = pygame.camera.Camera(cam_list[0],(640,480))
            webcam.start()
            for i in range(1, numBurstPhotos+1):
                #grab image, scale and blit to screen
                imagen = webcam.get_image()
                pygame.image.save(imagen, self.fileNamePrefix+str(i)+".jpg")
                time.sleep(delayBetweenPhotos)
            webcam.stop()                          
            
        if self.hardware == 'PiCamera':
            for i in range(1, numBurstPhotos+1):
                command = "raspistill -w 1024 -h 768 --nopreview -q 15 -vf -hf -ex auto -o " + self.fileNamePrefix+str(i)+".jpg"
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
                process.wait()    
                time.sleep(delayBetweenPhotos) 
                
        for i in range(1, numBurstPhotos+1):
            self.photosFileList.append(self.fileNamePrefix+str(i)+".jpg")
    
                 


        
        
        
        
        
        