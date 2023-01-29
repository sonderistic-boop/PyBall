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

#typical haxball has 30 diameter, 50 for the outer
class Pawn(pg.sprite.Sprite):
    def __init__(self,name,team,isPlayer,surface,position,size):
        super().__init__()
        self.name = name
        self.team = team
        self.isPlayer = isPlayer
        self.surface = surface
        self.x,self.y = position
        self.w,self.h = size

        self.colour = pg.Color(themeColours[team])

        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(center = (self.w//2,self.h//2))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)


        

    
    def render(self):
        self.rect.center = (self.w//2,self.h//2)

        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)
        if self.isPlayer:
            pg.draw.circle(self.image,(255,255,255,51),(self.w//2,self.h//2),(self.w//2),int(0.12*(self.w//2)))
        self.surface.blit(self.image,(self.x,self.y))
        

    def renderGraphics(self):
        pg.draw.circle(self.image,(0,0,0),(self.w//2,self.h//2),(0.64*(self.w//2)))
        pg.draw.circle(self.image,self.colour,(self.h//2,self.h//2),(0.6*(self.w//2)))








