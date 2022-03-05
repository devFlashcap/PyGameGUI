import pygame
from control import Control

class VerticalLayout(Control):
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

        slotHeight = self.rect.height / len(self.controls)

        for idx in range(0, len(self.controls)):
            yPos = slotHeight * idx + (slotHeight / 2 - self.controls[idx].rect.height / 2)
            self.controls[idx].setRect(pygame.Rect(self.rect.x, yPos, self.rect.width, self.controls[idx].rect.height))
            #pygame.draw.line(window, (0,0,0), (0, slotHeight * idx), (self.rect.width, slotHeight*idx), 4)

    
    def draw(self, window):
        self.calculateControlRects(window)
        for control in self.controls:
            control.draw(window)
            
