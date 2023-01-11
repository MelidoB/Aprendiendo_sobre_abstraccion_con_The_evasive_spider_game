from application_files.application import Application
from funciones.objetos_y_characteres import crear_character,crear_objeto

#Instancias

spider = crear_character('spider',(0,200),'spider.png',3,200)

spider.spiderweb_cooldown = 30
enemies = []

x=200
for i in range(3):
    enemies.append(crear_character('enemy',(x,200),'enemy.png',max_health=100))
    x+=400

pared = crear_objeto('wall',(400,0),'wall.png')

a = Application()

a.items_to_display['jugador'] = [spider]
a.items_to_display['enemigo'] =enemies
a.items_to_display['paredes'] = [pared]
a.items_to_display['objetos_tirados_del_jugador'] = []

a.run()

#a.run()


