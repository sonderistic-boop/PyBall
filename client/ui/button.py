import pygame as pg

#set up a button class
class Button:
    def __init__(self,surface,pos,size,colour = (155,155,155,0),textColour = (255,255,255)):
        self.surface = surface
        self.position = pos
        self.size = size
        self.colour = colour
        self.borderColour = (0,0,0)
        self.text = ""
        self.textColour = textColour
        self.textSize = 20
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
        pg.draw.rect(self.image,self.colour,self.rect)
        pg.draw.rect(self.image,self.borderColour,self.rect,4)
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

   


class menuButton(Button):
    def __init__(self,surface,pos,size,text,redirect):
        super().__init__(surface,pos,size,(51,102,0,0),(255,255,255))
        self.text = text
        self.borderColour = (76,153,0,0)
        self.redirect = redirect

    def onClick(self):
        return self.redirect
    
    def onHover(self):
        
        self.borderColour = (255,255,255,0)
    
    def onLeave(self):
        self.borderColour = (76,153,0,0)
    
    
        
