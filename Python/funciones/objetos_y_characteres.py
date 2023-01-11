from display.character import Character
from display.object import Object
from pygame import image

def crear_character(nombre,coordenadas,imagen,imagenes=0,max_health = 100):
    character = Character(nombre, coordenadas)  # enemigo
    character.set_image(f'{nombre}/{imagen}')

    for i in range(0, imagenes):
        character.save_images.append(image.load(f'Images/{nombre}/{i}.png'))

    character.set_point_b()
    character.max_health = max_health
    character.current_health = max_health

    return character


def crear_objeto(nombre, coordenadas, imagen, imagenes=0, max_health=100):
    object = Object(nombre, coordenadas)  # enemigo
    object.set_image(f'{nombre}/{imagen}')

    for i in range(0, imagenes):
        object.save_images.append(image.load(f'Images/{nombre}/{i}.png'))


    object.set_point_b()
    object.max_health = max_health
    object.current_health = max_health

    return object