import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


import pygame

from server.network import Network
import pickle
#pygame.font.init()

width = 700
height = 700
#win = pygame.display.set_mode((width, height))
#pygame.display.set_caption("pyBall-Client")






class Client:
    def __init__(self,serverIp,screen,info,userinfo):
        self.serverIp = serverIp
        self.networkInterface = Network(self.serverIp)
        

    #at the start, send username to the server, receive data in return, which will be used to edit lobby. When the server says that the game has started, start the game and start looping that
    #once the game has started, send the server the normalised direction the player wishes to move in, and receive the game data in return. This will then be used to draw the game
    
    
    def preGameUpdate(self):
        print("nice")
      

    def clientMain(self):
        run = True
        clock = pygame.time.Clock()


        while run:
            clock.tick(60)
            try:
                game = self.networkInterface.send("get")
            except Exception as wow:
                print(wow)
                run = False
                print("Couldn't get game")
                break

newclient = Client("localhost")
while True:
    newclient.clientMain()