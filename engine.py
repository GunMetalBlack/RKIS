import config
import imageloader
import curses
import containers
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
    curses.curs_set(2)
    while config.gameHasStarted == False:
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

    



RenderDistanceX = 3
RenderDistanceY = 3

def RenderingGameMap(stdscr):
  # Iterate Over Rendered Region
  for i in range(-RenderDistanceX, RenderDistanceX + 1):
    for j in range(-RenderDistanceY, RenderDistanceY + 1):
      # Calculate Screen/World Space Coordinates
      screen_space_x = i + RenderDistanceX
      screen_space_y = j + RenderDistanceY
      world_space_x = i + config.player_x
      world_space_y = j + config.player_y

      # Lookup Char from World
      char_from_map = config.map_01[world_space_x][world_space_y]
      # If Center of Screen, Replace World Char w/ Player Char
      if i == 0 and j == 0:
        stdscr.move(screen_space_y, screen_space_x)
        stdscr.addstr(imageloader.images("map_player"),curses.color_pair(3))
      
      # Chained 'elif' - Convert from Level Char to Render Char using 'imageloader'
      elif char_from_map == "0":
        stdscr.move(screen_space_y, screen_space_x)
        stdscr.addstr(imageloader.images("map_wall"))
      elif char_from_map == "*":
        stdscr.move(screen_space_y, screen_space_x)
        stdscr.addstr(imageloader.images("map_fill"))
      elif char_from_map == "1":
        Greyrand = random.randint(236, 239)
        curses.init_pair(2,Greyrand,curses.COLOR_BLACK)
        GREY = curses.color_pair(2)
        il = random.randint(1, 3)
        stdscr.move(screen_space_y, screen_space_x)
        if(il == 1):
          stdscr.addstr(imageloader.images("map_empty"),GREY)
        if(il == 2):
          stdscr.addstr(imageloader.images("map_empty01"),GREY)
        if(il == 3):
          stdscr.addstr(imageloader.images("map_empty02"),GREY)
      elif char_from_map == "3":
      #Bad code buggy boi
        entity.Entity['chest']['Xpos'] = screen_space_x
        entity.Entity['chest']['Ypos'] = screen_space_y
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

  stdscr.addstr(17,0,str(entity.CollidedEntityID).capitalize())




def Game(stdscr):
    stdscr.nodelay(0)
    containers.PlayerCollisionEntity()
    RenderingGameMap(stdscr)
    Draw_UI(stdscr)
    containers.PlayerMovement(stdscr)
    stdscr.refresh()
    