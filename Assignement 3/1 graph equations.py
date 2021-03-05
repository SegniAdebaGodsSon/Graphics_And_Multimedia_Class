from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

     
a=(input("Choose a letter a-g to see answers"))

def init():
     glClearColor(0.5, 0.8, 0.3, 1.0)
     gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.0, 0.0, 0.0)
     glPointSize(3.0)
     #drawing the coordinate system for visual refrence 
     glBegin(GL_POINTS)
     glVertex2f(-5.0, 0.0)
     glVertex2f(5.0, 0.0)
     glVertex2f(0.0, 5.0)
     glVertex2f(0.0, -5.0)
     glEnd()
     if a=="a":
          
          for x in arange(-5.0, 5.0, 0.1):
              y = x**2 -2
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="b":
          for x in arange(-5.0, 5.0, 0.1):
              y = x**3 -3*x -1
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="c":
          for x in arange(-5.0, 5.0, 0.1):
              y = x**4 -5*x**3+x**2-3*x-1
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="d":
          for x in arange(-5.0, 5.0, 0.1):
              y = math.sin(x)
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="e":
          for x in arange(-5.0, 5.0, 0.1):
              y = math.sin(3*x)
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="f":
          for x in arange(-5.0, 5.0, 0.1):
              y = math.sin(x/3)
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     if a=="g":
          for x in arange(-5.0, 5.0, 0.1):
              y = math.cos(x)
              glBegin(GL_POINTS)
              glVertex2f(x, y)
              glEnd()
     

     glFlush()
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
     glutInitWindowPosition(50,50)
     glutInitWindowSize(400,400)
     glutCreateWindow("Window")
     glutDisplayFunc(plotfunc)
     init()
     glutMainLoop()
main()
