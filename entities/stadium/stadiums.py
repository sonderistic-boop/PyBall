#standard stadiums should be 24  pawns wide
import pygame as pg
from entities.stadium.line import Line
from entities.stadium.goal.goal import collidingGoal
from entities.stadium.goal.goal import Goal

class Stadium():
    def __init__(self,screen,position,size):


        self.screen = screen
        self.position = position
        self.size = size
        self.w,self.h = size
        self.pawns = []
        self.teams = []
        self.ball = None
        self.tiles = None
        
        #Objects
        self.lines = {}
        self.collidingGoals = {}
        self.goals = {}
        self.arcs = {}




        

        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (position[0],position[1]))
        self.mask = pg.mask.from_surface(self.image)

    def render(self):
        self.renderGraphics()
        
    
    def renderGraphics(self):
        self.image.fill((0,0,0,0))
        for line in self.lines:
            self.lines[line].render()
        for collidingGoal in self.collidingGoals:
            self.collidingGoals[collidingGoal].render()
        
        for goal in self.goals:
            self.goals[goal].render()
        
        for arc in self.arcs:
            self.arcs[arc].render()






class smallStadium(Stadium):
    

    def __init__(self,screen,position,teams):
        super().__init__(screen,position,(1200,600))
        self.pawns = []
        self.teams = teams
        self.ball = None
        self.tiles = None

        self.bounds = {
         "x1" : self.position[0],
         "x2" : self.position[0]+self.size[0]-4,
         "y1" : self.position[1],
         "y2" : self.position[1]+self.size[1],
         "y3" : self.position[1]+(0.325*self.size[1]),
         "y4" : self.position[1]+self.size[1]-(0.325*self.size[1]),
         "xmiddle" : self.position[0]+(0.5*self.size[0]),
         "goalheight" : 0.35*self.size[1]+30,
        }

        #goal should be 210 down from top and 210 up from bottom
        self.lines = {
            "top" : Line(self.screen,False,True,(self.bounds["x1"],self.bounds["y1"]),(self.bounds["x2"],self.bounds["y1"])),
            "bottom" : Line(self.screen,False,True,(self.bounds["x1"],self.bounds["y2"]),(self.bounds["x2"],self.bounds["y2"])),


            "left1" : Line(self.screen,False,True,(self.bounds["x1"],self.bounds["y1"]),(self.bounds["x1"],self.bounds["y3"])),
            "left2" : Line(self.screen,False,True,(self.bounds["x1"],self.bounds["y4"]),(self.bounds["x1"],self.bounds["y2"])),
            "right1" : Line(self.screen,False,True,(self.bounds["x2"],self.bounds["y1"]),(self.bounds["x2"],self.bounds["y3"])),
            "right2" : Line(self.screen,False,True,(self.bounds["x2"],self.bounds["y4"]),(self.bounds["x2"],self.bounds["y2"])),


            "middle" : Line(self.screen,False,False,(self.bounds["xmiddle"],self.bounds["y1"]),(self.bounds["xmiddle"],self.bounds["y2"])),
        }

        self.collidingGoals = {
    
            "left": collidingGoal(self.screen,(self.bounds["x1"]-94,self.bounds["y3"]),self.bounds["goalheight"],self.teams[0],"left"),
            "right": collidingGoal(self.screen,(self.bounds["x2"],self.bounds["y3"]),self.bounds["goalheight"],self.teams[1],"right")
        }
    
        self.goals = {
            #"left": Goal(self.screen,(self.position[0],),(200,800),),
            #"right": Goal(self.screen,(self.position[0]+self.size[0],200),(1400,800))
        }


