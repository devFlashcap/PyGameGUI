import pygame
from control import Control

class HorizontalLayout(Control):
    def __init__(self, rect):
        self.rect = rect
        self.controls = []
    
    def addControl(self, control):
        self.controls.append(control)
    
    def removeControl(self, cID):
        control = [c for c in self.controls if c.id == cID]
        self.controls.remove(control)

    def calculateControlRects(self, window):
        
        if len(self.controls) == 0:
            return

        slotWidth = self.rect.width / len(self.controls)

        for idx in range(0, len(self.controls)):
            xPos = slotWidth * idx + (slotWidth / 2 - self.controls[idx].rect.width / 2)
            self.controls[idx].setRect(pygame.Rect(xPos, self.rect.y, self.controls[idx].rect.width, self.rect.height))
            pygame.draw.line(window, (0,0,0), (slotWidth * idx, 0), (slotWidth*idx, self.rect.height), 4)

    
    def draw(self, window):
        self.calculateControlRects(window)
        for control in self.controls:
            control.draw(window)
            
