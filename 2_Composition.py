from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import numpy as np
import math
show_translated = False

def composition(*array):
    # Start with first matrix
    print(array)
    result = array[-1]
    
    # Multiply one by one
    for m in array[-2::-1]:
        result = np.dot(m,result)   
    print(result)
    result=np.transpose(result)
    return result.tolist()   

def apply_translation(dx, dy):
    translation_matrix = [
    [1, 0, dx],
    [0, 1, dy],
    [0, 0, 1]
   ]
    return translation_matrix

def apply_scaling(sx, sy):
    scaling_matrix = [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]
    return scaling_matrix


def apply_rotation(angle_degrees):
    theta = math.radians(angle_degrees)  # Convert degrees to radians
    rotation_matrix = [
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta),  math.cos(theta), 0],
        [0, 0, 1]
    ]
    return rotation_matrix


# Function to draw bitmap text in OpenGL
def draw_text(x, y, text, color=(0, 0, 1)):
    glColor3f(*color)
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(ch))

def show():
    global show_translated

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    triangle_points = [[50, 0,1], 
                       [100, 0,1],
                       [50,50,1]]
    if not show_translated:
    # Draw original triangle
       glColor3f(0, 0, 1)
       glBegin(GL_POLYGON)
       for (x,y,z) in triangle_points:
          glVertex2f(x,y)
       glEnd()

    # Draw translated triangle (after delay)
    else:
        new_points=composition(np.array(apply_translation(dx=20, dy=20)),
                               np.array(apply_scaling(2,2,)),
                               np.array(apply_rotation(20)),
                               np.transpose(np.array(triangle_points)))
        glColor3f(1, 0, 0)
        glBegin(GL_POLYGON)
        for (x,y,z) in new_points:
            glVertex2f(x, y)
        glEnd()
        draw_text(250, 480, "Composition", color=(0, 0, 0))
    glutSwapBuffers()


def update(value):
    """Called by timer after delay."""
    global show_translated
    show_translated = True
    glutPostRedisplay()


# Main setup
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Triangle Transformation using Matrix Multiplication")
glClearColor(0.9, 0.9, 0.9, 1.0)
glutDisplayFunc(show)
# Trigger update after 2 seconds (2000 ms)
glutTimerFunc(2000, update, 0)
glutMainLoop()
