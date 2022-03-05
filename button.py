import pygame
from control import Control
from textalign import TextAlign

class Button(Control):
    def __init__(self, text, rect, backgroundColor, fontColor, fontSize, textAlign = TextAlign.Left, hoverBackgroundColor = (0, 0, 0), hoverFontColor = (255, 255, 255), padding = (0,0,0,0)):
        self.rect = rect
        self.backgroundColor = backgroundColor
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.hoverBackgroundColor = hoverBackgroundColor
        self.hoverFontColor = hoverFontColor
        self.font = pygame.font.Font(None, fontSize)
        self.textAlign = textAlign
        self.text = text
        self.label = None
        self.labelPosition = None
        self.padding = padding
        self.calculatePaddings()
        self.calculateTextPosition()
    
    def calculateTextPosition(self):
        self.label = self.font.render(self.text, True, self.fontColor)
        labelRect = self.label.get_rect()

        paddingTop, paddingBottom, paddingLeft, paddingRight = self.padding
        
        textXPos = self.rect.x + paddingLeft - paddingRight
        textYPos = self.rect.y + self.rect.height / 2 - labelRect.height / 2 + paddingTop - paddingBottom

        match self.textAlign:
            case TextAlign.Left:
                textXPos = textXPos
            case TextAlign.Center:
                textXPos = textXPos + self.rect.width / 2 - labelRect.width / 2
            case TextAlign.Right:
                textXPos = textXPos + self.rect.width - labelRect.width


        if textYPos + labelRect.height > self.rect.bottom:
            textYPos = self.rect.bottom - labelRect.height
        if textYPos < 0:
            textYPos = 0

        if textXPos + labelRect.width > self.rect.right:
            textXPos = self.rect.right - labelRect.width
        if textXPos < 0:
            textXPos = 0

        self.labelPosition = (textXPos, textYPos)
    
    def calculatePaddings(self):
        paddingTop, paddingBottom, paddingLeft, paddingRight = self.padding

        self.rect.height = self.rect.height + paddingTop + paddingBottom
        self.rect.width = self.rect.width + paddingLeft + paddingRight


    def draw(self, window):
        pygame.draw.rect(window, self.backgroundColor, self.rect)
        textPosition = self.calculateTextPosition()
        window.blit(self.label, self.labelPosition)


