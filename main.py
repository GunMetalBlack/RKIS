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
  stdscr.nodelay(1)
  curses.noecho()
  #init COLORS----------------------------
  curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
  BLUE_BLACK = curses.color_pair(1)
  curses.init_pair(3,158,curses.COLOR_BLACK)
  curses.init_pair(4,209,curses.COLOR_BLACK)
  curses.init_pair(5,209,252)
  curses.init_pair(6,229,curses.COLOR_BLACK)
  #init COLORS----------------------------
  while (config.run == False):
    stdscr.erase()
    stdscr.addstr( imageloader.images("loading"),BLUE_BLACK)
    stdscr.addstr("Press the E Key to begin!")
    stdscr.refresh()
    config.prev_key = config.key
    event = stdscr.getch()
    config.key = event if event != -1 else config.prev_key
    if config.key not in [ord('e')]:
        config.key = config.prev_key
    if(config.key == ord('e')):
      config.run = True
      stdscr.erase()
  while(config.run):
    stdscr.erase()
    DrawScreen(stdscr)
    stdscr.refresh()
    
    
      
 


if (__name__ == '__main__'):
  wrapper(main)