import pygame as pg

#set up a button class
class Button:
    def __init__(self,surface,pos,size,colour = (255,255,255,0),text = "",textColour = (0,0,0),textSize = 20):
        super().__init__()
        self.surface = surface
        self.position = pos
        self.size = size
        self.colour = colour
        self.text = text
        self.textColour = textColour
        self.textSize = textSize
        self.image = pg.Surface((self.size[0],self.size[1]),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (self.position[0],self.position[1]))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)

    def render(self):
        self.rect = self.image.get_rect(topleft = (self.position[0],self.position[1]))
        self.renderGraphics()
        self.mask = pg.mask.from_surface(self.image)
        self.surface.blit(self.image,(self.position[0],self.position[1]))

    def renderGraphics(self):
        pg.draw.rect(self.image,self.colour,(0,0,self.size[0],self.size[1]))
        if self.text != "":
            font = pg.font.SysFont("Arial",self.textSize)
            text = font.render(self.text,1,self.textColour)
            self.image.blit(text,(self.size[0]/2 - text.get_width()/2,self.size[1]/2 - text.get_height()/2))


    def onClick(self):
        pass

    def onHover(self):
        pass

    def onLeave(self):
        pass

    def onDrag(self):
        pass

    def onDrop(self):
        pass

    def onTrigger(self):
        pass

    def onTriggerExit(self):
        pass

    def onTriggerStay(self):
        pass

    def onEnable(self):
        pass

    def onDisable(self):
        pass

    def onAwake(self):
        pass

    def onSleep(self):
        pass

    def onTriggerEnter(self):
        pass

    def onTriggerExit(self):
        pass