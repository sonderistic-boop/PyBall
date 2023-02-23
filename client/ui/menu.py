
import pygame as pg
from Button import *
from shared.themeColours import *
# set up a menu class, with a themeColours green background, and a join server, host server, settings, credits, and exit button


class Menu:
    def __init__(self,surface):
        
        
        self.surface = surface
        self.background = pg.transform.scale((pg.image.load("./shared/assets/background/background.png")),(120,120))
        self.logo = pg.image.load("./shared/assets/background/pyballlogo.png")
        self.backgroundX = []
        
        
        for i in range(-120,self.surface.get_width()+120,120):
            self.backgroundX.append(i)
        
        
        
        
        self.buttons = {}
        self.buttons["Join Game"] = MenuButton(self.surface,(self.surface.get_width()/2-100,300),(200,50),"Join Game","joinGame")
        self.buttons["Host Game"] = MenuButton(self.surface,(self.surface.get_width()/2-100,400),(200,50),"Host Game","hostGame")
        self.buttons["Settings"] = MenuButton(self.surface,(self.surface.get_width()/2-100,500),(200,50),"Settings","settings")             
        self.buttons["Credits"] = MenuButton(self.surface,(self.surface.get_width()/2-100,600),(200,50),"Credits","credits")
        self.buttons["Exit"] = MenuButton(self.surface,(self.surface.get_width()/2-100,700),(200,50),"Exit","exit")
    
    
    
    
    
    
    
    def renderSlidingBackground(self):
        for i in range(0,len(self.backgroundX):
            for j in range(0,self.surface.get_height()+120,120):
                self.screen.blit(self.background,(i,j))
            self.backgroundX[i] -= 1
        
            if self.backgroundX < -120:
                self.backgroundX = self.surface.get_width()+120


    
    def renderLogo(self):
        self.screen.blit(self.logo,self.surface.get_width()-(self.logo.get_width()/2),100)
         
    
    def renderButtons(self):
        for button in self.buttons:
                    button.render(
    
    def render(self):
       self.renderSlidingBackground(self)
       self.renderLogo(self)
       self.renderButtons(self)
                        
