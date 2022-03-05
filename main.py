import pygame
from button import Button

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
    button = Button((0,0,200,40), (0,0,0), (255,255,255), 20)
    button.draw(window)

main()