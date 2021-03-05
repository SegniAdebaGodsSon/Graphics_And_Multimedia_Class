# plottingFucntions.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys


def init():
     glClearColor(0.5, 0.8, 0.3, 1.0)
     gluOrtho2D(-10.0, 10.0, -10.0, 10.0)
def plotfunc():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.0, 0.0, 0.0)
     glPointSize(2.0)
     #drawing the coordinate system for visual refrence 
     glBegin(GL_LINES)
     glVertex2f(-10.0, 0.0)
     glVertex2f(10.0, 0.0)
     glVertex2f(0.0, 10.0)
     glVertex2f(0.0, -10.0)
     glEnd()
     
          
     for x in arange(-10.0, 10.0, 0.0001):
          y = x**2 -2
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
