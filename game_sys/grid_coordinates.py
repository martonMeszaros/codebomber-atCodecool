from game_sys.game_config import config


def grid_pos(grid_x, grid_y):
    pos_x = 0
    pos_y = 0
    if grid_x >= config.map_size[0]:
        pos_x = config.sprite_size[0] * (config.map_size[0]-1)
    elif grid_x > 0:
        pos_x = config.sprite_size[0] * grid_x
    if grid_y >= config.map_size[1]:
        pos_y = config.sprite_size[1] * (config.map_size[1]-1)
    elif grid_y > 0:
        pos_y = config.sprite_size[1] * grid_y
    return pos_x, pos_y


def snap_to_grid(pos_x, pos_y):
    grid_x = round(pos_x / config.sprite_size[0])
    grid_y = round(pos_y / config.sprite_size[1])
    return grid_pos(grid_x, grid_y)


def get_map_size():
    return config.map_size[0] * config.sprite_size[0], config.map_size[1] * config.sprite_size[1]
