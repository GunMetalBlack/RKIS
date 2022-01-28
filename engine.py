import config
import imageloader
import curses
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

def mainMenu(stdscr):
    curses.curs_set(0)
    while config.gameHasStarted == False:
      stdscr.erase()
      if(config.Awnser == 1):
        stdscr.addstr(imageloader.images("ui_s1"))
        if(UserInput("e")):
          config.gameHasStarted = True
        stdscr.refresh()
      elif(config.Awnser == 2):
        stdscr.addstr(imageloader.images("ui_s2"))
        stdscr.refresh()
      elif(config.Awnser == 3):
        stdscr.addstr(imageloader.images("ui_s3"))
        stdscr.refresh()
      if(UserInput("w")):
       config.Awnser = config.Awnser + 1
      if(config.Awnser > 3 or config.Awnser < 0):
        config.Awnser = 1

    



  
def LoadingGameMap(stdscr):
 for y, line in enumerate(config.map_01):
        for x, c in enumerate(line):
            if c == "0":
              stdscr.move(y,x)
              stdscr.addstr(imageloader.images("map_wall"))
            if c == "1":
              stdscr.move(y,x)
              stdscr.addstr(imageloader.images("map_empty"))
            #The Player is in the array
            if c == "2":
              stdscr.move(y,x)
              containers.SetPlayerPos(x,y)
              stdscr.addstr(imageloader.images("map_player"))
            if c == "3":
              stdscr.move(y,x)
              entity.Entity['chest']['Xpos'] = x
              entity.Entity['chest']['Ypos'] = y
              stdscr.addstr(entity.Entity['chest']['Graphic'])
              
        stdscr.addstr("")



def Draw_UI(stdscr):
  stdscr.addstr(imageloader.images("ui_screenbar"))     
  




def Game(stdscr):
    
    LoadingGameMap(stdscr)
    Draw_UI(stdscr)
    stdscr.refresh()
    containers.PlayerCollisionEntity()
    containers.PlayerMovement(stdscr)
    