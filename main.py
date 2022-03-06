import pygame
from button import Button
from gridlayout import GridLayout
from horizontallayout import HorizontalLayout
from textalign import TextAlign
from verticallayout import VerticalLayout

pygame.init()

def main():

    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('PyGame GUI Test')
    
    isRunning = True
    clock = pygame.time.Clock()

    while isRunning:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            
        draw(window)
        pygame.display.update()
        
    pygame.quit()

def draw(window):
    window.fill((255,255,255))
    button = Button("asd", pygame.Rect(0,0,80,80), (0,0,0), (255,255,255), 20, TextAlign.Right)
    button2 = Button("fgh", pygame.Rect(0,0,80,80), (255,0,0), (255,255,255), 20, TextAlign.Center)
    button3 = Button("ijk", pygame.Rect(0,0,80,80), (0,255,0), (255,255,255), 20)
    button4 = Button("asd", pygame.Rect(0,0,80,80), (0,0,0), (255,255,255), 20, TextAlign.Right)
    button5 = Button("fgh", pygame.Rect(0,0,80,80), (255,0,0), (255,255,255), 20, TextAlign.Center)
    button6 = Button("ijk", pygame.Rect(0,0,80,80), (0,255,0), (255,255,255), 20)

    gridLayout = GridLayout(pygame.Rect(50,50,400,600), padding=(20, 20, 20, 20))

    gridLayout.addControl(button)
    gridLayout.addControl(button2)
    gridLayout.addControl(button3)

    gridLayout.addControl(button4)
    gridLayout.addControl(button5)
    gridLayout.addControl(button6)

    gridLayout.draw(window)

main()