from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import NW

import math

#Superclass for all moving objects on Canvas
class Hull():
    """Hull class used as a superclass for all moving elements in game
    
    It is created with 3 requiered arguments:
                                position on x-axis (int x),
                                position on y-axis (int y),
                                hull's image path (str image_path)
                                
                            And has 3 optional arguments
                                speed on x-axis (int sx)[defaults to 0]
                                speed on y-axis (int sy)[defaults to 0]
                                speed is pixels/10ms
                                object size compared to original photosize x:100
                                    (int scale > 0)[defaults to 100]
                                """
    #Default constructor
    def __init__(self, x: float, y: float, image_path: str, 
                 sx: float = 0, sy: float = 0, scale: int = 100):
        #setting image to correct size
        self.image = PhotoImage(file = image_path)

        #TODO: add image scaling
        self.size = [self.image.width(), self.image.height()]

        self.x = x
        self.y = y
        #speed is in pixels/10ms
        self.sx = sx
        self.sy = sy

        self.size = [self.image.width(), self.image.height()]

    def get_radius(self) -> int:
        """Calculates objects radius"""
        
        n = min(self.size)
        n = n / 2
        n = int(n)
        return n

    def get_image(self) -> PhotoImage:
        """Returns PhotoImage containing object's picture"""
        return self.image

    def draw(self, canvas: Canvas):
        """Draws object's picture on given canvas"""
        canvas.create_image(self.x - (self.size[0] / 2), \
            self.y - (self.size[1] / 2), anchor = NW, image = self.image)

    def collision(self, other):
        """Checks collision with parameter object. If collision, returns true, else returns false"""

        distance = math.sqrt((abs(self.x - other.x) ** 2) \
           + (abs(self.y - other.y)** 2))

        if distance < self.get_radius() + other.get_radius():
            return True
        else:
            return False