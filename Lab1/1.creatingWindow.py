from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window
    glutSwapBuffers()             # Refresh window

# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)             # Window size
glutCreateWindow(b"Simple OpenGL Window") # Window title
glutDisplayFunc(show)                    # What to display
glutMainLoop()                           # Keep window open