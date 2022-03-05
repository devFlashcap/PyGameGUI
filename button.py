import pygame
from control import Control

class Button(Control):
    def __init__(self, rect, backgroundColor, fontColor, fontSize, hoverBackgroundColor = (0, 0, 0), hoverFontColor = (255, 255, 255), margin = ('0'), padding = ('0')):
        self.rect = rect
        self.backgroundColor = backgroundColor
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.hoverBackgroundColor = hoverBackgroundColor
        self.hoverFontColor = hoverFontColor
        self.margin = margin
        self.padding = padding
    
    def setRect(self, rect):
        self.rect = rect

    def draw(self, surface):
        pygame.draw.rect(surface, self.backgroundColor, self.rect)