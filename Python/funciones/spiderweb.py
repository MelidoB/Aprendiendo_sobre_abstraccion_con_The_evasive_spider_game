from funciones.crear_objeto_que_sale_del_jugador import crear_character_que_sale_del_jugador
from funciones.objetos_y_characteres import crear_character


def crea_spiderweb(items_to_display):
    spiderweb = crear_character('spiderweb',(-9999,-9999),'spiderweb.png')
    crear_character_que_sale_del_jugador(items_to_display['jugador'][0],items_to_display,spiderweb)

def mueve_spiderweb(spider_web):
    if spider_web:#Si hay alguna spider web en el array
        for i in spider_web:
            i.move_forward()
            i.set_point_b()
    ############SPIDERWEB##############