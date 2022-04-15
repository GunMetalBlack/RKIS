import curses
import map
import time
run = False
loading = 0
speed = 1
Awnser = 1
gameHasStarted = False
needFrameUpdate = True
key = curses.KEY_RIGHT
prev_key = key
player_x = 350
player_y = 350
cols = 0
player_collision = 0
map_01 = map.map_02
TrueFps = 0
start_time = time.time()
x = 1 # displays the frame rate every 1 second
counter = 0