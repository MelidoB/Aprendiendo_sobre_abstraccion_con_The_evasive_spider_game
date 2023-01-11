

def crear_character_que_sale_del_jugador(jugador,diccionario,character):
    A = jugador.point_a
    B = jugador.point_b

    derecha = jugador.position_value == 0
    izquierda = jugador.position_value == 2
    arriba = jugador.position_value == 3




    if derecha:
        character.point_a.x,character.point_a.y = (B.x,((jugador.image.get_height()/2)+A.y) - character.get_height()/2)
        character.position_value = 0
        print(A.y)

    elif izquierda:
        character.point_a.x,character.point_a.y = (A.x-character.get_height(),(jugador.image.get_height()/2)+A.y- character.get_height()/2)
        character.position_value = 2
        print(A.y)
    elif arriba:
        character.point_a.x,character.point_a.y = ((jugador.image.get_width()/2)+A.x-character.get_width()/2,A.y-character.get_height())
        character.position_value = 3
        print(A.y)
    else:
        character.point_a.x,character.point_a.y = (((jugador.image.get_width()/2) +A.x)-character.get_width()/2,B.y)
        character.position_value = 1

    character.set_point_b()
    
    diccionario['objetos_tirados_del_jugador'].append(character)
    