import random
from unicodedata import name
import imageloader
import cardNames
def CardNameGenerator():
    first_name = cardNames.card_names[random.randint(0,1000)]
    last_name = cardNames.card_names[random.randint(0,1000)]
    name = first_name + last_name
    return name 

def CardDescGenerator():
   card_desc = "This card is a " + str(cardNames.phy_desc[random.randint(0,2639)]) + " it bears a " + str(cardNames.color_desc[0,165]) + "hue" + "and is a" + "GENERIC" + "type."
   return card_desc
    # This card is (physical descriptor) its bears a (color) and its a (TYPE) type

class Card:
    def __init__(self,HP,DEF,ENG,IMG,DESC,NAME):
        self.HP = HP
        self.DEF = DEF
        self.ENG = ENG
        self.IMG = IMG
        self.DESC = DESC
        self.NAME = NAME

class DECK:
    def __init__(self,card_selection):
        self.cards = []
        self.card_selection = card_selection
   
    def StartBuild(self):
        for i in range(0,5): 
            self.cards.append(Card(random.randint(1,3),random.randint(1,3),random.randint(1,3),imageloader.images("blank_card_art"),CardDescGenerator,CardNameGenerator()))

    def GET_CARD(self):
       return self.cards[self.card_selection]

    def Build(self):
        pass
        #for after you win boss battles or find cards in the wild 