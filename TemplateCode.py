from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time


start_time = 0
end_time = 0
def circle(xc,yc,r):
    global start_time, end_time
    start_time = time.perf_counter()
    points=[]
    #write the circle Drawing code here
    end_time = time.perf_counter()
    return points


# Function to draw bitmap text in OpenGL
def draw_text(x, y, text, color=(0, 0, 1)):
    glColor3f(*color)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))


def show():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw DDA line
    glColor3f(1.0, 0.0, 0.0)  # change the colour
    glBegin(GL_POLYGON)
    points=circle(250,250,100)
    for (x, y) in points:
        #
    glEnd()

    # Calculate execution time
    elapsed = (end_time - start_time) * 1e9  # nanoseconds

    # Display execution time text in window
    draw_text(50, 20, f"Execution Time: {elapsed:.2f} ns")

    # Optional: Display line label
    draw_text(250, 480, "DDA circle Drawing", color=(0, 0, 0))

    glutSwapBuffers()  # for double buffering


# OpenGL setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b" Circle Drawing - OpenGL")
gluOrtho2D(0, 500, 0, 500)       # 2D projection
glClearColor(0.9, 0.9, 0.9, 1.0) # light gray background
glutDisplayFunc(show)
glutMainLoop()
