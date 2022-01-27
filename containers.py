import config
import engine
import entity
import main
def SetPlayerPos(x,y):
    config.player_x = x
    config.player_y = y
    return config.player_x,config.player_y


def PlayerCollisionEntity():
  for i in range(len(entity.Entity)):
    
    if config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 1 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == 0 or config.player_x - entity.Entity[entity.EntityID[i]]['Xpos'] == -1:
    
       main.logging.debug(entity.Entity[entity.EntityID[i]]["Name"])


def PlayerMovement():
    speed = 1
    if(engine.UserInput("d") and config.player_x < 18 ):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(engine.UserInput("a") and 1 < config.player_x ):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x + -speed] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y,Playerx)
    elif(engine.UserInput("s") and config.player_y < 11):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y + 1,Playerx)
    elif(engine.UserInput("w") and 1 < config.player_y):
        
        Playery = str(config.map_01[config.player_y])
        temp = list(Playery)
        temp[config.player_x] = "1"
        temp[config.player_x] = "2"
        Playerx = "".join(temp)
        del config.map_01[config.player_y]
        config.map_01.insert(config.player_y - 1,Playerx)
    else:
      pass