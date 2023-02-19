import pygame as pg
from button import Button
# set up a menu class, with a themeColours green background, and a join server, host server, settings, credits, and exit button


class Menu:
    def __init__(self,surface):
        self.surface = surface
        self.themeColours = [(0,255,0),(0,0,255),(255,0,0),(255,255,0),(255,0,255),(0,255,255)]
        self.buttons = []
        self.buttons.append(Button(self.surface,(self.surface.get_width()/2 - 100,self.surface.get_height()/2 - 100),(200,50),self.themeColours[0],"Join Server"))
        self.buttons.append(Button(self.surface,(self.surface.get_width()/2 - 100,self.surface.get_height()/2 - 50),(200,50),self.themeColours[1],"Host Server"))
        self.buttons.append(Button(self.surface,(self.surface.get_width()/2 - 100,self.surface.get_height()/2),(200,50),self.themeColours[2],"Settings"))
        self.buttons.append(Button(self.surface,(self.surface.get_width()/2 - 100,self.surface.get_height()/2 + 50),(200,50),self.themeColours[3],"Credits"))
        self.buttons.append(Button(self.surface,(self.surface.get_width()/2 - 100,self.surface.get_height()/2 + 100),(200,50),self.themeColours[4],"Exit"))

    def render(self):
        for button in self.buttons:
            button.render()
