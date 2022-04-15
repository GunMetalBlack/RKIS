import random
from unicodedata import name
import imageloader
import cardNames
def CardNameGenerator():
    first_name = cardNames.card_names[random.randint(0,1000)]
    last_name = cardNames.card_names[random.randint(0,1000)]
    name = first_name + last_name
    return name 

class Card:
    def __init__(self,HP,DEF,ENG,IMG,DESC,NAME):
        self.HP = HP
        self.DEF = DEF
        self.ENG = ENG
        self.IMG = IMG
        self.DESC = DESC
        self.NAME = NAME
    def Display(self):
        #display Card Description and image
        pass

class DECK:
    def __init__(self):
        self.cards = []
   
    def StartBuild(self):
        self.cards.append(Card(random.randint(1,3),random.randint(1,3),random.randint(1,3),imageloader.images("blank_card_art"),,CardNameGenerator()))

    def Build(self):
        pass
        #for after you win boss battles or find cards in the wild 