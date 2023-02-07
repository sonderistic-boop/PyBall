#make game class, with a run method, and a main method
#game should be 810x770
import pygame as pg
import math
import sys

from entities.pawn import Pawn
from entities.ball import Ball
import entities.stadium.stadiums as stadium
class Game():
    def __init__(self,screen,players,stadium):
        self.size = (810,770)
        self.screen = screen
        self.stadium = stadium
        self.ball = Ball(screen,(self.stadium.bounds["xmiddle"],self.stadium.bounds["ymiddle"]),(30,30))
        #load game surface, load players, load ball, load stadium
        



        self.ballgroup = pg.sprite.GroupSingle(self.ball)
        self.guygroup = pg.sprite.Group()

        for player in players:
            self.guygroup.add(Pawn(player[0],player[1],player[2],screen,(400,400),(70.3,70.3)))
        self.arc = Arc(screen,(600,400),30,(0,math.pi/2),(255,255,255,128))
        self.arcgroup = pg.sprite.GroupSingle(self.arc)
    