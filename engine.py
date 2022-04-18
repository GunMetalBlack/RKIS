import config
import imageloader
import curses
import containers
import main
import random
import entity
import time
import desc


def UserInput(stdscr, keys):

    readKey = stdscr.getch()
    if(readKey == ord(keys)):
        keyisPressed = True
    else:
        keyisPressed = False
    return keyisPressed


def mainMenu(stdscr):
    if(config.selected_main_menu_option == 1):
        stdscr.addstr(imageloader.images("ui_s1"))
    elif(config.selected_main_menu_option == 2):
        stdscr.addstr(imageloader.images("ui_s2"))
    elif(config.selected_main_menu_option == 3):
        stdscr.addstr(imageloader.images("ui_s3"))
    config.prev_key = config.key
    event = stdscr.getch()
    config.key = event if event != -1 else config.prev_key
    if config.key not in [ord('\n'), ord('w')]:
        config.key = config.prev_key
    if(config.key == ord('\n') and config.selected_main_menu_option == 1):
        config.current_screen = "open_world"
    if(config.key == ord('w')):
        config.selected_main_menu_option = config.selected_main_menu_option + 1
        config.key = 0
    if(config.key == ord('s')):
        config.selected_main_menu_option = config.selected_main_menu_option - 1
        config.key = 0
    if(config.selected_main_menu_option > 3 or config.selected_main_menu_option < 0):
        config.selected_main_menu_option = 1
    stdscr.erase()


RenderDistanceX = 30
RenderDistanceY = 8


def RenderingGameMap(stdscr):
    # Iterate Over Rendered Region
    for i in range(-RenderDistanceX, RenderDistanceX + 1):
        for j in range(-RenderDistanceY, RenderDistanceY + 1):
            # Calculate Screen/World Space Coordinates
            screen_space_x = i + RenderDistanceX
            screen_space_y = j + RenderDistanceY
            world_space_x = i + config.player_x
            world_space_y = j + config.player_y
            global screen_space_offset
            screen_space_offset = int((config.cols - RenderDistanceX)/2)
            # Lookup Char from World
            char_from_map = config.map_01[world_space_x][world_space_y]
            # If Center of Screen, Replace World Char w/ Player Char
            if i == 0 and j == 0:
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                stdscr.addstr(imageloader.images(
                    "map_player"), curses.color_pair(3))

            # Chained 'elif' - Convert from Level Char to Render Char using 'imageloader'
            elif char_from_map == "0":
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                stdscr.addstr(imageloader.images("map_wall"))
            elif char_from_map == "9":
                curses.init_pair(44,201, curses.COLOR_WHITE)
                curses.init_pair(45,201, 0)
                Purple_WHITE = curses.color_pair(44)
                Purple_BLACK = curses.color_pair(45)
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                pos_of_entity_collided_with = containers.PlayerCollisionEntity()
                if pos_of_entity_collided_with != (-1,-1):
                     stdscr.addstr(imageloader.images("map_card_npc"),Purple_WHITE)
                else:
                    stdscr.addstr(imageloader.images("map_card_npc"),Purple_BLACK)
            elif char_from_map == "*":
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                stdscr.addstr(imageloader.images("map_fill"))
            elif char_from_map == "6":
                grass_colors = [curses.color_pair(14), curses.color_pair(15), curses.color_pair(13)]
                grass_chars = ['@','X']
                grass_color_index = hash(str(world_space_x)+str(world_space_y)) % 30
                if(grass_color_index > len(grass_colors) - 1): grass_color_index = len(grass_colors) - 1
                grass_char_index = hash(str(world_space_x)+str(world_space_y)+"filler") % 3
                if(grass_char_index > len(grass_chars) - 1): grass_char_index = len(grass_chars) - 1
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                stdscr.addstr(grass_chars[grass_char_index], grass_colors[grass_color_index])
            elif char_from_map == "1":
                Greyrand = random.randint(236, 239)
                curses.init_pair(2, Greyrand, curses.COLOR_BLACK)
                GREY = curses.color_pair(2)
                il = hash(str(world_space_x)+str(world_space_y)) % 3
                stdscr.move(screen_space_y, screen_space_x +
                            screen_space_offset)
                if(il == 0):
                    stdscr.addstr(imageloader.images("map_empty"), GREY)
                if(il == 1):
                    stdscr.addstr(imageloader.images("map_empty01"), GREY)
                if(il == 2):
                    stdscr.addstr(imageloader.images("map_empty02"), GREY)

    stdscr.addstr("")


def Draw_UI(stdscr):
    stdscr.move(20, 5 + screen_space_offset)

    pos_of_entity_collided_with = containers.PlayerCollisionEntity()
    if pos_of_entity_collided_with != (-1,-1):
        entity_collided_with = entity.entities[pos_of_entity_collided_with]
        entity_description = desc.descriptions[entity_collided_with.desc_name]
        imageloader.print_string_to_screen(stdscr, entity_description)
        return
    if(config.help_text == True):
        stdscr.addstr(desc.descriptions["help_desc"])
    else:
        imageloader.print_image_to_screen(stdscr, "ui_screenbar")
        imageloader.print_string_to_screen(stdscr, "\n" + str(config.player_x) + "," + str(config.player_y) + "\n")
        imageloader.print_image_to_screen(stdscr, "controls")
        imageloader.print_string_to_screen(stdscr, "\nFPS: " + str(config.true_fps))


def Game(stdscr):
    stdscr.nodelay(True)
    curses.noecho()
    curses.cbreak()
    config.cols = stdscr.getmaxyx()[1]
    containers.PlayerMovement(stdscr)
    if config.needFrameUpdate:
        stdscr.erase()
        RenderingGameMap(stdscr)
        Draw_UI(stdscr)
    if (time.time() - config.start_time) > config.fps_update_rate :
        config.true_fps = config.frame_count / (time.time() - config.start_time)
        config.frame_count = 0
        config.start_time = time.time()
    if(config.erase_shop == True):
        stdscr.erase()

        # stdscr.refresh()
