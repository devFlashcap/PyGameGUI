import pygame
from control import Control

class GridLayout(Control):
    def __init__(self, rect, padding = (0,0,0,0)):
        self.rect = rect
        self.controls = []
        self.padding = padding
    
    def addControl(self, control):
        self.controls.append(control)
    
    def removeControl(self, cID):
        control = [c for c in self.controls if c.id == cID]
        self.controls.remove(control)
    
    def calculateSlotSize(self):
        paddingTop, paddingBottom, paddingLeft, paddingRight = self.padding

        slotWidth = max(control.rect.width for control in self.controls) + paddingLeft + paddingRight
        slotHeight = max(control.rect.height for control in self.controls) + paddingTop + paddingBottom
        return (slotWidth, slotHeight)

    def calculateControlRects(self, window):
        
        if len(self.controls) == 0:
            return

        slotWidth, slotHeight = self.calculateSlotSize()
        slotsPerRow = self.rect.width // slotWidth

        currentRow = 0
        currentColumn = 0

        for idx in range(0, len(self.controls)):
            xPos = self.rect.x + currentColumn * slotWidth
            yPos = self.rect.y + currentRow * slotHeight
            self.controls[idx].setRect(pygame.Rect(xPos, yPos, self.controls[idx].rect.width, self.controls[idx].rect.height))
            if currentColumn + 1 == slotsPerRow:
                currentRow = currentRow + 1
                currentColumn = 0
            else:
                currentColumn = currentColumn + 1
            #pygame.draw.line(window, (0,0,0), (0, slotHeight * idx), (self.rect.width, slotHeight*idx), 4) 

    
    def draw(self, window):
        self.calculateControlRects(window)
        for control in self.controls:
            control.draw(window)
            
