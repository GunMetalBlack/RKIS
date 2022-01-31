import config
import imageloader
import curses
import containers
import time
import main
import random
import entity



def UserInput(stdscr,keys):

  readKey = stdscr.getch()
  if(readKey == ord(keys)):
      keyisPressed = True
  else:
      keyisPressed = False
  return keyisPressed

def mainMenu(stdscr):
    curses.curs_set(0)
    while config.gameHasStarted == False:
      main.logging.error(config.key)
      if(config.Awnser == 1):
        stdscr.addstr(imageloader.images("ui_s1"))
      elif(config.Awnser == 2):
        stdscr.addstr(imageloader.images("ui_s2"))
      elif(config.Awnser == 3):
        stdscr.addstr(imageloader.images("ui_s3"))
      config.prev_key = config.key
      event = stdscr.getch()
      config.key = event if event != -1 else config.prev_key
      if config.key not in [ord('r'),ord('w')]:
        config.key = config.prev_key
      if(config.key == ord('r') and config.Awnser == 1):
          config.gameHasStarted = True
      if(config.key == ord('w')):
          config.Awnser = config.Awnser + 1
          config.key = ord('s')
      if(config.Awnser > 3 or config.Awnser < 0):
          config.Awnser = 1
      stdscr.erase()

    



  
def LoadingGameMap(stdscr):
 for y, line in enumerate(config.map_01):
        for x, c in enumerate(line):
            if c == "0":
              stdscr.move(y,x)
              stdscr.addstr(imageloader.images("map_wall"))
            if c == "1":
              Greyrand = random.randint(236, 239)
              curses.init_pair(2,Greyrand,curses.COLOR_BLACK)
              GREY = curses.color_pair(2)
              il = random.randint(1, 3)
              stdscr.move(y,x)
              if(il == 1):
                stdscr.addstr(imageloader.images("map_empty"),GREY)
              if(il == 2):
                stdscr.addstr(imageloader.images("map_empty01"),GREY)
              if(il == 3):
                stdscr.addstr(imageloader.images("map_empty02"),GREY)
            #The Player is in the array
            if c == "2":
              stdscr.move(y,x)
              containers.SetPlayerPos(x,y)
              stdscr.addstr(imageloader.images("map_player"),curses.color_pair(3))
            if c == "3":
              stdscr.move(y,x)
              entity.Entity['chest']['Xpos'] = x
              entity.Entity['chest']['Ypos'] = y
              if(entity.isContainer == False):
                stdscr.addstr(entity.Entity['chest']['Graphic'],curses.color_pair(4))
              else:
                 stdscr.addstr(entity.Entity['chest']['Graphic'],curses.color_pair(5))
              
        stdscr.addstr("")



def Draw_UI(stdscr):
  stdscr.addstr(imageloader.images("ui_screenbar"))     
  stdscr.addstr(str(config.player_x))
  stdscr.addstr(",")
  stdscr.addstr(str(config.player_y))
  stdscr.addstr(" , ChestPos ")
  stdscr.addstr(str(entity.Entity['chest']['Ypos']))




def Game(stdscr):
    stdscr.nodelay(0)
    containers.PlayerCollisionEntity()
    LoadingGameMap(stdscr)
    Draw_UI(stdscr)
    containers.PlayerMovement(stdscr)
    stdscr.refresh()
    