import pygame

pygame.init()

running = False

(width,height) = (1920,1080)
newScreen = pygame.display.set_mode(width,height)

def runtime():
    running = True
    while running == True:
        pygame.display.flip()


runtime()  



