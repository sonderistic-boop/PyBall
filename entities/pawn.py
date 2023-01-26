import pygame as pg
themeColours = {
    "red" : "#d14242",
    "green" : "#52d142",
    "blue" : "#426ad1",
    "yellow" : "#e1c16e",
    "cyan" : "#03b9b9",
    "magenta" : "#674ea7",
    "orange" : "#e69138"

}
#when assigning  team parameter, make  sure you do  so in all caps, also positon should be a tuple


class Pawn():
    def __init__(self,name,team,isPlayer,surface,position):
        self.name = name
        self.team = team
        self.isPlayer = isPlayer
        self.surface = surface
        self.x,self.y = position


        self.colour = pg.Color(themeColours[team])
        

    def render(self):
        pg.draw.circle(self.surface,(0,0,0),(self.x,self.y),17,0)
        pg.draw.circle(self.surface,self.colour,(self.x,self.y), 15, 0)








