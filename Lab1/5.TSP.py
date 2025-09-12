from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def show():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear window
    
    glLoadIdentity()                     # Reset transformations
    glOrtho(0, 500, 0, 500, -1, 1)      # Set 2D coordinate system (graph paper 0–500)

     # Square (yellow)
    glColor3f(1, 1, 0)
    glBegin(GL_QUADS)
    for v in [(100,100),(200,100),(200,200),(100,200)]:
        glVertex2f(*v)
    glEnd()

    glColor3f(0, 0, 1)                   # Set color to blue
    glBegin(GL_TRIANGLES)                # Start drawing a triangle
    for v in [(220,100),(320,100),(270,200)]:
        glVertex2f(*v)                   # Specify triangle vertices
    glEnd()    
    
     # Polygon (red) – on top of both
    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    for v in [(150,250),(250,250),(270,300),(200,350),(130,300)]:
        glVertex2f(*v)
    glEnd()                         # Finish drawing the triangle



    glutSwapBuffers()             # Refresh window
    
# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)             # Window size
glutCreateWindow(b"Simple OpenGL Window") # Window title

# Set background color (light blue with alpha=0.5)
glClearColor(0.2, 0.6, 1.0, 1.0)

glutIdleFunc(show)
glutDisplayFunc(show)                    # What to display
glutMainLoop()                           # Keep window open