import pygame as pg
import math
#import twisted
#import numpy as np

import sys # for sys.exit()


from entities.pawn import Pawn
from entities.ball import Ball

pg.init() # initialises pg

#the colours used in the game

themeColours = {
    "red" : "#d14242",
    "green" : "#52d142",
    "blue" : "#426ad1",
    "yellow" : "#e1c16e",
    "cyan" : "#03b9b9",
    "magenta" : "#674ea7",
    "orange" : "#e69138"

}
#the maximum number of ticks per second
maxTicks = 60

screen = pg.display.set_mode((1200,600),pg.SRCALPHA) # width, height
pg.display.set_caption("PyBall")


#need to set up a stadium class for future stadiums
field = pg.image.load("./assets/tiles/fieldtiles/fieldtile.jpg")

#the clock object
clock = pg.time.Clock()

def runtime():
    #the main function
    running = True
    newball = Ball(screen,(200,200),(20,20))
    newguy = Pawn("bigboyo","red",True,screen,(400,400),(50,50))
    guygroup =  (pg.sprite.GroupSingle(newguy))
    ballgroup = (pg.sprite.GroupSingle(newball))
    while running:
        #while running is true, the game will run
       
        clock.tick(maxTicks)

        for event in pg.event.get():
            #event handling loop
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    sys.exit()


                
        keys = pg.key.get_pressed()
        newguy.vel[0] += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 0.5
        newguy.vel[1] += (keys[pg.K_DOWN] - keys[pg.K_UP]) * 0.5
        
        collide = pg.sprite.spritecollide(newball, guygroup, False, pg.sprite.collide_mask)
        
      
        screen.fill((themeColours["green"]))
        screen.fill((255, 0, 0) if collide else (255, 255, 255))
        
        #screen.blit(field,(20,20))
        #pg.draw.circle(screen,themeColours["yellow"],(200,200),100)
        newguy.updatePhysics()
        newball.render()
        newguy.render()
        print(newguy.vel)
        pg.display.flip()
       





if __name__ == "__main__":
    runtime()
