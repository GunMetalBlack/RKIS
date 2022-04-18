import logging
import shop
from numpy import std
import engine
import curses
from curses import wrapper
import imageloader
from replit import audio
import config
import cardUI
import entity
import combat

logging.basicConfig(filename="data.log", level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')


def main(stdscr):
    stdscr.nodelay(True)
    curses.noecho()
    curses.cbreak()
    # init COLORS----------------------------
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    # green wt green bg
    curses.init_pair(13, 48, curses.COLOR_BLACK)
    # red wt green bg
    curses.init_pair(14, 197, curses.COLOR_BLACK)
    # blue wt green bg
    curses.init_pair(15, 19, curses.COLOR_BLACK)
    BLUE_BLACK = curses.color_pair(1)
    curses.init_pair(3, 158, curses.COLOR_BLACK)
    curses.init_pair(4, 209, curses.COLOR_BLACK)
    curses.init_pair(5, 209, 252)
    curses.init_pair(6, 229, curses.COLOR_BLACK)
    # init COLORS----------------------------
    curses.curs_set(0)
    config.main_deck.start_build()
    logging.debug(str(config.main_deck.get_card()))
    stdscr.scrollok(1)
    
    entity.init_entities()
    combat.init_bosses()

    while (True):
        if(config.current_screen == "splash"):
            stdscr.erase()
            stdscr.addstr(imageloader.images("loading"), BLUE_BLACK)
            stdscr.addstr("Press the E Key to begin!")
            stdscr.refresh()
            config.prev_key = config.key
            event = stdscr.getch()
            config.key = event if event != -1 else config.prev_key
            if config.key not in [ord('e')]:
                config.key = config.prev_key
            if(config.key == ord('e')):
                config.current_screen = "main_menu"
                stdscr.erase()
        elif(config.current_screen == "main_menu"):
            engine.mainMenu(stdscr)
        elif(config.current_screen == "ui_deck"):
            cardUI.LoadCardUI(stdscr, True)
        elif(config.current_screen == "explosion_animation"):
            combat.render_explosion_animation(stdscr, config.next_screen)
        elif(config.current_screen == "boss_attack"):
            combat.render_boss_attack(stdscr, config.current_boss_fight)
        elif(config.current_screen == "card_select"):
            combat.render_card_select(stdscr)
        elif(config.current_screen == "shop_screen"):
            shop.display_shop(stdscr)
        else: # current_screen == "open_world"
            engine.Game(stdscr)


if (__name__ == '__main__'):
    wrapper(main)
