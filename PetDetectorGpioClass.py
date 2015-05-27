# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:06:14 2015

@author: Jonathan
"""
import RPi.GPIO as GPIO

class gpio():
    def __init__(self,pir_pin = 7):
        self.pir_pin = pir_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pir_pin, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()
        
    def MovementDetected(self):
        if GPIO.input(self.pir_pin) == 0:
            return False
        else:
            return True