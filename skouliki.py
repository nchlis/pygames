# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:14:21 2017

@author: N.Chlis
"""

import pygame
import sys
import random
#import numpy as np
#import matplotlib as mpl
import time

MUSIC = False
SOUND = True
FPS=5
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
LIGHTGREEN = (127.0, 201.0, 127.0, 255.0)#mpl2rgb(mpl.cm.Accent(0))
BLUE = (0, 0, 255, 255)
XLIM = 640
YLIM = 480

GRIDSIZE = 20
assert XLIM % GRIDSIZE == 0, 'GRIDX must fit in window!'
assert YLIM % GRIDSIZE == 0, 'GRIDY must fit in window!'
GRIDX = XLIM/GRIDSIZE
GRIDY = YLIM/GRIDSIZE

#UP = 'up'
#DOWN = 'down'
#LEFT = 'left'
#RIGHT = 'right'

UP    = (0, -1)
DOWN  = (0, 1)
LEFT  = (-1, 0)
RIGHT = (1, 0)

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

def draw_square(surface, color, pos):
    #r = pygame.Rect((pos[0], pos[1]), (GRIDSIZE, GRIDSIZE))
    #pygame.draw.rect(surf, color, r)
    pygame.draw.rect(surface, color, pygame.Rect(pos[0], pos[1], GRIDSIZE, GRIDSIZE))
    
BACKGROUND = BLACK

def main():
    global CLOCK, DISPLAY, FONT, FONTsmall
    #initialize pygame
    pygame.init()
    CLOCK = pygame.time.Clock()
    DISPLAY = pygame.display.set_mode((XLIM, YLIM))
    DISPLAY.fill(BACKGROUND)
    FONT = pygame.font.Font('freesansbold.ttf', 32)#font to write text, 32 textsize
    FONTsmall = pygame.font.Font('freesansbold.ttf', 16)#font to write text, 32 textsize
    pygame.display.set_caption('skouliki_v0.1!')
    
    welcome_screen()
    print('play!')
    score = play_game()
    game_over(score)
    #exit the game
    time.sleep(2)#wait for 2 seconds
    pygame.quit()
    sys.exit()
    return None

def welcome_screen():
    while True:
        textSurface = FONT.render('Hit Enter to start',True,
                                  LIGHTGREEN, BACKGROUND)
        textRect = textSurface.get_rect()
        textRect.center = (XLIM/2, YLIM/2)#at the center of the screen
        DISPLAY.blit(textSurface, textRect)
        pygame.display.update()
        CLOCK.tick(FPS)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    return                

def game_over(score):
    print('Game Over. Score:',score)
    textSurface = FONT.render('Game Over. Score: '+str(score),True,
                                  LIGHTGREEN, BACKGROUND)
    textRect = textSurface.get_rect()
    textRect.center = (XLIM/2, YLIM/2)#at the center of the screen
    DISPLAY.blit(textSurface, textRect)
    if SOUND == True:
        soundObj = pygame.mixer.Sound('explosion.wav')
        soundObj.play()
    pygame.display.update()

def play_game():
    pause = False
    worm = Worm()
    apple = Apple()
    apple.relocate(worm)
    new_direction = LEFT
    score = 0
    while True:
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    new_direction = LEFT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    new_direction = RIGHT
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    new_direction = UP
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    new_direction = DOWN
                elif event.key == pygame.K_p:
                    pause = not pause
                elif event.key == pygame.K_ESCAPE:
                    return score
        
        if pause == False:
            DISPLAY.fill(BACKGROUND)
            #print('Score:',score)
            textSurface = FONTsmall.render('Score: '+str(score),True,
                                  LIGHTGREEN, BACKGROUND)
            textRect = textSurface.get_rect()
            textRect.topright = (XLIM-20, 10)#at the center of the screen
            DISPLAY.blit(textSurface, textRect)
            worm.direction = new_direction
            worm.move()
            if(worm.collision == True): return score#go to game over screen
            eaten=evaluate_eat(worm, apple)
            if eaten == True:
                if SOUND == True:
                    soundObj = pygame.mixer.Sound('coin2.wav')
                    soundObj.play()
                score += 1
                #print('score', score)
            worm.draw()
            apple.draw()
            pygame.display.update()
            CLOCK.tick(FPS+score/2)#gets harder the higher the score
        
    


class Worm:
    def __init__(self, color = GREEN):
        self._length = 1 #one cell
        #all x-y locations of worm cells, in the beginning just 1
        #in the middle of the screen
        self._location = [(int(GRIDX*GRIDSIZE/2),int(GRIDY*GRIDSIZE/2))]
        self._direction = LEFT
        self.color = GREEN
        self._collision = False
        #self.myprint()
    
    @property
    def head(self):
        return self._location[0]
    
    @property
    def length(self):
        return self._length
    
    @property
    def direction(self):
        return self._direction
    
    @direction.setter
    def direction(self,new_direction):
        is_valid = True
        if self._direction == LEFT and new_direction == RIGHT:
            is_valid = False
        elif self._direction == RIGHT and new_direction == LEFT:
            is_valid = False
        elif self._direction == UP and new_direction == DOWN:
            is_valid = False
        elif self._direction == DOWN and new_direction == UP:
            is_valid = False
        
        #only update direction if new direction is valid
        if is_valid == True:
            self._direction = new_direction
    
    @property
    def xcoords(self):
        c = []
        for l in self._location:
            c.append(l[0])
        return c
    
    @property
    def ycoords(self):
        c = []
        for l in self._location:
            c.append(l[0])
        return c
    
    @property
    def collision(self):
        return self._collision
    
    #when the apple is eaten, it turns into the worm's new head
    def grow(self, apple):
        self._length += 1
        self._location.insert(0,apple.location)
    
    #move one position in current direction
    def move(self):
        #x_cur = self.head[0]
        #y_cur = self.head[1]
        #print(x_cur,y_cur)
        x_new = self.head[0]+self.direction[0]*GRIDSIZE
        y_new = self.head[1]+self.direction[1]*GRIDSIZE
        #check for collisions
        if((x_new,y_new) in self._location): self._collision = True
        #print('new:', x_new, y_new)
        if x_new >= GRIDX*GRIDSIZE: self._collision = True
        if y_new >= GRIDY*GRIDSIZE: self._collision = True
        if x_new < 0: self._collision = True
        if y_new < 0: self._collision = True
        #update the position
        self._location.insert(0,(x_new,y_new))
        self._location.pop()
    
    def print_location(self):
        print('Worms\'s location:',self._location)
    
    def draw(self):
        for x, y in self._location:
            draw_square(DISPLAY, self.color, (x,y))
    
        
class Apple:
    def __init__(self, color = GREEN):
        self._location = None
        self.color = RED
        #self.myprint()
    
    @property
    def location(self):
        return self._location
    
    def relocate(self, worm=None):
        #do not place apple on a worm cell by chance
        #do not place on same row or column as the worm
        #get random integers from 1 to GRID-2 in order not to place the 
        #apple directly on the border, since it can be quite hard to get
        #especially later in the game when the worm speeds up
        if worm != None:
            x=random.randint(1,GRIDX-2)*GRIDSIZE
            while x in worm.xcoords:
                x=random.randint(1,GRIDX-2)*GRIDSIZE
            y=random.randint(1,GRIDY-2)*GRIDSIZE
            while y in worm.ycoords:
                y=random.randint(1,GRIDY-2)*GRIDSIZE
            self._location = (x,y)
        else:
            x=random.randint(1,GRIDX-2)*GRIDSIZE
            y=random.randint(1,GRIDY-2)*GRIDSIZE
            self._location = (x,y) 
    
    def print_location(self):
        print('Apple\'s location:',self.location)
    
    def draw(self):
        draw_square(DISPLAY, self.color, self._location)


def evaluate_eat(worm, apple):
    if worm.head == apple.location:
        worm.grow(apple)
        apple.relocate(worm)
        return True
    else:
        return False

#main()
#%reset -f

#%%
if __name__ == '__main__':
    main()
