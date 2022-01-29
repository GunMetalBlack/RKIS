import logging
import engine 
import curses
from curses import wrapper
import imageloader
from replit import audio
import config



LogFile = "data.log"
logging.basicConfig(filename=LogFile,level = logging.DEBUG,format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def DrawScreen(stdscr):
  if(config.gameHasStarted == False):
    engine.mainMenu(stdscr)
  else:
    stdscr.erase()
    engine.Game(stdscr)
    


def main(stdscr):
  curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
  BLUE_BLACK = curses.color_pair(1)
  stdscr.erase()
  run = True
  stdscr.addstr( imageloader.images("loading"),BLUE_BLACK)
  stdscr.refresh()
  stdscr.addstr("Press enter twice to continue!")
  stdscr.getkey()
  stdscr.erase()
  while(run):
    stdscr.erase()
    DrawScreen(stdscr)
    stdscr.refresh()
    
    
      
 


if (__name__ == '__main__'):
  wrapper(main)