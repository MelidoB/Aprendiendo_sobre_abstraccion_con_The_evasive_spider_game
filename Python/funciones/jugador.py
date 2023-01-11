from pygame import key
def mover_al_jugador(jugador):
        """it will move depending on which of the 4 direction key is press"""
        key_pressed = key.get_pressed()
        if key_pressed[ord('a')]:
            jugador.move_left()
        if key_pressed[ord('d')]:
            jugador.move_right()
        if key_pressed[ord('w')]:#[0,1,2,3] Derecha,Abajo,Izquierda,Arriba
            if jugador.position_value == 0 and not jugador.se_puede_mover_para_derecha:
                jugador.se_puede_mover_para_arriba = False
            elif jugador.position_value == 1 and not jugador.se_puede_mover_para_abajo:
                jugador.se_puede_mover_para_arriba = False
            elif jugador.position_value == 2 and not jugador.se_puede_mover_para_derecha:
                jugador.se_puede_mover_para_arriba = False
            elif jugador.position_value == 3 and not jugador.se_puede_mover_para_arriba:
                jugador.se_puede_mover_para_arriba = False
            else:
                jugador.move_forward()
        if key_pressed[ord('s')]:
            if jugador.position_value == 2 and not jugador.se_puede_mover_para_derecha:
                jugador.se_puede_mover_para_abajo = False
            elif jugador.position_value == 3 and not jugador.se_puede_mover_para_abajo:
                jugador.se_puede_mover_para_abajo = False
            elif jugador.position_value == 0 and not jugador.se_puede_mover_para_derecha:
                jugador.se_puede_mover_para_abajo = False
            elif jugador.position_value == 1 and not jugador.se_puede_mover_para_arriba:
                jugador.se_puede_mover_para_abajo = False
            else:
                jugador.move_backwards()