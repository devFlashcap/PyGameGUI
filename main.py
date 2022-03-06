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

    button = Button("asd", pygame.Rect(0,0,80,80), (255,0,0), (255,255,255), 20, TextAlign.Center, (0,0,0), (255,255,255), onClick = onClick)
    button2 = Button("fgh", pygame.Rect(0,0,80,80), (255,0,0), (255,255,255), 20, TextAlign.Center, (0,0,0), (255,255,255))
    button3 = Button("ijk", pygame.Rect(0,0,80,80), (0,255,0), (255,255,255), 20, TextAlign.Center, (0,0,0), (255,255,255))
    button4 = Button("asd", pygame.Rect(0,0,80,80), (0,0,255), (255,255,255), 20, TextAlign.Center, (0,0,0), (255,255,255))
    button5 = Button("fgh", pygame.Rect(0,0,80,80), (255,0,0), (255,255,255), 20, TextAlign.Center, (0,0,0), (255,255,255))

    verticalLayout = VerticalLayout(pygame.Rect(50,50,400,600))
    verticalLayout.addControl(button)
    verticalLayout.addControl(button2)
    verticalLayout.addControl(button3)
    verticalLayout.addControl(button4)
    verticalLayout.addControl(button5)

    while isRunning:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
        
        for control in verticalLayout.controls:
            if control.rect.collidepoint(pygame.mouse.get_pos()):
                control.hovered = True
            else:
                control.hovered = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            for control in verticalLayout.controls:
                if control.rect.collidepoint(pygame.mouse.get_pos()):
                    if control.onClick:
                        control.onClick()
            
        draw(window, verticalLayout)
        pygame.display.update()
        
    pygame.quit()

def draw(window, layout):
    window.fill((255,255,255))

    layout.draw(window)

def onClick():
    print("Clicked button 1");

main()