import pygame
from control import Control
from textalign import TextAlign

class Button(Control):
    def __init__(self, text, rect, backgroundColor, fontColor, fontSize, textAlign = TextAlign.Left, hoverBackgroundColor = (0, 0, 0), hoverFontColor = (255, 255, 255)):
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
        self.labelRect = None
    
    def calculateTextPosition(self):
        self.label = self.font.render(self.text, True, self.fontColor)
        self.labelRect = self.label.get_rect()
        
        textXPos = self.rect.x
        textYPos = self.rect.y + self.rect.height / 2 - self.labelRect.height / 2

        match self.textAlign:
            case TextAlign.Left:
                pass
            case TextAlign.Center:
                textXPos = textXPos + self.rect.width / 2 - self.labelRect.width / 2
            case TextAlign.Right:
                textXPos = textXPos + self.rect.width - self.labelRect.width

        return (textXPos, textYPos)

    def draw(self, window):
        pygame.draw.rect(window, self.backgroundColor, self.rect)
        
        textPosition = self.calculateTextPosition()
        window.blit(self.label, textPosition)


