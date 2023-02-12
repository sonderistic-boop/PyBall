#make game class, with a run method, and a main method
#game should be 810x770
#game will have a stadium, a ball, and two teams
#game will have a run method, which will run the game
#game 
import pygame as pg
import math
import sys


import logic.physics as physics
from entities.pawn import Pawn
from entities.ball import Ball
import entities.stadium.stadiums as stadiums


class Game():
    def __init__(self,parentScreen,players,time,maxScore,stadium,colours):
        self.size = (810,770)
        #declares the parent screen, which is the screen that the game surface will be drawn on
        self.parentScreen = parentScreen
        #declares which stadium the game will be played on
        self.stadium = stadium

        #declares how long the game will last
        self.time = time
        #declares the maximum score the game will be played to
        self.maxScore = maxScore

        

        self.leftTeam = {}
        self.rightTeam = {}

        self.leftTeamScore = 0
        self.rightTeamScore = 0

        
        
        
        #load game surface, load players, load ball, load stadium
        

        self.screen = pg.Surface((self.size),pg.SRCALPHA)
        
        self.stadium = getattr(stadiums,stadium)
        self.stadium = self.stadium(self.screen,200,200)
        
        self.ball = Ball(self.screen,(self.stadium.bounds["middle"][0],self.stadium.bounds["middle"][0]),(30,30))
        
        #load players, and add them to the left and right team dictionaries. initial position will be the middle-left of the stadium for the left team, and the middle-right of the stadium for the right team
        for i in players["team1"]:
            self.leftTeam[i] = Pawn(i,colours["team1"],False,self.screen,(400,400),(70.3,70.3))          
        
        for i in players["team2"]:
            self.rightTeam[i] = Pawn(i,colours["team2"],False,self.screen,(400,400),(70.3,70.3))   

        
        
        
        #add sprite groups for ball, players, stadium parts

        #self.ballGroup = pg.sprite.GroupSingle(self.ball)


        self.playerGroup = pg.sprite.Group()
        self.playerGroup.add(self.leftTeam.values())
        self.playerGroup.add(self.rightTeam.values())


        self.stadiumBoundsGroup = pg.sprite.Group()
        self.stadiumBoundsGroup.add(self.stadium.lines.values())
        self.stadiumBoundsGroup.add(self.stadium.collidingGoals.values())

        self.stadiumGoalGroup = pg.sprite.Group()
        self.stadiumGoalGroup.add(self.stadium.goals.values())



    def run(self):
        #while the game is running, the game will run
        gameRunning = True
            #update the game
        self.update()
    
        self.render()
           


    def render(self):
        #draw the stadium, draw the ball, draw the players
        self.stadium.render()
        for i in self.playerGroup:
            i.render()
        self.ball.render()
        
        
        self.parentScreen.blit(self.screen,(0,100))
    
    def collisionChecker(self):
        #check for collisions between the ball and the players, and the ball and the stadium
        #check for collisions between the players and the stadium
        #check for collisions between the players and the other players
        #check for collisions between the ball and the goals
        #check for collisions between the players and the goals
        

        #check for collisions between the ball and the players
        ballPlayerCollisions = pg.sprite.spritecollide(self.ball,self.playerGroup,False,pg.sprite.collide_mask)

        ballStadiumCollisions = pg.sprite.spritecollide(self.ball,self.stadiumBoundsGroup,False,pg.sprite.collide_mask)

        ballGoalCollisions = pg.sprite.spritecollide(self.ball,self.stadiumGoalGroup,False,pg.sprite.collide_mask)

        playerStadiumCollisions = pg.sprite.groupcollide(self.playerGroup,self.stadiumBoundsGroup,False,pg.sprite.collide_mask)

        playerPlayerCollisions = pg.sprite.groupcollide(self.playerGroup,self.playerGroup,False,False,pg.sprite.collide_mask)


        for i in ballGoalCollisions:
            self.goalScored(i)


        for i in ballPlayerCollisions:
            physics.ballBallCollision(self.ball,i)

        
        
        #for i in ballStadiumCollisions:
        
    def goalScored(self,goal):
        if goal.team == "team1":
            self.leftTeamScore += 1
        elif goal.team == "team2":
            self.rightTeamScore += 1

        self.ball.reset()
        for i in self.playerGroup:
            i.reset()

    




        
        

        
    