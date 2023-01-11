import pygame
from application_files.close_game import close_game_function
from funciones.barra_de_salud import crear_barra_de_salud_para_enemigos,crear_barra_de_salud_para_jugador
from funciones.jugador import mover_al_jugador
from funciones.object_collition import determina_si_los_objetos_colicionan,determina_si_los_objetos_estan_dentro
from funciones.crear_objeto_que_sale_del_jugador import crear_character_que_sale_del_jugador
from funciones.objetos_y_characteres import crear_character
from funciones.spiderweb import crea_spiderweb, mueve_spiderweb


class Application:
    def __init__(self):
        self.gameDisplay = None
        self.clock = None
        self.items_to_display = {}


    def run(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((1400, 800))
        self.clock = pygame.time.Clock()
        while True:
            close_game_function()

            self.gameDisplay.fill((255,255,255))

            # Checkear si el jugador y el enemigo estan juntos

            # Checkear si el jugador y el objeto estan juntos

            for paredes in self.items_to_display['paredes']:
                izquierda, derecha, arriba, abajo = determina_si_los_objetos_colicionan(self.items_to_display['jugador'][0],
                                                                                    paredes)


            self.items_to_display['jugador'][0].se_puede_mover_para_izquierda = izquierda
            self.items_to_display['jugador'][0].se_puede_mover_para_derecha = derecha
            self.items_to_display['jugador'][0].se_puede_mover_para_arriba = arriba
            self.items_to_display['jugador'][0].se_puede_mover_para_abajo = abajo



            #determina_si_los_objetos_estan_dentro(self.items_to_display['jugador'][0],self.items_to_display['enemigo'][0])

            # Update all objects
            mover_al_jugador(self.items_to_display['jugador'][0]) # Mover al jugador

            ############SPIDERWEB##############
            #Si la tecla para crear spider webs es presionada se creara una
            key_pressed = pygame.key.get_pressed()
            cooldown = self.items_to_display['jugador'][0].spiderweb_cooldown < 30
            if not cooldown and key_pressed[ord('f')]:
                crea_spiderweb(self.items_to_display)
                self.items_to_display['jugador'][0].spiderweb_cooldown = 0
            else:
                self.items_to_display['jugador'][0].spiderweb_cooldown += 1
            mueve_spiderweb(self.items_to_display['objetos_tirados_del_jugador'])


            #Mira si el enemigo choca con la spider web
            temporary_list = self.items_to_display['objetos_tirados_del_jugador'].copy()
            for enemy in self.items_to_display['enemigo']:
                for objeto in self.items_to_display['objetos_tirados_del_jugador']:
                    #can move
                    izquierda, derecha, arriba, abajo = determina_si_los_objetos_colicionan(enemy,objeto)
                    if izquierda and derecha and arriba and abajo:
                        pass
                    else:
                        try:
                            temporary_list.remove(objeto)
                        except:
                            pass
                        enemy.current_health -= 50
                        print(enemy.current_health)
            self.items_to_display['objetos_tirados_del_jugador'] = temporary_list
            ############SPIDERWEB##############


            #Chequea si algun enemigo ha muerto. Esto puedo cambiarlo para todos los objetos ya luego
            temporary_list = []
            for i in self.items_to_display['enemigo']:
                if i.current_health > 0:
                    temporary_list.append(i)
            self.items_to_display['enemigo'] = temporary_list



            crear_barra_de_salud_para_jugador(self.items_to_display['jugador'][0], self.items_to_display, (1050, 55))
            temp_1 = []
            temp_2 = []
            for enemy in self.items_to_display['enemigo']:
                temp_value_1, temp_value_2 = crear_barra_de_salud_para_enemigos(enemy, self.items_to_display,(enemy.point_a.x, enemy.point_a.y))
                temp_1.append(temp_value_1)
                for i in temp_value_2:
                    temp_2.append(i)
            self.items_to_display['enemy_health_bar'] = temp_1.copy()
            self.items_to_display['enemy_health_bar_chunks'] = temp_2.copy()
            #Display all objects
            for i in self.items_to_display.values():
                for j in i:
                    self.gameDisplay.blit(j.image, (j.point_a.x, j.point_a.y))

            self.clock.tick(60)
            pygame.display.update()
            #keypress_select_direction(player)
            #randomly_select_direction(enemy)
            #show all instances into application
            #display instances ()
