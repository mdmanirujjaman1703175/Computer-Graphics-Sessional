from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window
    glLoadIdentity() # Reset transformations
    glOrtho(0, 500, 0, 500, -1, 1) 
    
    #drawing traingle.
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    for v in [(0,0),(250,0),(250,250)]:
        glVertex2f(*v)
    glEnd()
    
    glutSwapBuffers()             # Refresh window

# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)             # Window size
glutCreateWindow(b"Simple OpenGL Window") # Window title
#glClearColor(0.2, 0.6, 1.0, 1.0) # RGBA (Red, Green, Blue, Alpha)
glutDisplayFunc(show)                    # What to display
glutMainLoop()                           # Keep window open
