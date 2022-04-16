
from distutils.command.config import config
import cards
import config
import imageloader

def LoadCardUI(stdscr):
    card_id_selection = 0
    # Should be the screen where the deck is displayer with the name of the card
    event = stdscr.getch()
    if(event == ord('a')):
        card_id_selection =+ 1 
    elif(event == ord('d')):
        card_id_selection =- 1
    
    FORM_Card_UI = imageloader.images("card_ui_DECKLOGO") + "\n"+ config.main_deck.get_card(card_id_selection).NAME + "\n" + config.main_deck.get_card(card_id_selection).IMG + "\n" + config.main_deck.get_card(card_id_selection).DESC + "\n" + config.main_deck.get_card(card_id_selection).HP + "\n" + config.main_deck.get_card(card_id_selection).DEF + "\n" + config.main_deck.get_card(card_id_selection).ATT + "\n" + config.main_deck.get_card(card_id_selection).ENG   

    if(card_id_selection == 1):
     stdscr.addstr(str(FORM_Card_UI))
     stdscr.addstr(imageloader.images("card_ui_lowermenu_selection_0"))   
    elif(card_id_selection == 2):
     stdscr.addstr(str(FORM_Card_UI))
     stdscr.addstr(imageloader.images("card_ui_lowermenu_selection_1"))   
    elif(card_id_selection == 3):
     stdscr.addstr(str(FORM_Card_UI))
     stdscr.addstr(imageloader.images("card_ui_lowermenu_selection_3"))   
    elif(card_id_selection == 4):
     stdscr.addstr(str(FORM_Card_UI))
     stdscr.addstr(imageloader.images("card_ui_lowermenu_selection_4"))   
    elif(card_id_selection == 5):
     stdscr.addstr(str(FORM_Card_UI))
     stdscr.addstr(imageloader.images("card_ui_lowermenu_selection_5"))   
    elif(card_id_selection > 5):
        card_id_selection = 1

