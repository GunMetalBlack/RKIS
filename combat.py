import cards
import cardUI
import config
import desc
import imageloader
import time

bosses = {}

class Boss:
    def __init__(self, boss_graphic_key, boss_desc_key, boss_name, min_max_hp, min_max_att, min_max_def):
        self.boss_graphic_key = boss_graphic_key
        self.boss_desc_key = boss_desc_key
        self.boss_name = boss_name
        self.min_max_hp = min_max_hp
        self.min_max_def = min_max_def
        self.min_max_att = min_max_att 
        self.deck = cards.Deck()
        self.deck.build(
            self.boss_name,
            desc.descriptions[self.boss_desc_key],
            self.min_max_hp[0], self.min_max_hp[1],
            self.min_max_att[0], self.min_max_att[1],
            self.min_max_def[0], self.min_max_def[1],
            )
    def __str__(self):
        return str(self.deck.get_card())

class BossFight:
    def __init__(self, boss:Boss):
        self.boss = boss
        self.player_card_index = 0

def init_bosses():
    bosses[0] = Boss("boss_image_0", "boss_desc_0", "Len Bhapiro", (10,15), (15, 20), (3,6))
    bosses[1] = Boss("boss_image_1", "boss_desc_1", "Paywall", (20,25), (20, 25), (6,9))
    bosses[2] = Boss("boss_image_2", "boss_desc_2", "Senator Armstrong", (420420420420420, 420420420420420), (30, 50), (69,420))
    config.current_boss_fight = BossFight(bosses[config.current_boss])

def render_explosion_animation(stdscr, next_screen:str):
    stdscr.erase()
    stdscr.move(0,0)
    animation_phase = (config.current_animation_frame % 5) - 1
    imageloader.print_image_to_screen(stdscr, "explosion_" + str(animation_phase))
    config.current_animation_frame += 1
    if(config.current_animation_frame % 5 == 0):
        config.current_animation_frame += 1
        config.current_screen = next_screen
    stdscr.refresh()
    time.sleep(0.5)
    return

def render_boss_attack(stdscr, boss_fight:BossFight):
    stdscr.erase()
    imageloader.print_image_to_screen(stdscr, boss_fight.boss.boss_graphic_key)
    imageloader.print_string_to_screen(stdscr, desc.descriptions[boss_fight.boss.boss_desc_key])
    imageloader.print_string_to_screen(stdscr, str(boss_fight.boss))
    imageloader.print_string_to_screen(stdscr, str(config.main_deck.get_card()))
    stdscr.refresh()
    time.sleep(1)
    config.next_screen = "card_select"
    config.current_screen = "explosion_animation"
    return

def render_card_select(stdscr):
    cardUI.LoadCardUI(stdscr, False)

# Explosion Animation Stage
# Boss Attack Stage
# Explosion Animation Stage
# Card Select Stage
# Loop