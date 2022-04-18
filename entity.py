entities = {}

class Entity:
    def __init__(self, pos_x, pos_y, desc_name,npc_name):
        entities[(pos_x, pos_y)] = self
        self.desc_name = desc_name
        self.npc_name = npc_name

def init_entities():
    Entity(349, 343, "card_npc_01", "Unknown")
    Entity(249, 271, "card_npc_02", "Coal Miner")
    Entity(601, 79, "card_npc_03", "The Thief that Stole the Smoke")
    Entity(249, 271, "card_npc_04", "Bob")
    Entity(249, 271, "card_npc_05", "Jim")
