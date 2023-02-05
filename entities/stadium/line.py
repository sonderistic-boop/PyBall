import pygame as pg


#always start line with the left most point
class Line(pg.sprite.Sprite):
    def __init__(self,surface,collidesWithPlayer,collidesWithBall,startPosition,endPosition,colour = (255,255,255)):
        super().__init__()
        self.surface = surface
        self.startPosition =  pg.math.Vector2(startPosition)
        self.endPosition =  pg.math.Vector2(endPosition)        
        self.colour = colour

        self.size = (endPosition[0]-startPosition[0],endPosition[1]-startPosition[1])
       



        #PHYICS
        self.static = True
        self.collideswithPlayer = collidesWithPlayer
        self.collideswithBall = collidesWithBall


        self.image = pg.Surface((self.size[0]+16,self.size[1]+16),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (self.startPosition[0]-8,self.startPosition[1]-8))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)


    def render(self):
        self.rect = self.image.get_rect(topleft = (self.startPosition[0]-8,self.startPosition[1]-8))

        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)

        self.surface.blit(self.image,(self.startPosition[0],self.startPosition[1]))


    def renderGraphics(self):
        pg.draw.line(self.image,self.colour,(0,0),(self.size[0],self.size[1]),8)

