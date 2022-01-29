import main
from colorama import init, Fore, Back, Style

imageNames = []
imageFile =[]

def images(name):
    if name in (imageNames):
      fileIndex = imageNames.index(name)
    else:
      main.logging.error("NO IMAGE")
    return imageFile[fileIndex]







imageFile.append('''
 LOADING>>>     


██████╗░██╗░░██╗██╗░██████╗
██╔══██╗██║░██╔╝██║██╔════╝
██████╔╝█████═╝░██║╚█████╗░
██╔══██╗██╔═██╗░██║░╚═══██╗
██║░░██║██║░╚██╗██║██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░

Developed Along with the "Nostalgia Engine".

Thanks for playing! 
This is a adventure ascii game,
it was made without the use of a graphics library.

To navigate through the main menu press the
"W" key twice, to enter a menu press the "r" key.

Have Fun :D
PS: There may be some delay in Key Inputs due to Replit
Being slow.
''')

imageNames.append("loading")





#UI GRAPHICS
imageFile.append('''
  [*] Play Game

  [] About
  
  [] See How it was made  
  ''')
imageNames.append("ui_s1")


imageFile.append('''
  [] Play Game

  [*] About
  
  [] See How it was made  
  ''')
imageNames.append("ui_s2")


imageFile.append('''
  [] Play Game

  [] About
  
  [*] See How it was made  
  ''')
imageNames.append("ui_s3")


imageFile.append('''
 _______  _______  _______  _______  _______  
/______/\/______/\/______/\/______/\/______/\ 
\__::::\/\__::::\/\__::::\/\__::::\/\__::::\/ 
''')

imageNames.append("ui_screenbar")



# MAP GRAPHICS
imageFile.append("█")
imageNames.append("map_wall")

imageFile.append(":")
imageNames.append("map_empty")

imageFile.append("P")
imageNames.append("map_player")

#ITEM DESC imageFil
imageFile.append('''
                     
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
               ||=[ '-._.-.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

imageNames.append("desc_chest")







