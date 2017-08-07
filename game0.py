#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:03:18 2017

@author: nikos
"""

import pygame
import matplotlib as mpl

#scale matplotlib colormap back to 0-255 range
def mpl2rgb(cmap):
    return((cmap[0]*255,cmap[1]*255,cmap[2]*255,cmap[3]*255))
#%%
cmap = mpl.cm.Dark2
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        #if is_blue: color = (0, 128, 255)
        if is_blue: color = (0, 128, 255)
        else: color = mpl2rgb(cmap(0))
        #else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)

#pygame.display.quit()
pygame.quit()#this is necessary for the window to close when pressing (x)