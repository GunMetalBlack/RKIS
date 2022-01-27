import config
import imageloader
import containers
from readchar import readchar
import main
from colorama import init, Fore, Back, Style
import entity


def UserInput(keys):

  readKey = readchar()
  if(readKey == keys):
      keyisPressed = True
  else:
      keyisPressed = False
  return keyisPressed

def mainMenu(): 
    if(config.Awnser == 1):
          #Start Main Game Function
          print(imageloader.images("ui_s1"))
          if(UserInput("\r")):
            config.gameHasStarted = True
    elif(config.Awnser == 2):
      print(imageloader.images("ui_s2"))
      if(UserInput("\r")):
          main.replit.clear()
          print(Fore.BLUE + "Made By Noah Isaac")
          print(Fore.LIGHTMAGENTA_EX +"Started Jan 25,2022")
          input("Press the ENTER key twice to return:")
    elif(config.Awnser == 3):
        print(imageloader.images("ui_s3"))
        if(UserInput("\r")):
          main.replit.clear()
          print(Fore.LIGHTGREEN_EX + "LINK TO VIDEO OR WEBSITE")
          input("Press the ENTER key twice to return:")
    if(UserInput("w")):
      config.Awnser = config.Awnser + 1
    if(config.Awnser > 3 or config.Awnser < 0):
      config.Awnser = 1
  



  
def LoadingGameMap():
 for y, line in enumerate(config.map_01):
        for x, c in enumerate(line):
            if c == "0":
              print(imageloader.images("map_wall"),end = "")
            if c == "1":
              print(imageloader.images("map_empty"),end = "")
            #The Player is in the array
            if c == "2":
              containers.SetPlayerPos(x,y)
              print(imageloader.images("map_player"),end = "")
            if c == "3":
              entity.Entity['chest']['Xpos'] = x
              entity.Entity['chest']['Ypos'] = y
              print(entity.Entity['chest']['Graphic'],end = "")
        print()



def Draw_UI():
  print(imageloader.images("ui_screenbar"))     
  WritePos = config.player_x,config.player_y   
  rows =  [   ["Player Pos",str(WritePos),'',   ''],                   ['HEALTH:', 'b', 'c',    'd']         ,               ["1",   'bbbbbbbbbb', 'c',  'd']]
  widths = [max(map(len, col)) for col in zip(*rows)]
  for row in rows:
      print ("  ".join((val.ljust(width) for val, width in zip(row, widths))))
  print(entity.Entity[entity.EntityID[0]]['Xpos'],entity.Entity[entity.EntityID[0]]['Xpos'])




def Game():
    
    LoadingGameMap()
    Draw_UI()
    containers.PlayerCollisionEntity()
    containers.PlayerMovement()
    