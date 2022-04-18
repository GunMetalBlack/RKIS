
from distutils.command.config import config
import cards
import config
import curses
import imageloader


def LoadCardUI(stdscr, is_not_battle:bool):
    stdscr.scrollok(1)
    stdscr.move(0,0)
    
    # Should be the screen where the deck is displayer with the name of the card
    config.prev_key = config.key
    event = stdscr.getch()
    if(event != -1):
        config.key = event
    else:
        config.key = ord(']')
    
    if(config.key != config.prev_key):
        if(config.key == ord('a')):
            config.card_id_selection -= 1
        elif(config.key == ord('d')):
            config.card_id_selection += 1
        elif(config.key == ord('i') and is_not_battle):
            config.current_screen = "open_world"
            return
        elif(config.key == ord('\n') and not is_not_battle):
            config.next_screen = "boss_attack"
            config.current_screen = "explosion_animation"
            return

        if(config.card_id_selection > 4):
            config.card_id_selection = 0
        if(config.card_id_selection < 0):
            config.card_id_selection = 4
        config.main_deck.select_card(config.card_id_selection)
    
    card_ui_as_string = "{}\n{}\n{}\n{}\nHealth:{} Defense:{} Attack:{} Energy:{}\n".format(
        imageloader.images("card_ui_DECKLOGO"),
        config.main_deck.get_card().NAME,
        config.main_deck.get_card().IMG,
        config.main_deck.get_card().DESC,
        str(config.main_deck.get_card().HP),
        str(config.main_deck.get_card().DEF),
        str(config.main_deck.get_card().ATT),
        str(config.main_deck.get_card().ENG)
    )

    # Print Graphics Line-By-Line to Prevent Out-Of-Bounds Errors
    imageloader.print_string_to_screen(stdscr, card_ui_as_string)
    imageloader.print_image_to_screen(stdscr, "card_ui_lowermenu_selection_" + str(config.card_id_selection))

    stdscr.refresh()
    #stdscr.erase()
