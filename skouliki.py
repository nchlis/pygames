# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:14:21 2017

@author: N.Chlis
"""

import pygame
import sys
import numpy as np
import matplotlib as mpl

MUSIC = False
FPS=60
#CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
XLIM = 400
YLIM = 300
#DISPLAY = pygame.display.set_mode((XLIM, YLIM))
#BACKGROUND = WHITE
#DISPLAY.fill(BACKGROUND)
#FONT = pygame.font.Font('freesansbold.ttf', 32)#font to write text, 32 textsize
#pygame.display.set_caption('skouliki_v0.1!')
x = 30
y = 30
#ballImg = pygame.image.load('ball.png').convert()
pressed_space = False

#play background music
if MUSIC==True:#play background music
    pygame.mixer.music.load('project0.wav')
    pygame.mixer.music.play(-1, 0.0)#loop indefinitely, starting track from 0.0s

#scale matplotlib colormap back to 0-255 range
def mpl2rgb(cmap):
    return((cmap[0]*255,cmap[1]*255,cmap[2]*255,cmap[3]*255))

BACKGROUND = BLACK

def main():
    global CLOCK, DISPLAY, FONT    
    #initialize pygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((XLIM, YLIM))
    DISPLAY.fill(BACKGROUND)
    FONT = pygame.font.Font('freesansbold.ttf', 32)#font to write text, 32 textsize
    pygame.display.set_caption('skouliki_v0.1!')
    
    welcome_screen()
    print('play!')
    play_game()
    
    #exit the game
    pygame.quit()
    #sys.exit()
    return None

def welcome_screen():
    while True:
        textSurface = FONT.render('Hit Enter to start',True,
                                  mpl2rgb(mpl.cm.Accent(0)), BACKGROUND)
        textRect = textSurface.get_rect()
        textRect.center = (XLIM/2, YLIM/2)#at the center of the screen
        DISPLAY.blit(textSurface, textRect)
        pygame.display.update()
        CLOCK.tick(FPS)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return                

def play_game():
    return

main()
#%%
    
while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if MUSIC==True:
                        pygame.mixer.music.stop()#stop playing background music
                    #show GAME OVER on the screen
                    textSurface = FONT.render('Game Over.',True, GREEN, WHITE)
                    textRect = textSurface.get_rect()
                    textRect.center = (XLIM/2, YLIM/2)#at the center of the screen
                    DISPLAY.blit(textSurface, textRect)
                    pygame.display.update()
                    #play explosion sound
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
            #time.sleep(1)#game lags for 1 s, but MUSIC keeps playing
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
