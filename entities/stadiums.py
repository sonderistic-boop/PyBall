#standard stadiums should be 24  pawns wide
import pygame as pg


class Stadium():
    def __init__(self,screen,position,size):


        self.screen = screen
        self.position = position
        self.size = size
        self.w,self.h = size
        self.pawns = []
        self.ball = None
        self.tiles = None
        



        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (position[0],position[1]))
        self.mask = pg.mask.from_surface(self.image)
       



class smallStadium(Stadium):
    

    def __init__(self,screen,position,size):
        super().__init__(screen,position,size)
        self.pawns = []
        self.ball = None
        self.tiles = None
        self.image = pg.Surface((self.w,self.h),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (position[0],position[1]))
        self.mask = pg.mask.from_surface(self.image)
        self.render()
