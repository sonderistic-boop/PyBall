import pygame

pygame.init()


(width,height) = (1920,1080)
newScreen = pygame.display.set_mode((width,height))

def runtime():
    running = True
    while running is True:
        pygame.display.flip()


runtime()  



