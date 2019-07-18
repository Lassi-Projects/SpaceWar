from tkinter import NW
from tkinter import Tk
from tkinter import Canvas

import random
import time
import math

from globals import Globals
from spacecraft.hull import Hull
from spacecraft.hero import Hero
from spacecraft.rock import Rock

#DRAW images on the canvas
def graphics_operator(canvas: Canvas, hulls: list, spacehero: Hero, points: int):
    """Handles all drawing that happens on canvas

    Parameters:
        canvas (Canvas) to draw on
        hulls (list) containing all non-spacehero moving objects
        spacehero (Hero) player-controlled unit
    """

    points_text = "Points: " + str(points)

    #clear old drawings
    canvas.delete("all")

    #create black background
    canvas.create_rectangle(0, 0, Globals.canvas_size[0], Globals.canvas_size[1], fill = "black")

    #show points on canvas 
    canvas.create_text(Globals.canvas_size[0] - 60, 10, anchor = NW, text=points_text, fill="white")

    #draw spacehero
    spacehero.draw(canvas)

    #draw other items
    for hull in hulls:
        hull.draw(canvas)

###
#STARTING INTERFACE ITEMS

#master
master = Tk()
master.title("Space Mission") #name
master.resizable(0, 0) #not resizeable

#canvas
canvas = Canvas(master, width = Globals.canvas_size[0], height = Globals.canvas_size[1])
canvas.pack()

#time
last_time = time.time()

###
#GAME part

def spawn_meteor(hulls: list, points):
    """Adds new enemies to hulls-list

    Parameters:
        hulls (list) containing all non-hero moving objects
    """
    point_level = int(points / Globals.points_to_acc)
    rock_speed = Globals.speed_rock + Globals.rock_acceleration * (point_level)

    hulls.append(Rock(random.randint(0, Globals.canvas_size[0]), 0, Globals.image_rock, sy = rock_speed))

def game_over():
    """Actions taken at end of the game"""
    master.destroy()
    print("Game over\nYour points: ", points)

#hulls list to contain all non-hero moving objects
hulls = list()

#Player-controlled Hero object created on the bottom of canvas
spacehero = Hero(Globals.canvas_size[0] / 2, Globals.position_hero_y, Globals.image_hero, sx = Globals.speed_hero)

#points calculator /points added when rocks reach bottom of the screen
points = Globals.starting_points
#Controls meteor spawning
spawn_control = False

#Eventhandlers
def graphics_refresher():
    """Recursion loop to control canvas drawing"""
    graphics_operator(canvas, hulls, spacehero, points)
    master.after(Globals.graphics_refresh_rate, graphics_refresher)

def game_manager():
    """Recursion loop to control game objects refreshing"""

    #control points
    global points
    #Control interval of spawns
    global last_time
    global spawn_control
    #create random integer
    rnd = random.randrange(Globals.rate_range)

    #Create new enemies
    if(spawn_control):
        spawn_meteor(hulls, points)
        last_time = time.time()
        spawn_control = False
    #spawn enemies after spawn_interval time and if rnd exceeds rate_limit
    elif(time.time() - last_time > Globals.spawn_interval and rnd > Globals.rate_limit):
        spawn_control = True

    #Move and refresh all non-hero items
    for hull in hulls:
        if type(hull) == Rock:
            #hull.move_down returns object itself if it reaches bottom of screen
            remove_checker = hull.move_down()
            if(remove_checker == hull):
                #remove hull referance from list
                hulls.remove(hull)
                #add points
                points += 1

    #Check collision of Rocks and Spacehero
    for hull in hulls:
        if hull.collision(spacehero):
            game_over()

    master.after(Globals.game_refresh_rate, game_manager)

master.after(10, game_manager)
master.after(50, graphics_refresher)
master.bind('<Right>', spacehero.move_right)
master.bind('<Left>', spacehero.move_left)

#mainloop
master.mainloop()