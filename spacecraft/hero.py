from spacecraft.hull import Hull
from globals import Globals


#Hero's spaceship (Hull with added features like acceleration)
class Hero(Hull):
    """Spaceship controlled by player with left and right movement
    
    It is created with 3 requiered arguments:
                                position on x-axis (int x),
                                position on y-axis (int y),
                                hull's image path (str image_path)
                                
                            And has 3 optional arguments
                                speed on x-axis (int sx)[defaults to 0]
                                speed on y-axis (int sy)[defaults to 0]
                                speed is pixels/10ms
                                object size compared to original photosize (float > 0)[defaults to 1]
                                """
    #Acceleration to left(amount of change given in argument)
    def move_left(self, event):
        """Move spaceship to left

        Movement speed determined by speed on x-axis (int sx)
        """
        self.x = ((self.x - self.sx) % Globals.canvas_size[0])

    #Acceleration to right
    def move_right(self, event):
        """Move spaceship to right

        Movement speed determined by speed on x-axis (int sx)
        """
        self.x = ((self.x + self.sx) % Globals.canvas_size[0])