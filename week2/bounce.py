# -- eyu --
# Bounce

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

global anim, x, y ,dx, dy
# initial position of the ball
x = -0.67
y = 0.34
# Direction "sign" of the ball's motion
dx = dy = 1
# Window dimensions
width = height = 500
axrng = 1.0
# No animation to start
anim = 0
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glColor3ub(255, 0, 0)
    # Dimensions of the screen
    # Make axrng larger and see what happens!
    gluOrtho2D(-axrng, axrng, -axrng, axrng)


def idle():
    # We animate only if anim == 1, otherwise
    # the ball doesn't move
    if anim == 1:
        glutPostRedisplay()


def bounce():
    global x, y, dx, dy
    glClear(GL_COLOR_BUFFER_BIT)
    # changes x and y
    x += 0.001*dx
    y += 0.001*dy
    # Keep the motion mathematics
    # Safe from harm and then
    # Move the ball location based on x and y
    glPushMatrix()
    glTranslate(x,y,0)
    glutSolidSphere(0.1, 50, 50)
    glPopMatrix()
    # Collision detection!
    # What happens here and why does this work?
    if x >= axrng or x <= -axrng:
        dx = -1*dx
    if y >= axrng or y <= -axrng:
        dy = -1*dy

    glFlush()


def keyboard(key, x, y):
    # Allows us to quit by pressing 'Esc' or 'q'
    # We can animate by "a" and stop by "s"
    key = str(key, "UTF-8")
    global anim
    if key == chr(27):
        sys.exit()
    if key == "a":
        # Notice we are making anim = 1
        # What does this mean? Look at the idle function
        anim = 1
    if key == "s":
        # STOP the ball!
        anim = 0
    if key == "q":
        sys.exit()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
    glutInitWindowPosition(100,100)
    glutInitWindowSize(width,height)
    glutCreateWindow("Bounce")
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(idle)
    init()
    glutMainLoop()

main()