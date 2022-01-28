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
menu = ['Play','About','How its Made']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()
def mainMenu(stdscr):
    curses.curs_set(0)
    # color scheme for selected row
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0
    print_menu(stdscr, current_row)
    if(UserInput("w")):
        current_row = current_row + 1
    if(current_row > 3 or current_row < 0):
        current_row = 1
    print_menu(stdscr, current_row)
    



  
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
    containers.PlayerMovement()
    