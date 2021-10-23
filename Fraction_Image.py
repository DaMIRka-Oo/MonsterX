import random
import pygame, sys
from pygame.locals import *

class FractionImage:
    def __init__(self, imageName, surface, xsize, ysize, x, y):
        self.image_name=imageName
        self.surface=surface
        self.xsize=xsize
        self.ysize=ysize
        self.x=x
        self.y=y

        self.IMAGE = pygame.image.load(self.image_name).convert()  # or .convert_alpha()
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.xsize, self.ysize))
        # Create a rect with the size of the image.
        self.rect = self.IMAGE.get_rect()
        #self.met=met


    def setByField(self):
        self.rect.center = (self.x, self.y)
        self.surface.blit(self.IMAGE, self.rect)


    def collide(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click:
                return True


class PlayingCard(FractionImage):
    def __init__(self, imageName, surface, xsize, ysize, num, num1, picked, pos):
        if picked and pos==0:
            x = 200 + num1*150
            y = 370
        elif picked and pos==1:
            x = 200 + num1*150
            y = 520
        elif not(picked):
            x = 800 + num*70
            y = 445
        FractionImage.__init__(self, imageName, surface, xsize, ysize, x, y)
        self.num=num
        self.num1=num1
        self.picked=picked
        self.pos=pos

    def collide(self, mx, my, click):
        if self.rect.collidepoint((mx, my)):
            if click and not(self.picked):
                #print(self.num)
                return True,self.num
        return False,-1
