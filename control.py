import pygame
import uuid

class Control:
    def __init__(self):
        self.id = uuid.uuid1()
        self.margin = ('0')
        self.padding = ('0')
        self.rect = None
    
    def setRect(self, rect):
        self.rect = rect

