#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 21:03:18 2017

@author: nikos
"""

import pygame
import matplotlib as mpl
import sys
import time

#scale matplotlib colormap back to 0-255 range
def mpl2rgb(cmap):
    return((cmap[0]*255,cmap[1]*255,cmap[2]*255,cmap[3]*255))

cmap = mpl.cm.Dark2
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init
FPS=60
CLOCK = pygame.time.Clock()
#%% moving box that changes color

DISPLAY = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Welcome to game0!')
is_blue = True
x = 30
y = 30
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        #sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        DISPLAY.fill((0, 0, 0))
        #if is_blue: color = (0, 128, 255)
        if is_blue: color = (0, 128, 255)
        else: color = mpl2rgb(cmap(0))
        #else: color = (255, 100, 0)
        pygame.draw.rect(DISPLAY, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.update()
        CLOCK.tick(FPS)
print('Done!')
#pygame.display.quit()
#pygame.quit()#this is necessary for the window to close when pressing (x)
        
#%% moving ball
#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init
MUSIC = True
FPS=60
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 0, 255)
BACKGROUND = WHITE
DISPLAY = pygame.display.set_mode((400, 300))
DISPLAY.fill(BACKGROUND)
pygame.display.set_caption('Welcome to game0!')
x = 30
y = 30
ballImg = pygame.image.load('ball.png').convert()
pressed_space = False

if MUSIC==True:#play background music
    pygame.mixer.music.load('project0.wav')
    pygame.mixer.music.play(-1, 0.0)#loop indefinitely, starting track from 0.0s

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if MUSIC==True:
                        pygame.mixer.music.stop()#stop playing background music
                    soundObj = pygame.mixer.Sound('explosion.wav')
                    soundObj.play()
                    time.sleep(1)#wait for 1 second
                    pygame.quit()
                    #sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pressed_space = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        DISPLAY.fill(BACKGROUND)
        DISPLAY.blit(ballImg, (x, y))
        
        if pressed_space: 
            #DISPLAY.fill((0, 0, 0))
            pressed_space = False
            time.sleep(1)#game lags for 1 s, but MUSIC keeps playing
            if BACKGROUND == BLACK:
                BACKGROUND = WHITE
                print('black->white')
            elif BACKGROUND == WHITE:
                BACKGROUND = BLACK
                print('white->black')
            #DISPLAY.fill(BACKGROUND)
        
        pygame.display.update()
        CLOCK.tick(FPS)
print('Done!')





























