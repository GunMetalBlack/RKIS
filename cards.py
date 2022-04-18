import random
from unicodedata import name
import imageloader
import cardNames
import logging

def CardNameGenerator():
    first_name = cardNames.card_names[random.randint(0, 1000)]
    last_name = cardNames.card_names[random.randint(0, 1000)]
    name = first_name.capitalize() + " " + last_name.capitalize()
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
    DEAD_TYPE = CardType("Dead", 0, 0)

    def __init__(self, health_points: int, attack: int, defense: int, energy: int, image: str, description: str, name: str, type: CardType):
        self.HP = health_points
        self.DEF = defense
        self.ENG = energy
        self.ATT = attack
        self.IMG = image
        self.DESC = description
        self.NAME = name
        self.TYPE = type

    def get_copy(self):
        return Card(
            self.HP,
            self.DEF,
            self.ENG,
            self.ATT,
            self.IMG,
            self.DESC,
            self.NAME,
            self.TYPE
        )

    def __str__(self):
        return "Name = {}\nHealth = {}\nAttack = {}\nDefense = {}\nEnergy = {}".format(self.NAME, self.HP, self.ATT, self.DEF, self.ENG)


class Deck:
    def __init__(self):
        self.cards = []
        self.card_selection = 0

    def get_copy(self):
        copy_of_self = Deck()
        copy_of_self.card_selection = self.card_selection
        for original_card in self.cards:
            copy_of_self.cards.append(original_card.get_copy())
        return copy_of_self

    def start_build(self):
        for i in range(0, 5):
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
        if card_selection < 0 or card_selection > len(self.cards) - 1:
            return
        if self.cards[card_selection].TYPE.name == "Dead":
            return
        self.card_selection = card_selection

    def get_card(self):
        return self.cards[self.card_selection]

    def kill_current_card(self):
        self.cards[self.card_selection] = Card(
            0,
            0,
            0,
            0,
            imageloader.images("dead_card"),
            "A CARD TORN TO SHREADS",
            "PLAUGE",
            Card.DEAD_TYPE
        )
        self.select_card(self.get_next_living_card())

    def get_next_living_card(self) -> int:
        for i in range(0, len(self.cards)):
            card_in_deck = self.cards[i]
            if card_in_deck.TYPE.name != Card.DEAD_TYPE.name:
                return i
        return -1  # No Living Cards

    def build_boss_deck(self, boss_name, boss_desc, hp_min, hp_max, att_min, att_max, def_min, def_max):
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
