import pygame
from control import Control

class Button(Control):
    def __init__(self, rect, backgroundColor, fontColor, fontSize, hoverBackgroundColor = (0, 0, 0), hoverFontColor = (255, 255, 255)):
        self.rect = rect
        self.backgroundColor = backgroundColor
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.hoverBackgroundColor = hoverBackgroundColor
        self.hoverFontColor = hoverFontColor

    def draw(self, window):
        pygame.draw.rect(window, self.backgroundColor, self.rect)