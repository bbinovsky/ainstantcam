#!/usr/bin/env python

# Author:  Brian Binovsky
# Date:    5/17/2014
# Version: 1

import os
import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Webcam Test')
snapshot = pygame.surface.Surface((640, 480), 0, window)

camlist = pygame.camera.list_cameras()
print ("Running.")
if camlist:
    print ("Camera found.")
    cam = pygame.camera.Camera(camlist[0])
    cam.start()
    snapimages = True
    while snapimages:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                 print ("Key press detected.")
                 snapimages = False
        snapshot = cam.get_image(snapshot)
        window.blit(snapshot, (0,0))
        pygame.display.flip()
        pass
    print ("Done grabbing image.")

    pygame.image.save(snapshot,'camimage.jpg')
    print ("Image saved")
                               
    os.system("jp2a camimage.jpg --output=camimage.txt")
    print ("Text version of image saved")

    with open ("camimage.txt", "r") as textfile:
        text=textfile.read()
    print (text)
