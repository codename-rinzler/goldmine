import libtcodpy as libtcod

class FieldOfView:
    def __init__(self, player, map, width, height, torch_radius = 10, fov_light_walls = True, fov_algo = 0):
        self.need_recompute = True
        self.fov_map = libtcod.map_new(width, height)
        self.player = player
        self.torch_radius = torch_radius
        self.fov_light_walls = fov_light_walls
        self.fov_algo = fov_algo

        for y in range(height):
            for x in range(width):
                libtcod.map_set_properties(self.fov_map, x, y, not map.map[x][y].block_sight, not map.map[x][y].blocked)

    def recompute(self):
        if self.need_recompute:
            self.need_recompute = False
            pos = self.player.components['position']
            libtcod.map_compute_fov(self.fov_map, pos.x, pos.y, self.torch_radius, self.fov_light_walls, self.fov_algo)

    def visible(self, x, y):
        return libtcod.map_is_in_fov(self.fov_map, x, y)
