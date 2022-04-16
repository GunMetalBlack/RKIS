import curses
import map
import time
import cards

cols = 0
current_screen = "splash"
fps_update_rate = 1 # displays the frame rate every 1 second
frame_count = 0
key = 0
loading = 0
main_deck = cards.Deck()
map_01 = map.map_01
needFrameUpdate = True
player_collision = 0
player_x = 350
player_y = 350
prev_key = key
selected_main_menu_option = 1
speed = 1
start_time = time.time()
true_fps = 0