
from distutils.command.config import config
import cards
import config
import imageloader


def LoadCardUI(stdscr):
    stdscr.scrollok(1)
    stdscr.move(0,0)
    
    # Should be the screen where the deck is displayer with the name of the card
    config.prev_key = config.key
    event = stdscr.getch()
    config.key = event if event != -1 else config.prev_key
    if event != -1:
        config.key = event
    else:
        config.key = ord(']')
    if(config.card_id_selection > 5):
        config.card_id_selection = 0
    if(config.card_id_selection < 0):
        config.card_id_selection = 5
    if(config.key == ord('a')):
        config.card_id_selection =- 1
        config.key = ord('l')
    elif(config.key == ord('d')):
        config.card_id_selection =+ 1
        config.key = ord('l')
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
    for line in card_ui_as_string.splitlines():
        stdscr.addnstr(line, stdscr.getmaxyx()[1])
        stdscr.addstr("\n")
    for line in imageloader.images_as_array("card_ui_lowermenu_selection_" + str(config.card_id_selection)):
        stdscr.addnstr(line, stdscr.getmaxyx()[1])
        stdscr.addstr("\n")

    stdscr.refresh()
    #stdscr.erase()
