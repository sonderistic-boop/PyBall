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


#typical ball  is 20 diameter

class Ball(pg.sprite.Sprite):
    def __init__(self,surface,pos,size):

        #inherits from sprite class, assigns all variables declared at initialisation
        super().__init__()
        self.surface = surface
        self.pos =  pg.math.Vector2(pos)
        self.w,self.h = size

        #assigns the image and rect attributes to the ball

        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (self.pos[0],self.pos[1]))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)
        
    #renders the ball, and updates the mask
    def render(self):
        self.rect = self.image.get_rect(topleft = (self.pos[0],self.pos[1]))

        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)

        self.surface.blit(self.image,(self.pos[0],self.pos[1]))
        
        
    #renders the graphics of the ball, the outer circle and the inner circle
    def renderGraphics(self):
        pg.draw.circle(self.image,(0,0,0),(self.w//2,self.h//2),((self.w//2)))
        pg.draw.circle(self.image,(255,255,255),(self.h//2,self.h//2),(0.83*(self.w//2)))




