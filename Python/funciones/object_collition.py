def determina_si_los_objetos_colicionan(object_a,object_b):
    A = object_a.point_a
    B = object_a.point_b
    C = object_b.point_a
    D = object_b.point_b

    derecha = True
    izquierda = True
    arriba = True
    abajo = True

    # Izquierda y Derecha




    # El objeto esta en la misma coordenada de x que el otro
    if B.y >= C.y + 5 and A.y <= D.y - 5:
        #print("derecha o izquierda")
        if B.x > C.x > A.x:
            derecha = False #No se puede ir a la derecha
            #print("No se puede ir a la derecha")
        elif A.x < D.x < B.x:
            izquierda = False #No se puede ir a la izquierda
            #print("No se puede ir a la izquierda")


    # Arriba y Abajo



    # El objeto esta en la misma coordenada de y que el otro
    if B.x >= C.x+5 and A.x <= D.x -10:
        #print("arriba o abajo")
        if A.y < D.y < B.y:
            arriba = False #No se puede subir
            print("No se puede subir")
        elif B.y > C.y > A.y:
            abajo = False #No se puede bajar
            print("No se puede bajar")

    return izquierda, derecha,arriba,abajo


def determina_si_los_objetos_estan_dentro(object_a,object_b):
    A = object_a.point_a
    B = object_a.point_b
    C = object_b.point_a
    D = object_b.point_b

    objeto_a_esta_dentro_de_objeto_b = [
        A.x >= C.x,
        A.y >= C.y,
        B.x <= D.x,
        B.y <= D.y
    ]
    objeto_b_esta_dentro_de_objeto_a = [
        A.x < C.x,
        A.y < C.y,
        B.x > D.x,
        B.y > D.y
    ]
    if all(objeto_a_esta_dentro_de_objeto_b):
        print("Object a is inside object b.")

    elif all(objeto_b_esta_dentro_de_objeto_a):
        print("Object b is inside object a.")
