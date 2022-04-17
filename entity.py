entities = {}

class Entity:
    def __init__(self, pos_x, pos_y, desc_name,npc_name):
        entities[(pos_x, pos_y)] = self
        self.desc_name = desc_name
        self.npc_name = npc_name
    