from display.object import Object
from display.point import Point
from pygame import transform,image
from funciones.array_functions import circulate_through_array

class Character(Object):
    def __init__(self,name,coordinates):
        Object.__init__(self,name,coordinates)

        self.position = [0,1,2,3] #Derecha,Abajo,Izquierda,Arriba
        self.position_value = 0
        self.se_puede_mover_para_izquierda = True
        self.se_puede_mover_para_derecha = True
        self.se_puede_mover_para_arriba = True
        self.se_puede_mover_para_abajo = True




    #Movement functions
    def move_left(self):
        """self.point_a.x -= 5
        self.point_b.x -= 5"""
        new_images = []
        for i in self.save_images:
            i = transform.rotate(i, 90)
            new_images.append(i)
        self.save_images = new_images
        self.position_value = circulate_through_array(self.position_value-1,len(self.position))
        self.image = (self.save_images[self.image_value])

        self.set_point_b()


    def move_right(self):
        """self.point_a.x += 5
        self.point_b.x += 5"""
        new_images = []
        for i in self.save_images:
            i = transform.rotate(i, -90)
            new_images.append(i)
        self.save_images = new_images
        self.position_value = circulate_through_array(self.position_value + 1, len(self.position))
        self.image = (self.save_images[self.image_value])

        self.set_point_b()

    def move_forward(self):


        #[0,1,2,3] Derecha,Abajo,Izquierda,Arriba
        if self.position_value == 0 and self.se_puede_mover_para_derecha:
            self.point_a.x += 5
        elif self.position_value == 1 and self.se_puede_mover_para_abajo:
            self.point_a.y += 5
        elif self.position_value == 2 and self.se_puede_mover_para_izquierda:
            self.point_a.x -= 5
        elif self.position_value == 3 and self.se_puede_mover_para_arriba:
            self.point_a.y -= 5

        self.set_point_b()

        if self.save_images:#list
            self.image_value = circulate_through_array(self.image_value + 1, len(self.save_images))
            self.image = (self.save_images[self.image_value])


    def move_backwards(self):

        if self.position_value == 0 and self.se_puede_mover_para_izquierda:
            self.point_a.x -= 5
            self.point_b.x -= 5
        elif self.position_value == 1 and self.se_puede_mover_para_arriba:
            self.point_a.y -= 5
            self.point_b.y -= 5
        elif self.position_value == 2 and self.se_puede_mover_para_derecha:
            self.point_a.x += 5
            self.point_b.x += 5
        elif self.position_value == 3 and self.se_puede_mover_para_abajo:
            self.point_a.y += 5
            self.point_b.y += 5
        self.image_value = circulate_through_array(self.image_value - 1, len(self.save_images))
        self.image = (self.save_images[self.image_value])






