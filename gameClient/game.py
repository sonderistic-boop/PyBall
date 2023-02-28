#make game class, with a run method, and a main method
#game should be 810x770
#game will have a stadium, a ball, and two teams
#game will have a run method, which will run the game
#game 
import pygame as pg
import math
import sys


from gameClient.entities.pawn import Pawn
from gameClient.entities.ball import Ball
import gameClient.entities.stadium.stadiums as stadiums


class Game():
    def __init__(self,parentScreen,players,gameSettings,username):
        self.size = (1920,1080)
        #declares the parent screen, which is the screen that the game surface will be drawn on
        self.parentScreen = parentScreen
        #declares which stadium the game will be played on
        self.stadium = gameSettings["stadium"]
        self.username = username
        #declares how long the game will last
        self.time = gameSettings["time"]
        #declares the maximum score the game will be played to
        self.maxScore = gameSettings["maxScore"]

        self.colours = {
            "team1" : "red",
            "team2" : "blue"
        }

        self.leftTeam = {}
        self.rightTeam = {}

        self.leftTeamScore = 0
        self.rightTeamScore = 0

        
        
        
        #load game surface, load players, load ball, load stadium
        

        self.screen = pg.Surface((self.size),pg.SRCALPHA)
        
        self.stadium = getattr(stadiums,gameSettings["stadium"])
        self.stadium = self.stadium(self.screen,(100,100),[self.colours["team1"],self.colours["team2"]])
        
        
        self.ball = Ball(self.screen,(self.stadium.bounds["middle"][0],self.stadium.bounds["middle"][1]),(30,30))
        
        #load players, and add them to the left and right team dictionaries. initial position will be the middle-left of the stadium for the left team, and the middle-right of the stadium for the right team
        for i in players["team1"]:
            self.leftTeam[i] = Pawn(i,self.colours["team1"],(False | (self.username == i)),self.screen,(400,400),(70.3,70.3))          
        
        for i in players["team2"]:
            self.rightTeam[i] = Pawn(i,self.colours["team2"],False,self.screen,(400,400),(70.3,70.3))   

        
        
        
        #add sprite groups for ball, players, stadium parts

        #self.ballGroup = pg.sprite.GroupSingle(self.ball)


        


       

        
           


    def render(self):
        #draw the stadium, draw the ball, draw the players
        self.parentScreen.fill((136, 179, 120))
        self.stadium.render()
        for i in self.leftTeam:
            self.leftTeam[i].render()
        for i in self.rightTeam:
            self.rightTeam[i].render()
        self.ball.render()
        
        
        self.parentScreen.blit(self.screen,(0,50))

    

    
    
    #main function, takes the receivingData as a parameter, and then renders the items based on this
    # another function as well, getData() which getData() returns the position of the isMe player.
    def getData(self,info):
        data = {}
        data["actions"] = {
            "direction" : (0,0),
            "kicked" : False
            }
        """
        for player in self.leftTeam:
            if player.isPlayer is True:
                position = player.position
                
        for player in self.rightTeam:
            if player.isPlayer is True:
                position = player.position
           """
        


        #create a dictionary, with keys position, and actions. actions will have keys "kicked" and "direction" with a normalised vector of the direction of movement
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            data["actions"]["direction"] = (data["actions"]["direction"][0], data["actions"]["direction"][1] + 1)
        
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            data["actions"]["direction"] = (data["actions"]["direction"][0], data["actions"]["direction"][1] - 1)

        if keys[pg.K_a] or keys[pg.K_LEFT]:
            data["actions"]["direction"] = (data["actions"]["direction"][0] - 1, data["actions"]["direction"][1])

        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            data["actions"]["direction"] = (data["actions"]["direction"][0] + 1, data["actions"]["direction"][1])

        if keys[pg.K_x] or keys[pg.K_SPACE]:
            data["actions"]["kicked"] = True
                        
      
        
        return data
                    
                    
                    
                          
                        
                        
                  
            
        
         
        
    def update(self,receivingData):

        #update positions of every object
        #update the ball

        #update the players
        for player in self.leftTeam:
            self.leftTeam[player].update(receivingData["gameData"]["players"]["team1"][player])

            
        for player in self.rightTeam:
            self.rightTeam[player].update(receivingData["gameData"]["players"]["team2"][player]) 
        self.ball.update(receivingData["gameData"]["ball"])
        self.time = receivingData["gameData"]["timeRemaining"]
        self.leftTeamScore = receivingData["gameData"]["score"]["team1"]
        self.rightTeamScore = receivingData["gameData"]["score"]["team2"]

        
    def main(self,info,receivingData):
        #check for collisions, check for goals, check for time, check for score
        #update the ball, update the players
        #render the stadium, render the ball, render the players
        self.update(receivingData)

        self.render()
           
        
        
     
        
     

    




        
        

        
    