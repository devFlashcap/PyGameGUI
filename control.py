import pygame
import uuid

class Control:
    def __init__(self):
        self.id = uuid.uuid1()
        self.margin = (0,0,0,0)
        self.padding = (0,0,0,0)
        self.rect = None
        self.hovered = False
    
    def setRect(self, rect):
        self.rect = rect

