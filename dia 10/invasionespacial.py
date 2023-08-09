import pygame
from pygame import mixer
import random
import math
import io

# inicializar pygame
pygame.init()

'''
variables del juego
'''
# variables generales
PANT_X = 800  # tamanio de la pantalla en x
PANT_Y = 600  # tamanio de la pantalla en y
RED = 205  # valor de rojo del color de fondo
GREEN = 144  # valor de verde del color de fondo
BLUE = 228  # valor de azul del color de fondo
TITULO = "Space Invation"  # titulo del juego
ICONO = "ovni.png"  # archivo del icono del juego
FONDO = "fondo_espacio.png"


# transformar string a bytes
def fuente_bytes(fuent):
    with open(fuent, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente_final = pygame.font.Font(fuente_como_bytes, 32)

# musica
MUSICA = "MusicaFondo.mp3"
volumen = 0.3


# puntaje
puntaje = 0
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# variables de jugador
IMG_JUGADOR = "astronave.png"  # archivo de la imagen del jugador
jugador_x = 368  # posicion inicial en x
jugador_y = 536  # posicion inicial en y
movimiento_x = 0  # movimiento inicial en x
movimiento_y = 0  # movimiento inicial en y

# variables de enemigos
IMG_ENEMIGOS = []
enemigo_x = []
enemigo_y = []
movimiento_en_x = []
movimiento_en_y = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    IMG_ENEMIGOS.append("alien-ship.png")  # imagen de los enemigos
    enemigo_x.append(random.randint(0, 736))  # posicion inicial en x
    enemigo_y.append(random.randint(50, 400))  # posicion inicial en y
    movimiento_en_x.append(3)  # movimiento en x
    movimiento_en_y.append(50)  # movimiento en y

# variables del disparo
IMG_DISPARO = "sun (1).png"
disparo_x = 0
disparo_y = jugador_y
movimiento_dis_x = 0
movimiento_dis_y = 17
disparo_visible = False
SONIDO_DISPARO = "disparo.mp3"
vol_disparo = 0.5
SONIDO_COLISION = "golpe.mp3"
vol_colision = 0.5

'''
funciones 
'''


# creamos la pantalla con un tamanio de x, y
def crear_pantalla(x, y):
    return pygame.display.set_mode((x, y))


# definir el color de la pantalla
def color_pantalla(r, g, b):
    pantalla.fill((r, g, b))


# actualizar pantalla
def actualizar():
    pygame.display.update()


# titulo del juego
def titulo(string):
    pygame.display.set_caption(string)


# cargo una imagen a pygame
def cargar_imagen(string):
    return pygame.image.load(string)


# defino un icono para el juego
def set_icono(string):
    pygame.display.set_icon(cargar_imagen(string))


# cargo una imagen y la defino como jugador
def mostrar_imagenes(string, tupla):
    pantalla.blit(cargar_imagen(string), tupla)


def mostrar_enemigo(x, y, ene):
    pantalla.blit(cargar_imagen(IMG_ENEMIGOS[ene]), (x, y))


# realizar disparo
def disparar(disparo, x, y):
    global disparo_visible
    disparo_visible = True
    mostrar_imagenes(disparo, (x + 16, y + 10))


# detectar colisiones
def chequear_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    if distancia < 27:
        return True
    else:
        return False


# generar enemigo
def generar_enemigo():
    x = random.randint(0, 736)
    y = random.randint(50, 400)
    return x, y


# mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# agregar musica
def musica(arch, vol):
    mixer.music.load(arch)
    mixer.music.set_volume(vol)
    mixer.music.play(-1)


# ejecutar algun sonido
def ejecutar_sonido(arch, vol):
    sonido = mixer.Sound(arch)
    sonido.set_volume(vol)
    sonido.play()


# mostrar texto al terminar el juego
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))


'''
Programa principal del juego
'''
# crear la pantalla
pantalla = crear_pantalla(PANT_X, PANT_Y)

# titulo e icono
titulo(TITULO)
set_icono(ICONO)

# agregar musica
musica(MUSICA, volumen)

# loop del juego
se_ejecuta = True
while se_ejecuta:
    color_pantalla(RED, GREEN, BLUE)

    # imagen de fondo
    mostrar_imagenes(FONDO, (0, 0))

    # iterar eventos
    for evento in pygame.event.get():
        # evento quit
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimiento_x = -3
            elif evento.key == pygame.K_RIGHT:
                movimiento_x = 3
            elif evento.key == pygame.K_SPACE:
                ejecutar_sonido(SONIDO_DISPARO, vol_disparo)
                if not disparo_visible:
                    disparo_x = jugador_x
                    disparar(IMG_DISPARO, disparo_x, disparo_y)
        if evento.type == pygame.KEYUP:
            movimiento_x = 0

    # modificar ubicacion del jugador
    jugador_x += movimiento_x
    # mantener al jugador dentro de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar ubicacion del enemigo
    for e in range(cantidad_enemigos):
        # fin del juego
        if enemigo_y[e] > 472:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += movimiento_en_x[e]
    # mantener al enemigo dentro de la pantalla
        if enemigo_x[e] <= 0:
            movimiento_en_x[e] = 3
            enemigo_y[e] += movimiento_en_y[e]
        elif enemigo_x[e] >= 736:
            movimiento_en_x[e] = -3
            enemigo_y[e] += movimiento_en_y[e]

        # colision
        colision = chequear_colision(enemigo_x[e], enemigo_y[e], disparo_x, disparo_y)
        if colision:
            ejecutar_sonido(SONIDO_COLISION, vol_colision)
            disparo_y = jugador_y
            disparo_visible = False
            puntaje += 1
            enemigo_x[e], enemigo_y[e] = generar_enemigo()

        mostrar_enemigo(enemigo_x[e], enemigo_y[e], e)

    # mover elementos
    if disparo_y <= -32:
        disparo_y = jugador_y
        disparo_visible = False
    if disparo_visible:
        disparar(IMG_DISPARO, disparo_x, disparo_y)
        disparo_y -= movimiento_dis_y

    mostrar_imagenes(IMG_JUGADOR, (jugador_x, jugador_y))
    mostrar_puntaje(texto_x, texto_y)

    # actualizar pantalla
    actualizar()
