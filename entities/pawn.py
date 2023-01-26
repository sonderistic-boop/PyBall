import pygame as pg
themeColours = {
    "RED" : "#d14242",
    "GREEN" : "#52d142",
    "BLUE" : "#52d142",
    "YELLOW" : "#e1c16e",
    "CYAN" : "#03b9b9",
    "MAGENTA" : "#674ea7",
    "ORANGE" : "#e69138"

}
#when assigning  team parameter, make  sure you do  so in all caps


class Pawn():
    def __init__(self,team,name,isPlayer):
        self.team = team
        self.name = name
        self.isPlayer = isPlayer


        self.colour = pg.Color(themeColours[team])
        self.maxVelocity = 50
        self.x = 
        self.y = 

    def render(self):







newguy = Pawn("BLUE","bigboyo",True)

print(newguy.team)