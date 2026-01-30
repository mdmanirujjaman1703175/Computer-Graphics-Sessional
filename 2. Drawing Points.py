#Triangle Drawing
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window
    glLoadIdentity() # Reset transformations
    glOrtho(0, 500, 0, 500, -1, 1) # Set 2D coordinate system from 0 to 500 in X and Y
    
    glColor3f(1.0,1.0,1.0)
    points=[(100,100),(99,100),(100,99),(98,99),(99,98),(101,100),(100,101)]
    points2 = [
    [200, 200],
    [199, 200],
    [200, 199],
    [198, 199],
    [199, 198],
    [201, 200],
    [200, 201]
]

    glBegin(GL_POINTS)
    # glVertex2i(100,100)
    # glVertex2i(99,100)
    # glVertex2i(100,99)
    # glVertex2i(100,101)
    # glVertex2i(101,100)
    # glVertex2i(102,100)
    # glVertex2i(100,102)
    
    for x,y in points:
        glVertex2i(x,y)
    
    for x,y in points2:
        glVertex2i(x,y)
    glEnd()

    
    glutSwapBuffers()             # Refresh window

# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)             # Window size
glutCreateWindow(b"Simple OpenGL Window") # Window title
glClearColor(0.0, 0.0, 0.0, 1.0) # RGBA (Red, Green, Blue, Alpha)
glutDisplayFunc(show)                    # What to display
glutMainLoop()                           # Keep window open