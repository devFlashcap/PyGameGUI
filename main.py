import pygame
from button import Button
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
    button = Button("asd", pygame.Rect(0,0,200,40), (0,0,0), (255,255,255), 20, TextAlign.Right, padding=(20, 20, 20, 40))
    button2 = Button("fgh", pygame.Rect(0,0,200,60), (255,0,0), (255,255,255), 20, TextAlign.Center, padding=(20, 20, 20, 40))
    button3 = Button("ijk", pygame.Rect(0,0,200,40), (0,255,0), (255,255,255), 20)

    verticalLayout = VerticalLayout(pygame.Rect(0,0,600,600))
    verticalLayout.addControl(button)
    verticalLayout.addControl(button2)
    verticalLayout.addControl(button3)

    verticalLayout.draw(window)

main()