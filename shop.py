from email.mime import image
import config
import cards
import imageloader
def display_shop(stdscr): 
    stdscr.scrollok(1)
    stdscr.move(0,0)
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
        elif(config.key == ord('i')):
            config.erase_shop = False
            config.current_screen = "open_world"
            return
        elif(0 < config.shop_points):

            if(config.key == ord('h')):
                #health
                config.shop_points -= 1
                config.main_deck.get_card().HP += 1
            if(config.key == ord('j')):
                #defence
                config.shop_points -= 1
                config.main_deck.get_card().DEF += 1
            if(config.key == ord('k')):
                #attack
                config.shop_points -= 1
                config.main_deck.get_card().ATT += 1
            if(config.key == ord('l')):
                #energy
                config.shop_points -= 1
                config.main_deck.get_card().ENG += 1
                
    config.main_deck.select_card(config.card_id_selection)

    if(config.card_id_selection > 4):
        config.card_id_selection = 0
    if(config.card_id_selection < 0):
        config.card_id_selection = 4
   
   
   
    card_ui_as_string = "{}\n{}\nHealth:{} Defense:{} Attack:{} Energy:{}\n".format(
    imageloader.images("shop_ui_logo"),
    config.main_deck.get_card().NAME,
    str(config.main_deck.get_card().HP),
    str(config.main_deck.get_card().DEF),
    str(config.main_deck.get_card().ATT),
    str(config.main_deck.get_card().ENG)
    )

    

        # Print Graphics Line-By-Line to Prevent Out-Of-Bounds Errors
    imageloader.print_string_to_screen(stdscr, card_ui_as_string)
    imageloader.print_string_to_screen(stdscr,'''PRESS I TO EXIT''')
    imageloader.print_string_to_screen(stdscr,"\nYour remaining points to spend is " + str(config.shop_points))

    imageloader.print_string_to_screen(stdscr,'''
    PICK 'H' to upgrade Health or
    PICK 'J' to upgrade DEFENSE or
    PICK 'K' to upgrade ATTACK or
    PICK 'L' to upgrade ENERGY''')
    imageloader.print_image_to_screen(stdscr, "card_ui_lowermenu_selection_" + str(config.card_id_selection))

    stdscr.refresh()

