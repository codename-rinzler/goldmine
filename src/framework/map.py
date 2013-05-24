import libtcodpy as libtcod
from rect import Rect
from tile import Tile
from framework.components.position_component import PositionComponent

class Map:
    def __init__(self, width, height, messenger, player):
        self.map = []
        self.gameitems = []
        self.messenger = messenger
        self.player = player
        
        self.reinitialise(width, height)
        

    # setting self.w and self.h here so that we can call this to regen
    # worlds of different sizes without reinit'ing the class
    def reinitialise(self, width, height):
        self.width = width
        self.height = height

        self.map = [[ Tile(True)
                  for y in range(self.height) ]
                    for x in range(self.width) ]


    def make_map(self, max_rooms = 30, room_min_size = 6, room_max_size = 10):
        self.reinitialise(self.width, self.height)
        
        rooms = []
        num_rooms = 0

        for r in range(max_rooms):
            w = libtcod.random_get_int(0, room_min_size, room_max_size)
            h = libtcod.random_get_int(0, room_min_size, room_max_size)
            x = libtcod.random_get_int(0, 0, self.width - w - 1)
            y = libtcod.random_get_int(0, 0, self.height - h - 1)

            new_room = Rect(x, y, w, h)
            failed = False
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break

            if not failed:
                self.create_room(new_room)
                #self.place_objects(new_room)
                #self.place_items(new_room)
 
                (new_x, new_y) = new_room.center()
 
                if num_rooms == 0:
                    self.player.add_component(PositionComponent(new_x, new_y))

                else:
                    (prev_x, prev_y) = rooms[num_rooms-1].center()
 
                    if libtcod.random_get_int(0, 0, 1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
 
                rooms.append(new_room)
                num_rooms += 1
        
    def create_room(self, room):

        for x in range(room.x1, room.x2+1):
            for y in range(room.y1, room.y2+1):
                self.map[x][y].blocked = False
                self.map[x][y].block_sight = False
 
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False

    def create_v_tunnel(self, y1, y2, x):

        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False

    def place_items(self, room, max_room_items = 2):
        num_items = libtcod.random_get_int(0, 0, max_room_items)

        for i in range(num_items):
            x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
            y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)

            if not self.is_blocked(x, y):
                dice = libtcod.random_get_int(0, 0, 100)
                if dice < 70:
                    heal = HealingComponent(5)
                    inv_item = InventoryItem(self.player, use_component = heal)
                    item = GameItem(x, y, '!', 'healing potion', libtcod.violet, self.messenger, self, inventory_item=inv_item)
                else:
                    lightning = LightningBoltComponent()
                    inv_item = InventoryItem(self.player, use_component = lightning)
                    item = GameItem(x, y, '#', 'scroll of lightning bolt', libtcod.light_yellow, self.messenger, self, inventory_item=inv_item)

                self.gameitems.append(item)
                item.send_to_back(self.gameitems)

    def place_objects(self, room, max_room_monsters = 3):
        num_monsters = libtcod.random_get_int(0, 0, max_room_monsters)
 
        for i in range(num_monsters):
            x = libtcod.random_get_int(0, room.x1+1, room.x2-1)
            y = libtcod.random_get_int(0, room.y1+1, room.y2-1)
 
            monster_death = MonsterDeathComponent(self.gameitems)

            if not self.is_blocked(x, y):
                if libtcod.random_get_int(0, 0, 100) < 80:  #80% chance of getting an orc
                    fighter_component = Fighter(hp=10, defense=0, power=3, death = monster_death)
                    ai_component = BasicMonster()
 
                    monster = GameItem(x, y, 'o', 'orc', libtcod.desaturated_green, self.messenger, self,
                                       blocks=True, fighter=fighter_component, ai=ai_component)
                else:
                    fighter_component = Fighter(hp=16, defense=1, power=4, death = monster_death)
                    ai_component = BasicMonster()
 
                    monster = GameItem(x, y, 'T', 'troll', libtcod.darker_green, self.messenger, self,
                                       blocks=True, fighter=fighter_component, ai=ai_component)
 
                self.gameitems.append(monster)

    def is_blocked(self, x, y):
        if self.map[x][y].blocked:
            return True
 
        for item in self.gameitems:
            if item.blocks and item.x == x and item.y == y:
                return True
 
        return False

    def nearest_monster(self, max_range = 5):
        closest_enemy = None
        closest_dist = max_range + 1  #start with (slightly more than) maximum range
 
        for item in self.gameitems:
            if item.fighter and not item == self.player and self.fov.visible(item.x, item.y):
                dist = self.player.distance_to(item)
                if dist < closest_dist:  #it's closer, so remember it
                    closest_enemy = item
                    closest_dist = dist
        return closest_enemy
