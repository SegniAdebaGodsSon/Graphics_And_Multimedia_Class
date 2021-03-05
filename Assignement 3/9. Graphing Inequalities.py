# plottingFucntions.py
# Plotting functions
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys


#ANSWER


def init():
     glClearColor(0.5, 0.8, 0.3, 1.0)
     gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
def plotfunc():
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(0.0, 0.0, 0.0)
     glPointSize(1.0)
     #drawing the coordinate system for visual refrence 
     glBegin(GL_LINES)
     glVertex2f(-5.0, 0.0)
     glVertex2f(5.0, 0.0)
     glVertex2f(0.0, 5.0)
     glVertex2f(0.0, -5.0)
     glEnd()
     
          
     for x in arange(-5.0, 5.0, 0.01):
            y = x*x
            glColor3f(0.0, 0.0, 0.0)
            glBegin(GL_POINTS)
            glVertex2f(x,y)
            glEnd()
            for a in arange(-5.0, 5.0, 0.01):
                    if a < x*x:
                        glColor3f(0.50,0.50,0.50)
                        glBegin(GL_POINTS)
                        glVertex2f(x,a)
                        glEnd()
     glColor3f(0.0, 0.0, 0.0)
     glBegin(GL_LINES)
     glVertex2f(-5.0, 0.0)
     glVertex2f(5.0, 0.0)
     glVertex2f(0.0, 5.0)
     glVertex2f(0.0, -5.0)
     glEnd()
     glFlush()
   
     

     glFlush()
def main():
     glutInit(sys.argv)
     glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
     glutInitWindowPosition(50,50)
     glutInitWindowSize(400,400)
     glutCreateWindow("Function Plotter")
     glutDisplayFunc(plotfunc)
     init()
     glutMainLoop()
main()
