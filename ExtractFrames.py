# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:40:23 2022

@author: Farid
"""

import cv2

def ExtractFrames(source, dimensions):
    counter = 0
    frames = ()

    while (True):
        strcounter = f'{counter:03d}'
        tempsource = source+strcounter+".png"
        frame = cv2.imread(tempsource, cv2.IMREAD_UNCHANGED)
        
        try:
          frame = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
        except:
            break
      

        frames = frames + (frame,)
        counter += 1
        

    return frames,counter
