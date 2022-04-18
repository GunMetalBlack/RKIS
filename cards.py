import random
from unicodedata import name
import imageloader
import cardNames


def CardNameGenerator():
    first_name = cardNames.card_names[random.randint(0, 1000)]
    last_name = cardNames.card_names[random.randint(0, 1000)]
    name = first_name + last_name
    return name


def CardDescGenerator(type):
    card_desc = "This card is a " + str(cardNames.phy_desc[random.randint(0, len(cardNames.phy_desc) - 1)]) + ". It bears a " + str(
        cardNames.color_desc[random.randint(0, len(cardNames.color_desc) - 1)]) + " hue and is a " + type + " type."
    return card_desc
    # This card is (physical descriptor) its bears a (color) and its a (TYPE) type


class CardType:
    def __init__(self, name, def_multiplier, att_multiplier):
        self.name = name
        self.def_multiplier = def_multiplier
        self.att_multiplier = att_multiplier


class Card:
    STEEL_TYPE = CardType("Steel", 4.20, 0.69)
    MAGIE_TYPE = CardType("Magie", 0.42, 6.90)
    GENERIC_TYPE = CardType("Generic", 1, 1)

    def __init__(self, health_points, attack, defense, energy, image, description, name, type):
        self.HP = health_points
        self.DEF = defense
        self.ENG = energy
        self.ATT = attack
        self.IMG = image
        self.DESC = description
        self.NAME = name
        self.TYPE = type

    def __str__(self):
        return "Card:\nName = {}\nHealth = {}\nAttack = {}\nDefense = {}\nEnergy = {}\nDescription = {}".format(self.NAME, self.HP, self.ATT, self.DEF, self.ENG, self.DESC)


class Deck:
    def __init__(self):
        self.cards = []
        self.card_selection = 0

    def start_build(self):
        for i in range(0, 6):
            self.cards.append(Card(
                random.randint(1, 3),
                random.randint(1, 3),
                random.randint(1, 3),
                random.randint(1, 3),
                imageloader.images("blank_card_art"),
                CardDescGenerator(Card.GENERIC_TYPE.name),
                CardNameGenerator(),
                Card.GENERIC_TYPE
            ))

    def select_card(self, card_selection):
        self.card_selection = card_selection

    def get_card(self):
        return self.cards[self.card_selection]

    def dead_card_fill(self):
         self.cards.append(Card(
            0,
            0,
            0,
            0,
            imageloader.images("dead_card"),
            "A CARD TORN TO SHREADS",
            "PLAUGE",
            "Nottype"
        ))

    def build(self, boss_name, boss_desc, hp_min, hp_max, att_min, att_max, def_min, def_max):
        self.cards.append(Card(
            random.randint(hp_min, hp_max),
            random.randint(att_min, att_max),
            random.randint(def_min, def_max),
            69696969696969,
            "noimg",
            boss_desc,
            boss_name,
            "Nottype"
        ))
        # for after you win boss battles or find cards in the wild
