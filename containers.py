import config
import engine
import entity
import main
import curses


def SetPlayerPos(x,y):
    config.player_x = x
    config.player_y = y
    return config.player_x,config.player_y


def PlayerCollisionEntity():
  entity.isContainer = False
  entity.CollidedEntityID = ''
  for i in range(len(entity.Entity)):
    if(config.player_y - entity.Entity[entity.EntityID[i]]['Ypos'] == 1 or config.player_y - entity.Entity[entity.EntityID[i]]['Ypos'] == -1):

      if config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 1 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 0 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == -1:
        if(entity.Entity[entity.EntityID[i]]['Type'] == 'container'):  
           entity.isContainer = True
           entity.CollidedEntityID = entity.EntityID[i]
           
        
          

def PlayerMovement(stdscr):
    config.prev_key = config.key
    event = stdscr.getch()
    config.key = event if event != -1 else config.prev_key
    if config.key not in [ord('w'),ord('a'),ord('s'),ord('d'),ord('i')]:
        config.key = ord('p')
    speed = 1
    if(config.key == ord('d') and config.player_x < len(config.map_01[config.player_y]) - 2):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(config.key == ord('a') and 1 < config.player_x ):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + -speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(config.key == ord('s') and config.player_y < len(config.map_01)-2):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y + 1,Playerx)
    elif(config.key == ord('w') and 1 < config.player_y):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y - 1,Playerx)
    elif(config.key == ord('i') and entity.isContainer == True):
      if(entity.CollidedEntityID != ''):
          stdscr.erase()
          stdscr.addstr("DESCRIPTION: ",curses.color_pair(6))
          stdscr.addstr(entity.Entity[entity.CollidedEntityID]['Desc'],curses.color_pair(6))
          stdscr.addstr('''
          
          ''')
          stdscr.addstr(entity.Entity[entity.CollidedEntityID]['DescImage'],curses.color_pair(6))
          stdscr.addstr("Press Any Key To Exit!",curses.color_pair(6))
          stdscr.refresh()
          stdscr.getkey()
          
      