import logging
import engine 
import imageloader
from colorama import init, Fore, Back, Style
import config
import replit
from time import sleep
replit.clear()

LogFile = "data.log"
logging.basicConfig(filename=LogFile,level = logging.DEBUG,format= Fore.RED +'%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def DrawScreen():
  if(config.gameHasStarted == False):
    engine.mainMenu()
  else:
    engine.Game()
    sleep(config.FPS)



def main():
  init(autoreset=True)
  run = True
  print(Fore.CYAN +Back.BLACK+ imageloader.images("loading"))
  input(Fore.CYAN +Back.BLACK+"Press enter twice to continue!")
  while(run):
    replit.clear()
    DrawScreen()
    
    
      
 


if (__name__ == '__main__'):
  main()