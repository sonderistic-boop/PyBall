import pygame as pg

#this is a dictionary of colours, the keys are the names of the colours, and the values are the hex codes of the colours
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

#typical haxball player has 30 diameter, 50 for the outer, 

class Pawn(pg.sprite.Sprite):
    def __init__(self,name,team,isPlayer,surface,pos,size):

        #inherits from sprite class, assigns all variables declared at initialisation
        super().__init__()
        self.name = name
        self.team = team
        self.isPlayer = isPlayer
        self.surface = surface
        self.pos =  pg.math.Vector2(pos)
        self.size = size
        self.w,self.h = size
        self.colour = pg.Color(themeColours[team])


        #physics variables
        self.vel = pg.math.Vector2(0,0)

        #assigns the image and rect attributes to the sprite

        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (pos[0],pos[1]))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)


        

    #renders the pawn, and updates the mask, if the pawn is the player, a circle is drawn around the pawn
    def render(self):
        self.rect = self.image.get_rect(topleft = (self.pos[0],self.pos[1]))

        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)
        if self.isPlayer:
            pg.draw.circle(self.image,(255,255,255,51),(self.w//2,self.h//2),(self.w//2),int(0.12*(self.w//2)))

        

        self.surface.blit(self.image,(self.pos[0],self.pos[1]))
        
        
    #renders the graphics of the pawn, the outer circle and the inner circle
    def renderGraphics(self):
        pg.draw.circle(self.image,(0,0,0),(self.w//2,self.h//2),(0.64*(self.w//2)))
        pg.draw.circle(self.image,self.colour,(self.h//2,self.h//2),(0.6*(self.w//2)))


    def updatePhysics(self):
        
        self.pos  +=  self.vel
        self.vel *= 0.975
        







