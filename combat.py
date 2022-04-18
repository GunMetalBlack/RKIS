import cards
import cardUI
import config
import desc
import imageloader
import main
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
        self.deck.build_boss_deck(
            self.boss_name,
            desc.descriptions[self.boss_desc_key],
            self.min_max_hp[0], self.min_max_hp[1],
            self.min_max_att[0], self.min_max_att[1],
            self.min_max_def[0], self.min_max_def[1],
        )
    
    def get_copy(self):
        return Boss(
            self.boss_graphic_key,
            self.boss_desc_key,
            self.boss_name,
            self.min_max_hp,
            self.min_max_def,
            self.min_max_att
        )

    def __str__(self):
        return str(self.deck.get_card())


class BossFight:
    def __init__(self, boss: Boss, player_deck: cards.Deck):
        self.boss = boss
        self.player_deck = player_deck
        self.player_card_index = 0
        self.turn = "boss"
    
    def get_attack_or_defense_text(self):
        if self.turn == "boss":
            return "ATTACKING"
        else:
            return "DEFENDING"
    
    def do_turn(self) -> tuple[str, str]:
        attacking_card: cards.Card
        defending_card: cards.Card
        if self.turn == "boss":
            attacking_card = self.boss.deck.get_card()
            defending_card = self.player_deck.get_card()
        else:
            attacking_card = self.player_deck.get_card()
            defending_card = self.boss.deck.get_card()
        # Do Damage
        if defending_card.DEF >= attacking_card.ATT:
            defending_card.HP -= 1
        else:
            defending_card.HP -= attacking_card.ATT - defending_card.DEF
        # Check If Dead
        if defending_card.HP <= 0:
            if self.turn == "boss":
                self.player_deck.kill_current_card()
                if self.player_deck.get_next_living_card() == -1:
                    return "open_world", "ui_you_lost"
                else:
                    config.shop_points += 1
                    self.turn = "player"
                    return "card_select", "ui_card_dead"
            else:
                config.shop_points += 5
                config.current_boss += 1
                return "open_world", "ui_you_won"
        if self.turn == "boss":
            self.turn = "player"
        else:
            self.turn = "boss"
        return "card_select", "explosion_animation"


def init_bosses():
    bosses[0] = Boss("boss_image_0", "boss_desc_0",
                     "Len Bhapiro", (10, 15), (15, 20), (3, 6))
    bosses[1] = Boss("boss_image_1", "boss_desc_1",
                     "Paywall", (20, 25), (20, 25), (6, 9))
    bosses[2] = Boss("boss_image_2", "boss_desc_2", "Senator Armstrong",
                     (420420420420420, 420420420420420), (30, 50), (69, 420))


def render_text_animation(stdscr, next_screen: str, num_frames: int, image_name_base: str):
    stdscr.erase()
    stdscr.move(0, 0)
    if(config.current_animation_frame % (num_frames + 1) == 0):
        config.current_animation_frame += 1
        config.current_screen = next_screen
    animation_phase = (config.current_animation_frame % (num_frames + 1)) - 1
    imageloader.print_image_to_screen(
        stdscr, image_name_base + str(animation_phase))
    config.current_animation_frame += 1
    stdscr.refresh()
    time.sleep(0.5)
    return


def render_boss_attack(stdscr, boss_fight: BossFight):
    stdscr.erase()
    imageloader.print_image_to_screen(stdscr, boss_fight.boss.boss_graphic_key)
    imageloader.print_string_to_screen(
        stdscr, desc.descriptions[boss_fight.boss.boss_desc_key])
    imageloader.print_string_to_screen(stdscr, "\nBoss' Card (" + boss_fight.get_attack_or_defense_text() + "):")
    imageloader.print_string_to_screen(stdscr, str(boss_fight.boss))
    imageloader.print_string_to_screen(stdscr, "\nYour Card:")
    imageloader.print_string_to_screen(
        stdscr, str(config.main_deck.get_card()))
    imageloader.print_string_to_screen(stdscr, "\nPress Enter to Continue....")
    stdscr.refresh()
    
    while(True):
        while(True):
            config.prev_key = config.key
            event = stdscr.getch()
            if event != -1:
                config.key = event
                break
            else:
                config.key = ']'

        if(config.key != config.prev_key):
            if(config.key == ord('\n')):
                config.next_screen, config.current_screen = boss_fight.do_turn()
                return

def render_card_select(stdscr):
    cardUI.LoadCardUI(stdscr, False)

# Explosion Animation Stage
# Boss Attack Stage
# Explosion Animation Stage
# Card Select Stage
# Loop
