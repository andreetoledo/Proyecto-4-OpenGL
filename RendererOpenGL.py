import pygame
from pygame.locals import *

from gl import Renderer, Model
import shaders
import glm
from math import sqrt, sin, cos, tan, radians

cubeX = 0
cubeY = 0
cubeZ = 0
roll = 0
pitch = 0
yaw = 0
distance = 0
deltaTime = 0.0

changeY=False
changeX=False

# Inicializacion de pygame
pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, OPENGLBLIT | DOUBLEBUF | OPENGL)

#backgroung
#bgspace=pygame.image.load('spaceIm.jpg')

# Inicializacion de nuestro Renderer en OpenGL
r = Renderer(screen)
r.camPosition.z = 3
r.camPosition.x = 0
r.camPosition.y = 0
r.pointLight.x = 5


r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

#r.modelList.append(Model('dogo.obj', 'dogo1.bmp'))

#Incluir audio
def play_music():
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.init()
        pygame.mixer.music.load("audio.mp3")
        pygame.mixer.music.play(10)

def play_audio():
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play(0)


isPlaying = True
while isPlaying:

    # Para revisar si una tecla esta presionada
    keys = pygame.key.get_pressed()
    # Move cam
    if keys[K_d]:
        r.camPosition.x += 5 * deltaTime
    if keys[K_a]:
        r.camPosition.x -= 5 * deltaTime
    if keys[K_w]:
        r.camPosition.z -= 5 * deltaTime
    if keys[K_s]:
        r.camPosition.z += 5 * deltaTime
    if keys[K_e]:
        #Reproduce la música
        play_audio()
        r.modelList.clear
        r.modelList.append(Model('rata.obj', 'rata.bmp'))
    if keys[K_q]:
        #Reproduce la música
        play_audio()
        r.modelList.clear
        r.modelList.append(Model('wolf.obj', 'wolf.bmp'))
    if keys[K_r]:
        r.modelList.clear
        r.modelList.append(Model('dogo.obj', 'dogo1.bmp'))

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            # para revisar en el momento que se presiona una tecla
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False

    # Main Renderer Loop
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    r.cont=r.cont+1


pygame.quit()
