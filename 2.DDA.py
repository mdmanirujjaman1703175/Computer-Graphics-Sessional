from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def DDA(x1, y1, x2, y2):
    
    points = []
    dx = x2 - x1
    dy = y2 - y1    

    # Handle vertical line (dx = 0)
    if dx == 0:
        for y in range(y1, y2 + 1):
            points.append((x1, y))
        return points

    m = dy / dx  # slope
    y = y1

    # Gentle slope: |dx| >= |dy|
    if abs(dx) >= abs(dy):
        for x in range(x1, x2 + 1):
            points.append((round(x), round(y)))
            y += m
    else:
        x = x1
        step = 1 / m
        for y in np.arange(y1, y2 + 1, 1):
            points.append((round(x), round(y)))
            x += step
    return points

def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window\

    glColor3f(1.0, 1.0, 1.0)  # white color for line
    glBegin(GL_POINTS)
    points=DDA(100,100,300,300)
    for x,y in points:
        glVertex2i(x,y)



        
    x = np.arange(100, 201, 1)   # x from 100 to 200
    y = np.full_like(x,100)
    points = list(zip(x,y))
    for x,y in points:
        glVertex2i(x,y)
    glEnd()
    
    glutSwapBuffers()             # Refresh window


# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)             # Window size
glutCreateWindow(b"Simple OpenGL Window") # Window title
glClearColor(0.0, 0.0, 0.0, 1.0)  # Black background
gluOrtho2D(0, 500, 0, 500) # Define the 2D orthographic projection
glutDisplayFunc(show)                    # What to display
glutMainLoop() 

