import pygame as pg
# design a pygame window, and set the window title as pyBall
pg.init()
pg.display.set_caption("pyBall")
screen = pg.display.set_mode((1600, 1000))
# set up the clock
clock = pg.time.Clock()
# set up the main function for the game
def main():
    running = True
    while running:
        # set the maximum FPS
        clock.tick(60)
        # get all the events
        for event in pg.event.get():
            # if the event is to quit the game, then set running as False
            if event.type == pg.QUIT:
                running = False
        # update the display
        pg.display.update()


