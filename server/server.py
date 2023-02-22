import socket
import pickle
from _thread import *
from network import get_ip
class pyBallServer:
    
    def __init__(self):
        
        self.port = 5555
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = get_ip()
        self.transferMode = "lobby"
        #two transferModes, "lobby" and "game". While lobby is active, client will send team to server, and server will send back-
        #teams of all players, and gamesettings in a pickle dump object with two dictionaries
        #admin can change any clients team, this request will take precedent over any other.
        #when joining, client will send their name, and receive, their stuff
        
        self.gamesettings = {
            "stadium" : "smallStadium",
            "time" : 5,
            "maxScore": 3 
            
        }
            
        self.players = {
            "team1" : {},
            "team2" : {},
            "neutral" : {}


        }
       
        #player should have name,address,
      
        try:
            self.serverSocket.bind((self.serverIP, self.port))
        except socket.error as e:
            str("Error")





        print("Server IP:", self.serverIP)
        self.serverSocket.listen()
        print("Waiting for a connection, Server Started")




    def newClient(self,connection, address):
        
        player = connection.recv(4096).decode() 
        
        self.players["neutral"][str(player)] = {"address": address}
        adminPrivilege = True
        data = {"team" : "neutral"}
        
        
        
        sendingDataLoad = pickle.dumps{"gameSettings" : self.gameSettings,
                                       "players" : self.players
                                      }
        connection.send(sendingDataLoad)
        
        
        #while true, receive data, which includes team of player
        #send data load, containing the aforementioned player and gamesettings. When a change in the transferMode occurs,
        #start transferring in gamestyle synchronous transmission, containing gameState, score, time remaining, and positions of ball and player

        
        
        while True:
            
            match self.TransferMode:
                
                case "lobby":
                    try:
                        receivingDataLoad = connection.recv(4096).decode()
                        receivingData = pickle.loads(receivingDataLoad) 

                    except:
                        break

                    if receivingData["team"] != data["team"]:
                        #change has occured in players selected team, rectify by deleting record of player in previous team and adding to new team
                        N = (self.players[(data["team"])][str(player)]).copy()
                        del self.players[(data["team"])][str(player)]
                        self.players[(receivingData["team"])][str(player)] = N

                    #additional checks, if player is an admin, if they made any changes to server

                    if adminPrivilege:
                        if "gameSettings" in receivingData:
                            if receivingData["gameSettings"] != self.gameSettings:
                                "self.gameSettings = receivingData["gameSettings"]
                        
                        if "transferMode" in receivingData:
                            self.transferMode = receivingData["transferMode"]





                    data = receivingDataLoad.copy()
                    #new initial data
                    sendingDataLoad = pickle.dumps{"gameSettings" : self.gameSettings,
                                                   "players" : self.players
                                                  }
                    connection.send(sendingDataLoad)
                    #send data
                    
                    
                case "game":
                    #if game, then try and receuve
                     try:
                        receivingDataLoad = connection.recv(4096).decode()
                        receivingData = pickle.loads(receivingDataLoad) 

                     except:
                        break
                
                
                
                
        
                
                
                
                
            
                
                
                
                
                
                

                
            
            

        print("Lost connection")
        try:
            print("deleting", player)
            del self.gamesettings["players"][player]
        except:
            pass
        connection.close()


    def connectionChecker(self):
        
        connection, address = self.serverSocket.accept()
        print("connected to:", address)
        


        start_new_thread(self.newClient, (connection,address))


        
        
        
        
        
   
 
servernew = pyBallServer()
 
while True:
    servernew.connectionChecker()
