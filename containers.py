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
    if(config.key == ord('s') and config.player_y + engine.RenderDistanceY + 1 < len(config.map_01)):
        config.player_y += speed
    elif(config.key == ord('w') and config.player_y - engine.RenderDistanceY >= 0):
        
     config.player_y -= speed
    elif(config.key == ord('d') and config.player_x + engine.RenderDistanceX + 1 < len(config.map_01[0])):
       config.player_x += speed
    elif(config.key == ord('a') and config.player_x - engine.RenderDistanceX <= 0):
        config.player_x -= speed
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
          
      