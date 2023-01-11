from pygame import image
from display.point import Point

class Object:

    def __init__(self,name,coordinates):
        #Attributes
        self.name = name
        self.image = None
        self.image_value = 0
        self.save_images = []
        self.max_health = 0
        self.current_health = 0

        # x,y
        x, y = coordinates
        self.point_a = Point(x, y)
        self.point_b = None


        #Determine if it'll be displayed in the game
        self.display = True




    def set_image(self,img):
        self.image = image.load(f'Images/{img}')

    def not_display_anymore(self):
        self.display = False

    #All objects can move
    def change_coordinate(self):
        pass

    def set_point_b(self):
        x = self.point_a.x + self.image.get_width()
        y = self.point_a.y + self.image.get_height()
        self.point_b = Point(x,y)

    def get_width(self):
        return self.image.get_width()
    def get_height(self):
        return self.image.get_height()

