import logging
import engine 
import curses
from curses import wrapper
import imageloader
from colorama import init, Fore, Back, Style
import config
from time import sleep


LogFile = "data.log"
logging.basicConfig(filename=LogFile,level = logging.DEBUG,format= Fore.RED +'%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def DrawScreen(stdscr):
  if(config.gameHasStarted == False):
    engine.mainMenu(stdscr)
  else:
    engine.Game(stdscr)
    



def main(stdscr):
  stdscr.erase()
  init(autoreset=True)
  run = True
  stdscr.addstr( imageloader.images("loading"))
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