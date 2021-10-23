import random
import pygame, sys
from pygame.locals import *

class DrawText:
    def __init__(self, text, font, color, surface, x, y):
        self.text=text
        self.font=font
        self.color=color
        self.surface=surface
        self.x=x
        self.y=y
        #self.met=met
        self.textobj = self.font.render(self.text, 1, self.color)
        self.textrect = self.textobj.get_rect()
        self.textrect.topleft = (self.x, self.y)

    def setByField(self):
        self.surface.blit(self.textobj, self.textrect)


    def collide(self, mx, my, click):
        if self.textrect.collidepoint((mx, my)):
            if click:
                return True


def drawText(text, font, color, surface, x, y):
    textObj = font.render(text, 1, color)
    textRect = textObj.get_rect()
    textRect.topleft = (x, y)
    surface.blit(textObj, textRect)
