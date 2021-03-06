images_dictionary = {}

def images(name):
    return images_dictionary[name]

def images_as_array(name):
    return images(name).splitlines()

def print_string_to_screen(stdscr, string_to_print):
    for line in string_to_print.splitlines():
        stdscr.addnstr(line, stdscr.getmaxyx()[1])
        stdscr.addstr("\n")

def print_image_to_screen(stdscr, image_name):
    print_string_to_screen(stdscr, images(image_name))

images_dictionary["loading"] = '''
 LOADING>>>     

██████╗░██╗░░██╗██╗░██████╗
██╔══██╗██║░██╔╝██║██╔════╝
██████╔╝█████═╝░██║╚█████╗░
██╔══██╗██╔═██╗░██║░╚═══██╗
██║░░██║██║░╚██╗██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░

Welcome to your last and final destination. [The machine sputtered].
[Your eyes burned with 1s and 0s] You found yourself in a world not of your own. 
A deck of cards lay in front of you. 
You gather your things and leave to explore the vast prison beyond. 
Seek out the other trapped players 
CONTROLS:
“W” to cycle through the main menu and “ENTER“ to select an option 
“W,A,S,D” to move around the world.
“I” to view your card deck.
"Y" to start boss battles
"B" to enter shop

Developed Along with the "Nostalgia Engine".
Have Fun :D
PS: There may be some delay in Key Inputs due to Replit
'''

# UI GRAPHICS
images_dictionary["ui_s1"] = '''
   __      __     ___ _                 ___                                                             
  | _|_/\_|_ |   / _ \ | __ _ _   _    / _ \__ _ _ __ ___   ___                                         
  | |\    /| |  / /_)/ |/ _` | | | |  / /_\/ _` | '_ ` _ \ / _ \                                        
  | |/_  _\| | / ___/| | (_| | |_| | / /_\\\\ (_| | | | | | |  __/                                        
  | |  \/  | | \/    |_|\__,_|\__, | \____/\__,_|_| |_| |_|\___|                                        
  |__|    |__|                |___/                                                                     
   __ __     _   _                 _                                                                    
  | _|_ |   /_\ | |__   ___  _   _| |_                                                                  
  | | | |  //_\\\\| '_ \ / _ \| | | | __|                                                                 
  | | | | /  _  \ |_) | (_) | |_| | |_                                                                  
  | | | | \_/ \_/_.__/ \___/ \__,_|\__|                                                                 
  |__|__|                                                                                               
   __ __   __                                   _ _                                             _       
  | _|_ | / _\ ___  ___    /\  /\_____      __ (_) |_  __      ____ _ ___   _ __ ___   __ _  __| | ___  
  | | | | \ \ / _ \/ _ \  / /_/ / _ \ \ /\ / / | | __| \ \ /\ / / _` / __| | '_ ` _ \ / _` |/ _` |/ _ \ 
  | | | | _\ \  __/  __/ / __  / (_) \ V  V /  | | |_   \ V  V / (_| \__ \ | | | | | | (_| | (_| |  __/ 
  | | | | \__/\___|\___| \/ /_/ \___/ \_/\_/   |_|\__|   \_/\_/ \__,_|___/ |_| |_| |_|\__,_|\__,_|\___| 
  |__|__|                                                                                                
  '''

images_dictionary["ui_s2"] = '''
   __ __     ___ _                 ___                                                                   
  | _|_ |   / _ \ | __ _ _   _    / _ \__ _ _ __ ___   ___                                               
  | | | |  / /_)/ |/ _` | | | |  / /_\/ _` | '_ ` _ \ / _ \                                              
  | | | | / ___/| | (_| | |_| | / /_\\\\ (_| | | | | | |  __/                                              
  | | | | \/    |_|\__,_|\__, | \____/\__,_|_| |_| |_|\___|                                              
  |__|__|                |___/                                                                           
   __      __     _   _                 _                                                                
  | _|_/\_|_ |   /_\ | |__   ___  _   _| |_                                                              
  | |\    /| |  //_\\\\| '_ \ / _ \| | | | __|                                                             
  | |/_  _\| | /  _  \ |_) | (_) | |_| | |_                                                              
  | |  \/  | | \_/ \_/_.__/ \___/ \__,_|\__|                                                             
  |__|    |__|                                                                                           
   __ __   __                                   _ _                                             _        
  | _|_ | / _\ ___  ___    /\  /\_____      __ (_) |_  __      ____ _ ___   _ __ ___   __ _  __| | ___   
  | | | | \ \ / _ \/ _ \  / /_/ / _ \ \ /\ / / | | __| \ \ /\ / / _` / __| | '_ ` _ \ / _` |/ _` |/ _ \  
  | | | | _\ \  __/  __/ / __  / (_) \ V  V /  | | |_   \ V  V / (_| \__ \ | | | | | | (_| | (_| |  __/  
  | | | | \__/\___|\___| \/ /_/ \___/ \_/\_/   |_|\__|   \_/\_/ \__,_|___/ |_| |_| |_|\__,_|\__,_|\___|  
  |__|__|                                                                                                
  '''

images_dictionary["ui_s3"] = '''
   __ __     ___ _                 ___                                                                       
  | _|_ |   / _ \ | __ _ _   _    / _ \__ _ _ __ ___   ___                                                   
  | | | |  / /_)/ |/ _` | | | |  / /_\/ _` | '_ ` _ \ / _ \                                                  
  | | | | / ___/| | (_| | |_| | / /_\\\\ (_| | | | | | |  __/                                                  
  | | | | \/    |_|\__,_|\__, | \____/\__,_|_| |_| |_|\___|                                                  
  |__|__|                |___/                                                                               
   __ __     _   _                 _                                                                         
  | _|_ |   /_\ | |__   ___  _   _| |_                                                                       
  | | | |  //_\\\\| '_ \ / _ \| | | | __|                                                                      
  | | | | /  _  \ |_) | (_) | |_| | |_                                                                       
  | | | | \_/ \_/_.__/ \___/ \__,_|\__|                                                                      
  |__|__|                                                                                                    
   __      __   __                                   _ _                                             _       
  | _|_/\_|_ | / _\ ___  ___    /\  /\_____      __ (_) |_  __      ____ _ ___   _ __ ___   __ _  __| | ___  
  | |\    /| | \ \ / _ \/ _ \  / /_/ / _ \ \ /\ / / | | __| \ \ /\ / / _` / __| | '_ ` _ \ / _` |/ _` |/ _ \ 
  | |/_  _\| | _\ \  __/  __/ / __  / (_) \ V  V /  | | |_   \ V  V / (_| \__ \ | | | | | | (_| | (_| |  __/ 
  | |  \/  | | \__/\___|\___| \/ /_/ \___/ \_/\_/   |_|\__|   \_/\_/ \__,_|___/ |_| |_| |_|\__,_|\__,_|\___| 
  |__|    |__|                                                                                                
  '''

images_dictionary["ui_screenbar"] = '''
 _______  _______  _______  _______  _______
/______/\/______/\/______/\/______/\/______/\ 
\__::::\/\__::::\/\__::::\/\__::::\/\__::::\/ 
'''

# MAP GRAPHICS
images_dictionary["map_wall"] = "█"
images_dictionary["map_card_npc"] = "8"
images_dictionary["map_empty"] = "'"
images_dictionary["map_empty01"] = ","
images_dictionary["map_empty02"] = "_"
images_dictionary["map_player"] = "P"
images_dictionary["map_fill"] = " "
images_dictionary["map_grass"] = "@"

images_dictionary["controls"] = '''CONTROLS: 
    “W,A,S,D” to move around the world.
    “I” to view your card deck.
    Once in the card deck screen you can switch cards with "a" and "d"
    Press "y" to enter the mainframe aka(Start a boss battle with cards)
    "B" to enter shop
    Press "H" to toggle help menu
     '''
# ITEM DESC imageFil
images_dictionary["desc_chest"] = '''
                     
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'  ||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-.-'       o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
'''

images_dictionary["blank_card_art"] = '''
┌─────────┐
│         │
│ ┌─────┐ │
│ │     │ │
│ │     │ │
│ └┬───┬┘ │
│  │   │  │
│  ├───┤  │
└──┴───┴──┘
'''

images_dictionary["card_ui_lowermenu_selection_0"] = ''']
  "A key" to cycle left and "D key" to cycle right Press Enter To Select
██████████████████████████████████████████████████████████████████
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░█░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
██████████████████████████████████████████████████████████████████
'''

images_dictionary["card_ui_lowermenu_selection_1"] = '''
  "A key" to cycle left and "D key" to cycle right Press Enter To Select
██████████████████████████████████████████████████████████████████
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░█░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
██████████████████████████████████████████████████████████████████
'''

images_dictionary["card_ui_lowermenu_selection_2"] = '''
  "A key" to cycle left and "D key" to cycle right Press Enter To Select
██████████████████████████████████████████████████████████████████
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░█░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
██████████████████████████████████████████████████████████████████
'''

images_dictionary["card_ui_lowermenu_selection_3"] = '''
  "A key" to cycle left and "D key" to cycle right Press Enter To Select
██████████████████████████████████████████████████████████████████
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░█░░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░█░█░█┼┼┼┼┼┼┼█░░░░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼██░░░██┼┼┼┼┼┼┼█░░░░░█┼
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
██████████████████████████████████████████████████████████████████
'''

images_dictionary["card_ui_lowermenu_selection_4"] = '''
  "A key" to cycle left and "D key" to cycle right Press Enter To Select
██████████████████████████████████████████████████████████████████
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░█░░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░█░█░█┼
┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼┼█░░░░░█┼┼┼┼┼┼┼██░░░██┼
┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼┼███████┼┼┼┼┼┼┼███████┼
██████████████████████████████████████████████████████████████████
'''

images_dictionary["card_ui_DECKLOGO"] = '''
      ___           ___           ___           ___     
     /\  \         /\  \         /\  \         /\__\    
    /::\  \       /::\  \       /::\  \       /:/  /    
   /:/\:\  \     /:/\:\  \     /:/\:\  \     /:/__/     
  /:/  \:\__\   /::\~\:\  \   /:/  \:\  \   /::\__\____ 
 /:/__/ \:|__| /:/\:\ \:\__\ /:/__/ \:\__\ /:/\:::::\__\ 
 \:\  \ /:/  / \:\~\:\ \/__/ \:\  \  \/__/ \/_|:|~~|~   
  \:\  /:/  /   \:\ \:\__\    \:\  \          |:|  |    
   \:\/:/  /     \:\ \/__/     \:\  \         |:|  |    
    \::/__/       \:\__\        \:\__\        |:|  |    
     ~~            \/__/         \/__/         \|__|    
'''

images_dictionary["ui_you_won_0"]='''
 ▄· ▄▌      ▄• ▄▌    ▄▄▌ ▐ ▄▌       ▐ ▄ 
▐█▪██▌▪     █▪██▌    ██· █▌▐█▪     •█▌▐█
▐█▌▐█▪ ▄█▀▄ █▌▐█▌    ██▪▐█▐▐▌ ▄█▀▄ ▐█▐▐▌
 ▐█▀·.▐█▌.▐▌▐█▄█▌    ▐█▌██▐█▌▐█▌.▐▌██▐█▌
  ▀ •  ▀█▄▀▪ ▀▀▀      ▀▀▀▀ ▀▪ ▀█▄▀▪▀▀ █▪
'''


images_dictionary["ui_you_lost_0"] = '''
▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▄▄▄█████▓
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒░ ▓██▓ ░ 
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒  ▒██▒ ░ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░    
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░    ░      
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░           
 ░ ░                                                                 
'''
images_dictionary["ui_card_dead_0"]='''
 ▄· ▄▌      ▄• ▄▌▄▄▄       
▐█▪██▌▪     █▪██▌▀▄ █·     
▐█▌▐█▪ ▄█▀▄ █▌▐█▌▐▀▀▄      
 ▐█▀·.▐█▌.▐▌▐█▄█▌▐█•█▌     
  ▀ •  ▀█▄▀▪ ▀▀▀ .▀  ▀     
 ▄▄·  ▄▄▄· ▄▄▄  ·▄▄▄▄      
▐█ ▌▪▐█ ▀█ ▀▄ █·██▪ ██     
██ ▄▄▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌    
▐███▌▐█ ▪▐▌▐█•█▌██. ██     
·▀▀▀  ▀  ▀ .▀  ▀▀▀▀▀▀•     
·▄▄▄▄  ▪  ▄▄▄ .·▄▄▄▄       
██▪ ██ ██ ▀▄.▀·██▪ ██      
▐█· ▐█▌▐█·▐▀▀▪▄▐█· ▐█▌     
██. ██ ▐█▌▐█▄▄▌██. ██      
▀▀▀▀▀• ▀▀▀ ▀▀▀ ▀▀▀▀▀•    

'''

images_dictionary["shop_ui_logo"] = '''
  _________.__                      
 /   _____/|  |__   ____ ______     
 \_____  \ |  |  \ /  _ \\____ \    
 /        \|   Y  (  <_> )  |_> >   
/_______  /|___|  /\____/|   __/    
        \/      \/       |__|         
  ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/                                    
'''

images_dictionary["dead_card"] = '''
  _____
 /     \\
| () () |
 \  ^  /
  |||||
  |||||


--------
'''


images_dictionary["boss_image_0"] = '''
xkkkkkkOOOOOOkxoc:;;,;:coxO00OOOOOOOOOOO
kkkkkOOOOOOOl'..        ..;lx0000OOOOOOO
kkkOOOOOOOkc.       ...     .lO00000OOOO
kkkOOOOOOx;......''.......    ;k000000OO
kkOOOOOO0l..:llodxxxxxxdolc:;..l0000000O
kOOOOO000o.'lodkOO000000Okkxd;.o00000000
OOOOO0000x,'ldxkO00000000OOxd;'dK0000000
OOOOO0000d'':ldxkO0000000Okdo;,d0000000O
OOOOO0000d,'...',:okOkl:;,',:cok000OOOOO
OOOOOOOO0k::c;,;::lx0kl:::codoxOOOOOOOOO
OOOOOOOOOkc;oxxxxookOkxkkOOOdldOOOOOOOkk
OOOOOOOOOOo,:dxkdcokOxdxO0OxllkOOOOkkkkk
OOkOOkkkkOkc':oxd:;clloxkkxocokOOkkkkkkk
kkkkkkkxoc:'.':lccllloooooo:..,;cldxxkkk
kkxol:,..    ..:llloooodo:,.      ...',:
:,..         ...'codddoc,','            
             .''....;;;;;;           
             .,l;'...'',:c;.            
              'cc;;,',;cl:.             
              .;:::,',ldxo.             
'''

images_dictionary["boss_image_1"] = '''
XXXXXXXXXXOl;'.'',,;;;;;;:cxk0NNXXXXXXXX
XXXXXXXX0o'..........'',,,;::cdKNXXXXXXX
XXXXXXXXx;'.............',;;;;,oKXXXXXXX
XXXXXXX0l'.,:cclc:cccc::cll:,,,l0XXXXXXX
XXXXXXX0c.;odxxxxxxxxdddddo:,',oKXXXXXXX
XXXXXXXKo,lddodddddddoooddoc,.,dXXXXXXXX
XXXXXXXXxlddoolclolcccclolool;;dXXXXXXXX
XXXXXXNXOdoooc::coo::::clloool:xXXXXXXXX
XXXXXXNX0xddoooodkxolloodddoodoOXXXXXXXX
XXXXXXNXKkooooloxkkdolcooollodkKXXXXXXXX
XXXXXXNXKOocc:clccc:cc:::::cld0XXXXXXXXX
XXXXXXNXKKdc:::::;;;;;::::::cx0KXXXXXXXX
XXXXXXNXKK0xc:cc:;;;::c:;;;:oKk:oOXXXXXX
XXXXXXNNKKKKOocccccccc::;;:dKXo..,lxO0KX
XXXXXXNXKKKK0xoc::::::;:ldOX0c......';co
XXXXXXNXKOxo;,dOo::clodk0XXO;...........
XXXXXX0xl;'..,kXx:;lx0XXXNO;............
XXXKkl;......c0kc;,,,l0NN0:.............
Kkl:'........lKx:;;oxOKX0:..............
k,...........oOo::l0NNN0:...............
o...........,kxcccl0NNKc................
c...........:dlllco0WKl.................
'''
images_dictionary["boss_image_2"]='''
MMMMMMMMMMMMXOdolcccccclldOXWMMMMMMMMMMM
MMMMMMMMMMMMXOdolc::::clldOXWMMMMMMMMMMM
MMMMMMMMMMNd,.            .'dXMMMMMMMMMM
MMMMMMMMMXl.  ............  .cXMMMMMMMMM
MMMMMMMMMk.  ..............  .xMMMMMMMMM
MMMMMMMMWd....................oWMMMMMMMM
MMMMMMMMWo....................lNMMMMMMMM
MMMMMMMMWo....................lNMMMMMMMM
MMMMMMMWKc................ ...:0WMMMMMMM
MMMMMMMK:......................;0MMMMMMM
MMMMMMMK:......................;0MMMMMMM
MMMMMMMWd......................oNMMMMMMM
MMMMMMMMKc....................:0MMMMMMMM
MMMMMMMMXo...'................lXMMMMMMMM
MMMMMMWOc......................cONMMMMMM
MMMNKkl'.. .................. ..'ckKNMMM
0koc,.....  ................  .....,:ok0
,'......... ..............    ........',
.......      .............       ......'
.......      ............       .......'
........     ........... ..     .....''.
'''

images_dictionary["explosion_0"] = '''












                                        *'''
images_dictionary["explosion_1"] = '''







                                    ****#****
                                 ***#@##*#@#****
                               *@**@@@*##**#*#**#*
                              **@@*#**#@*#@****#***
                              ****@*@***#****@**@@*
                             *******@***@@***#****#*
                              *#***#*##@****##@@@**
                              **#@###****@*********
                               *****@**@*@*****@**
                                 ************@**
                                    ****#****
                                    '''
images_dictionary["explosion_2"] = '''

                                        *                                       
                               ********* **@******
                           ****   **#**@ #**#*#   ****
                         ***  **  **##** *@@*@*  **  ***
                       **  *  @@   *@*#* ***@*   *#  *  **
                     *** #  *  *#  *@#** ***@*  **  @  * *@*
                    ** *  * ** *@  ****@ @****  ** #* *  * **
                   ** * @* * ** *@  #### *#**  ** ** * @* * **
                  *# * # ** * #* *  **** ****  @ ** * ** * * #*
                 ** * *# * @ * #  @  @*@ *#*  *  @ # # * @* * **
                 *# * * * * # * @* * **# *#* * ** * * * * * # **
                 ** # * * @ * * # * # ** @* * * * * * # @ @ * **
                *# * * * * * * * * # * * * * * * @ @ * * * * * **
                 *# * @ * @ * @ * * * ** *@ * * # * * * * * @ @*
                 *# # @ * * # * *@ * *** @#@ @ ** * @ @ * * # **
                 *# * ** * * * @  @  **@ ***  *  @ * * * @* * #*
                  ** * * ** * #@ *  #*** **##  * #* * #@ * * @*
                   *# * *@ * @@ *#  **** @***  ** ** * #* * #*
                    *# *  * *@ **  @**@* *@#**  ** ** *  * @*
                     *#* @  *  @@  **##* ****@  **  #  * @**
                       **  @  #*   @*@#* @*@*#   @#  *  **
                         *#*  @*  @#*@*# **#*@#  **  ***
                           ****   *##**# #***@*   @***
                               ****@**@* *****@***
'''
images_dictionary["explosion_2"] = '''
              *  -  -  --  --   ------- -------   --  --  -  -  *
             ** -  -  -  --  --   ------ ------   --  --  -  -  - **
            * -- - -- -- --  --   ------ ------   --  -- -- -- - -- *
          ** - -  - -- -- --  --  ------ ------  --  -- -- -- -  - - **
         *  - - -- - -- -  -  --   ----- -----   --  -  - -- - -- - -  *
        ** - - - -- - -- -  -  --  ----- -----  --  -  - -- - -- - - - **
        * - - - -  - - -  - -- --  ----- -----  -- -- -  - - -  - - - - *
       * - - - -  - - - -- - -- --  ---- ----  -- -- - -- - - -  - - - - *
      * -- - - - - - - - -- - -- -  ---- ----  - -- - -- - - - - - - - -- *
      * - - - - - - - -- - - - -  -  --- ---  -  - - - - -- - - - - - - - *
      * - - - - - - - - - - - - -- - --- --- - -- - - - - - - - - - - - - *
      * - - - - - - - - - - - - - - - -- -- - - - - - - - - - - - - - - - *
     * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *
      * - - - - - - - - - - - - - - - -- -- - - - - - - - - - - - - - - - *
      * - - - - - - - - - - - - -- - --- --- - -- - - - - - - - - - - - - *
      * - - - - - - - -- - - - -  -  --- ---  -  - - - - -- - - - - - - - *
      * -- - - - - - - - -- - -- -  ---- ----  - -- - -- - - - - - - - -- *
       * - - - -  - - - -- - -- --  ---- ----  -- -- - -- - - -  - - - - *
        * - - - -  - - -  - -- --  ----- -----  -- -- -  - - -  - - - - *
        ** - - - -- - -- -  -  --  ----- -----  --  -  - -- - -- - - - **
         *  - - -- - -- -  -  --   ----- -----   --  -  - -- - -- - -  *
          ** - -  - -- -- --  --  ------ ------  --  -- -- -- -  - - **
            * -- - -- -- --  --   ------ ------   --  -- -- -- - -- *
             ** -  -  -  --  --   ------ ------   --  --  -  -  - **
'''
images_dictionary["explosion_3"] = '''
                                                                                
                                           @      
                                    #  @ #  # #  
                                    ##    @@ @        
                              @@    @ #     @            
                         #      #   @#      @      @     @ 
                                @      @ @         #         
                        @        @  ####  #            @      
                   #   #      #                @             # 
                       #   @   #  @  @ @  #      @ # #   @      
                  #         #   @      #  #                 #   
                    #     @     #   #    @            # @ @     
                 #                 #             @ @             
                  #   @   @   @           @     #           @ @ 
                  # # @     #    @       @#@ @      @ @     #   
                  #            @  @    @         @       @    # 
                              #@    #      ##    #    #@     @ 
                    #    @   @@  #       @             #    # 
                     #       @     @  @   @#               @ 
                      #  @     @@    ##      @      #    @  
                           @  #    @ @#  @ @ #   @#       
                          #   @   @# @ #   # @#         
                                   ##  # #   @    @   
                                   @  @       @   
'''