import pygame as pg
import math
#import twisted
#import numpy as np
import sys


from entities.pawn import Pawn
pg.init() # initialises pg


themeColours = {
    "red" : "#d14242",
    "green" : "#52d142",
    "blue" : "#426ad1",
    "yellow" : "#e1c16e",
    "cyan" : "#03b9b9",
    "magenta" : "#674ea7",
    "orange" : "#e69138"

}

maxTicks = 60

screen = pg.display.set_mode((1200,600),pg.SRCALPHA) # width, height
pg.display.set_caption("PyBall")


field = pg.image.load("./assets/tiles/fieldtiles/fieldtile.jpg")

clock = pg.time.Clock()

def runtime():
    
    running = True
    newguy = Pawn("bigboyo","red",True,screen,(200,220),(50,50))
    while running:
       
        clock.tick(maxTicks)

        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    sys.exit()


                
        keys = pg.key.get_pressed()
        newguy.x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 1
        newguy.y += (keys[pg.K_DOWN] - keys[pg.K_UP]) * 1
                    
      
        screen.fill((themeColours["green"]))
        #screen.blit(field,(20,20))
        pg.draw.circle(screen,themeColours["yellow"],(200,200),100)
        newguy.render()
        pg.display.flip()
       





if __name__ == "__main__":
    runtime()
