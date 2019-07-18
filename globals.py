import os

#All immutable global functions and variables
class Globals():
    #Canvas size
    canvas_size = [800, 600]
    starting_points = 0
    game_refresh_rate = 10
    graphics_refresh_rate = 10

    #Hero specific
    position_hero_y = canvas_size[1] - 140
    speed_hero = 6 #pixel/10ms

    #Rock specific
    speed_rock = 2 #pixels/10ms
    rock_acceleration = 0.1 #(pixels/10ms)/points_to_acc
    points_to_acc = 5
    #spawn rate
    rate_range = 100
    rate_limit = 95
    spawn_interval = 1

    #Path to file
    dir_path = os.path.dirname(os.path.realpath(__file__))

    #Art work paths
    image_rock = dir_path + "/art/meteorB4.png"
    image_hero = dir_path + "/art/ship.png"