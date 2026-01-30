from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np  

def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window\

    glColor3f(1.0, 1.0, 1.0)  # white color for line
    glBegin(GL_POINTS)
    glVertex2i(250, 250) 
    glVertex2i(250, 251)  
    glVertex2i(251, 250) 
    glVertex2i(251, 251)  



    glVertex2i(350, 350) 
    glVertex2i(350, 351)  
    glVertex2i(351, 350) 
    glVertex2i(351, 351)  
    

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

