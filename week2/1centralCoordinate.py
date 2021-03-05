# centralCoordinate.py
# Setting a coordinate system with central origin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)    # bg color
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)    # define coordinates
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_STRIP)      # begin drawing
    glVertex2f(0.5, 0.0)
    glVertex2f(0.0, 0.5)
    glVertex2f(-0.5, 0.0)
    glVertex2f(0.5, 0.0)


    glEnd()                 # end drawing
    glFlush()               # dump on screen

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Coordinate system with Central Origin")
    glutDisplayFunc(plotpoints)
    init()
    glutMainLoop()
main()