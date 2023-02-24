
import pygame as pg
from client.ui.button import *
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
        self.buttons["Join Game"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),300),(200,50),"Join Game","JoinGame")
        self.buttons["Host Game"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),400),(200,50),"Host Game","HostGame")
        self.buttons["Settings"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),500),(200,50),"Settings","Settings")             
        self.buttons["Credits"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),600),(200,50),"Credits","Credits")
        self.buttons["Exit"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),700),(200,50),"Exit","Exit")
    
    
    
    
        
    
    def eventHandler(self,info):
        for button in self.buttons:
            checker = self.buttons[button].eventHandler(info)
            if checker != None:
                return checker




    def renderSlidingBackground(self):
        for i in range(0,len(self.backgroundX)):
            if self.backgroundX[i] <= -120:
                self.backgroundX[i] = self.surface.get_width() + 120
            for j in range(0,(self.surface.get_height()+120),120):
                
                self.surface.blit(self.background,(self.backgroundX[i],j))
                
            self.backgroundX[i] -= 1


      
    def renderLogo(self):
        self.surface.blit(self.logo,(((self.surface.get_width()/2)-(self.logo.get_width()/2)),100))
        
    
    def renderButtons(self):
        for button in self.buttons:
            self.buttons[button].render()
        
        
    
    def render(self):
       self.renderSlidingBackground()
       self.renderLogo()
       self.renderButtons()


    def main(self,events):
        checker = self.eventHandler(events)
        if checker != None:
            return checker
        self.render()



class JoinGame(Menu):
    def __init__(self,surface):
        self.surface = surface
        self.background = pg.transform.scale((pg.image.load("./shared/assets/background/background.png")),(120,120))
        self.backgroundX = []
        
        for i in range(-120,self.surface.get_width()+120,120):
            self.backgroundX.append(i)
        
        self.buttons = {}
        self.buttons["Back"] = MenuButton(self.surface,(((150),150)),(200,50),"Back","Menu")
        self.buttons["Join"] = MenuButton(self.surface,(((self.surface.get_width()/2)-100),700),(200,50),"Join","join")
        self.buttons["IP"] = InputButton(self.surface,(((self.surface.get_width()/2)-100),400),(200,50))
        self.buttons["Port"] = InputButton(self.surface,(((self.surface.get_width()/2)-100),500),(200,50))
        
       



    def renderSlidingBackground(self):
        return super(JoinGame,self).renderSlidingBackground()
    
        
    def eventHandler(self,info):
        for button in self.buttons:
            checker = self.buttons[button].eventHandler(info)
            if checker != None:
                return checker
            


    def renderSlidingBackground(self):
        for i in range(0,len(self.backgroundX)):
            if self.backgroundX[i] <= -120:
                self.backgroundX[i] = self.surface.get_width() + 120
            for j in range(0,(self.surface.get_height()+120),120):
                
                self.surface.blit(self.background,(self.backgroundX[i],j))
                
            self.backgroundX[i] -= 1


      
    def renderLogo(self):
        self.surface.blit(self.logo,(((self.surface.get_width()/2)-(self.logo.get_width()/2)),100))

    def renderButtons(self):
        for button in self.buttons:
            self.buttons[button].render()
    
    def render(self):
        self.renderSlidingBackground()
        s = pg.Surface((self.surface.get_width()-200,self.surface.get_height()-200))
        s.set_alpha(220)                
        s.fill((0,0,0)) 
        self.surface.blit(s,(100,100))
        self.renderButtons()

    def main(self,events):
        checker = self.eventHandler(events)
        if checker != None:
            return checker
        self.render()