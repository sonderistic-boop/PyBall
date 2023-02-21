import socket
import pickle
from _thread import *
from network import get_ip
class pyBallServer:
    
    def __init__(self):
        
        self.port = 5555
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverIP = get_ip()
        
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
        connection.send(str.encode("received"))
        player = connection.recv(4096).decode()
        print(player)

        self.players["neutral"][player] = {"address": address}
        
        while True:
            try:
                data = connection.recv(4096).decode()
                #first data received should  be the player name,

             
                    

                
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
