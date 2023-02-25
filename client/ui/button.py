import pygame as pg

#set up a button class
class Button:
    def __init__(self,surface,pos,size,colour = (155,155,155,255),textColour = (255,255,255,255)):
        self.surface = surface
        self.position = pos
        self.size = size
        self.colour = colour
        self.borderColour = (0,0,0,255,255)
        self.text = ""
        self.textColour = textColour
        self.textSize = 20
        self.image = pg.Surface((self.size[0],self.size[1]),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (self.position[0],self.position[1]))
        

    def render(self):
        

        self.renderGraphics()

        
        
        if self.text != "":
            font = pg.font.SysFont("Arial",self.textSize)
            text = font.render(self.text,1,self.textColour)
            self.image.blit(text,(self.size[0]/2 - text.get_width()/2,self.size[1]/2 - text.get_height()/2))

        self.surface.blit(self.image,(self.position[0],self.position[1]))

    def renderGraphics(self):
        pg.draw.rect(self.image,self.colour,(0,0,self.size[0],self.size[1]))
        pg.draw.rect(self.image,self.borderColour,(0,0,self.size[0],self.size[1]),3)
        
        
    
    def eventHandler(self):
        pass
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

  
    def onEnable(self):
        pass

    def onDisable(self):
        pass

   





class MenuButton(Button):
    def __init__(self,surface,pos,size,text,redirect):
        super().__init__(surface,pos,size,(51,102,0,255),(255,255,255,255))
        self.text = text
        self.colour = (51,102,0,255)
        self.borderColour = (76,153,0,255)
        self.redirect = redirect

        
    def eventHandler(self,info):
        if self.rect.collidepoint((info["mouse"])):
            self.onHover()
            for event in info["events"]:
                
                match event.type:
                    case pg.MOUSEBUTTONDOWN:
                        return self.onClick()
        else:
            self.onLeave()
     
        
    def onClick(self):
        print(self.redirect)
        return self.redirect
    
    
    
    def onHover(self):
        self.borderColour = (255,255,255,255)
    
    def onLeave(self):
        self.borderColour = (76,153,0,255)





    

class InputButton(Button):
    def __init__(self,surface,pos,size):
        super().__init__(surface,pos,size,(0,0,0,150))
        self.borderColour = (0,0,0,150)
        self.trigger = False
        
    def eventHandler(self,info):
            for event in info["events"]:
                match event.type:
                    case pg.MOUSEBUTTONDOWN:
                        #if mouse click and mouseposition in rect
                        self.onClick(info)

                    case pg.KEYDOWN:
                        if self.trigger:
                            if event.key == pg.K_RETURN:
                                self.trigger = False
                                self.onTriggerExit()
                            elif event.key == pg.K_BACKSPACE:
                                self.text = self.text[:-1]
                            else:
                                self.text += event.unicode

    def onClick(self,info):
        if self.rect.collidepoint(info["mouse"]):
             if self.trigger == False:
                self.trigger = True
                self.onTrigger()
        else:
            if self.trigger:
                self.trigger = False
                self.onTriggerExit()


    def onTrigger(self):
        self.borderColour = (255,255,255,255)
        self.textColour = (255,255,255,255)
    
    def onTriggerExit(self):
        self.borderColour = (0,0,0,150)
        self.textColour = (128,128,128,255)

  



#make a drop down button, which is a button that when clicked, opens a dropdown menu, where option from a list are displayed. If the user clicks on one of the options, the button text is changed to the option that was clicked
class DropdownButton(Button):
    def __init__(self,surface,pos,size,optionList):
        super().__init__(surface,pos,size,(128,128,128,255))
        self.borderColour = (0,0,0,150)
        self.alternateColour = (180,180,180,255)
        self.trigger = False
        
        self.selectedOption = self.optionList[0]
        self.textColour = (128,128,128,255)
        self.textSize = 20
        self.optionButtons = {}
        for i in optionList:
            self.optionButtons[i] = MenuButton(self.surface,(self.position[0],self.position[1]+self.get),(self.size[0],self.size[1]),i,str(i))
    
    def eventHandler(self,info):

        if self.rect.collidepoint((info["mouse"])):
            self.onHover()
            for event in info["events"]:
                
                match event.type:
                    case pg.MOUSEBUTTONDOWN:
                        if self.trigger:
                            for i in self.optionButtons:
                                option = self.optionButtons[i].eventHandler(info)
                                if option != None:
                                    #swap places of selected option and option
                                    
                                    self.onClick()
        else:
            self.onLeave()
        
    def onClick(self):
        if self.trigger == False:
            self.trigger = True
            self.onTrigger()
        else:
            self.trigger = False
            self.onTriggerExit()
    

  






class ListButton(Button):
    def __init__(self,surface,pos,size,list):
        super().__init__(surface,pos,size,(150,150,150,255))
        self.borderColour = (0,0,0,150)
        self.list = {}
        self.trigger = False
        for i in list:
            self.list[i] = ListItemButton(self.surface,(self.position[0],self.position[1]+60),(self.size[0],self.size[1]),i)
        

        



        self.textColour = (255,255,255,255)
        self.textSize = 9

    def eventHandler(self,info):
        for i in self.list:
            self.list[i].eventHandler(info)
        
    def render(self):
        self.image.fill((128,128,128,128))
        #draw the text in the list
        self.surface.blit(self.image,(self.position[0],self.position[1]))
        for i in self.list:
            self.list[i].render()
        

    def removeItem(self,item):
        if item in self.list:
            self.list.remove(item)
    
    def addItem(self,item):
        if item not in self.list:
            self.list.append(item)
    
    def clearList(self):
        self.list = []
    

class InfoButton(Button):
    def __init__(self,surface,pos,size,info):
        super().__init__(surface,pos,size,(0,0,0,255))
        self.info = info
        self.textColour = (255,255,255,255)
        self.textSize = 9

    def render(self):
        self.image.fill(self.colour)
        #draw the info text
        if self.info != "":
            font = pg.font.SysFont("Arial",self.textSize)
            text = font.render(self.info,1,self.textColour)
            self.image.blit(text,(0,0))
    
        self.surface.blit(self.image,(self.position[0],self.position[1]))


class ListItemButton(Button):
    def __init__(self,surface,pos,size,text):
        super().__init__(surface,pos,size,(180,180,180,255))
        self.text = text

    def eventHandler(self,info):
            for event in info["events"]:
                match event.type:
                    case pg.MOUSEBUTTONDOWN:
                        #if mouse click and mouseposition in rect
                        self.onClick(info)

                    

    def onClick(self,info):
        if self.rect.collidepoint(info["mouse"]):
             if self.trigger == False:
                self.trigger = True
                self.onTrigger()
                return self.text
        
        else:
            if self.trigger:
                self.trigger = False
                self.onTriggerExit()


    def onTrigger(self):
        self.colour = (200,200,200,255)
       
    
    def onTriggerExit(self):
        self.colour = (180,180,180,255)

    def render(self):
        self.image.fill(self.colour)
        #draw the text in the list
        font = pg.font.SysFont("Arial",self.textSize)
        text = font.render(self.text,1,self.textColour)
        self.image.blit(text,(0,0))
        
        self.surface.blit(self.image,(self.position[0],self.position[1]))
       

        