# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
# IMPORT OBJECT LOADER
from objloader import *


pygame.init()
viewport = (1000,700)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.4, 0.4, 0.4, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

# LOAD OBJECT AFTER PYGAME INIT
cityObj = OBJ('Graphics Final Project\city.obj', swapyz=True)

cityObj.generate()



glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 0.001, 1000.0)

glScale(1/900, 1/900, 1/900)


# glScale(1/10, 1/10, 1/10)
# glTranslate(0, 1000, 1000)
# glScale(1/11, 1/13, 1/10)
# glRotate(-45, 1, 0, 0)


glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)
clock = pygame.time.Clock()
rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False
while 1:

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(200, zpos-200)
            elif e.button == 5: zpos += 200
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # RENDER OBJECT
    glTranslate(tx*20., ty*20., - zpos)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 0, 1)

   

    cityObj.render()

    pygame.display.flip()
    clock.tick(600)

print("hi")
print("hi")