import config
import engine
import entity
import main


def SetPlayerPos(x,y):
    config.player_x = x
    config.player_y = y
    return config.player_x,config.player_y


def PlayerCollisionEntity():
  entity.isContainer = False
  for i in range(len(entity.Entity)):
    if(config.player_y - entity.Entity[entity.EntityID[i]]['Ypos'] == 1 or config.player_y - entity.Entity[entity.EntityID[i]]['Ypos'] == -1):

      if config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 1 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 0 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == -1:
        if(entity.Entity[entity.EntityID[i]]['Type'] == 'container'):  
           entity.isContainer = True
        
          

def PlayerMovement(stdscr):
    speed = 1
    key = stdscr.getch()
    if(key == ord('d') and config.player_x < 18 ):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(key == ord('a') and 1 < config.player_x ):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + -speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(key == ord('s') and config.player_y < 11):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y + 1,Playerx)
    elif(key == ord('w') and 1 < config.player_y):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y - 1,Playerx)
    else:
      pass