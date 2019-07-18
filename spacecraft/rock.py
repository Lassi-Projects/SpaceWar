from spacecraft.hull import Hull
from globals import Globals

#Flying rocks class
class Rock(Hull):
    """Flying object with no speed modification
    
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

    def move_down(self):
        """Move rock down

        Movement speed determined by speed on y-axis (int sy)
        Returns itself when it is outside canvas, otherwise None is returned.
        """
        self.y = self.y + self.sy

        if self.y > Globals.canvas_size[1]:
            return self
        else:
            return None