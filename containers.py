from re import T
import config
import engine
import entity
import curses
import main
import desc


def SetPlayerPos(x, y):
    config.player_x = x
    config.player_y = y
    return config.player_x, config.player_y


def PlayerCollisionEntity():
    for i in range(-1,2):
        for j in range(-1,2):
            postuple = (i + config.player_x, j + config.player_y)
            if postuple in entity.entities:
                return postuple
    return (-1,-1)

def PlayerMovement(stdscr):
    config.prev_key = config.key
    event = stdscr.getch()
    config.key = event if event != -1 else config.prev_key
    if event != -1:
        config.key = event
    else:
        config.key = ord(']')
    config.frame_count += 1
    config.needFrameUpdate = True
    if(config.prev_key == config.key):
        config.needFrameUpdate = False
        return

    if(config.key == ord('s') and config.map_01[config.player_x][config.player_y + 1] != "0"):
        config.player_y += config.speed
    elif(config.key == ord('w') and config.map_01[config.player_x][config.player_y - 1] != "0"):
        config.player_y -= config.speed
        # Doesn't move the right way and crashes!
    elif(config.key == ord('d') and config.map_01[config.player_x + 1][config.player_y] != "0"):
        config.player_x += config.speed
    elif(config.key == ord('a') and config.map_01[config.player_x - 1][config.player_y] != "0"):
        config.player_x -= config.speed

    elif(config.key == ord('i')):
        config.current_screen = "ui_deck"
    elif(config.key == ord('e')):
        config.current_screen = "boss_attack"
    elif(config.key == ord('b')):
        config.current_screen = "shop_screen"
