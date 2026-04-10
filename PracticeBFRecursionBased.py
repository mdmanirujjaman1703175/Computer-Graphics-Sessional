import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

SIZE = 501
sys.setrecursionlimit(1000000)

# 0 = empty
# 1 = boundary
# 2 = filled
inside_points = []

# Create grid in simple C-style Python
grid = []
for i in range(SIZE):
    row = []
    for j in range(SIZE):
        row.append(0)
    grid.append(row)


# -----------------------------------
# Convert window coordinate to grid coordinate
# Window: origin bottom-left
# Grid:   origin top-left
# -----------------------------------
def window_to_grid(x, y):
    grid_x = x
    grid_y = SIZE - 1 - y
    return grid_x, grid_y


# -----------------------------------
# Draw boundary on grid
# -----------------------------------
def draw_boundary(points):
    for (x, y) in points:
        if 0 <= x < SIZE and 0 <= y < SIZE:
            gx, gy = window_to_grid(x, y)
            grid[gy][gx] = 1


# -----------------------------------
# Recursive Boundary Fill
# x, y are window coordinates
# -----------------------------------
def boundary_fill(x, y):
    # Step 1: outside window
    if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
        return

    # Convert window coordinate to grid coordinate
    gx, gy = window_to_grid(x, y)

    # Step 2: stop if boundary or already filled
    if grid[gy][gx] == 1 or grid[gy][gx] == 2:
        return

    # Step 3: fill current point
    grid[gy][gx] = 2
    inside_points.append((x, y))   # store window coordinate for drawing

    # Step 4: recursively visit 4-neighbors
    boundary_fill(x + 1, y)   # right
    boundary_fill(x - 1, y)   # left
    boundary_fill(x, y + 1)   # up
    boundary_fill(x, y - 1)   # down


# -----------------------------------
# DDA Line Drawing
# -----------------------------------
def DDA(x1, y1, x2, y2):
    points = []

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))
    if steps == 0:
        return [(x1, y1)]

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += x_inc
        y += y_inc

    return points


# -----------------------------------
# Reset grid
# -----------------------------------
def reset_grid():
    inside_points.clear()

    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] = 0


# -----------------------------------
# Display
# -----------------------------------
def show():
    glClear(GL_COLOR_BUFFER_BIT)

    reset_grid()

    # Triangle vertices in window coordinates
    A = (100, 100)
    B = (300, 120)
    C = (180, 300)

    # Get boundary points
    points1 = DDA(A[0], A[1], B[0], B[1])
    points2 = DDA(B[0], B[1], C[0], C[1])
    points3 = DDA(C[0], C[1], A[0], A[1])

    boundary_points = points1 + points2 + points3

    # Mark boundary in grid
    draw_boundary(boundary_points)

    # Draw triangle boundary using window coordinates
    glColor3f(1.0, 1.0, 1.0)   # white
    glBegin(GL_POINTS)
    for x, y in boundary_points:
        glVertex2i(x, y)
    glEnd()

    # Seed point (centroid)
    seed_x = (A[0] + B[0] + C[0]) // 3
    seed_y = (A[1] + B[1] + C[1]) // 3

    # Fill inside
    boundary_fill(seed_x, seed_y)

    # Draw filled pixels using window coordinates
    glColor3f(1.0, 0.0, 0.0)   # red
    glBegin(GL_POINTS)
    for x, y in inside_points:
        glVertex2i(x, y)
    glEnd()

    glutSwapBuffers()


# -----------------------------------
# Main
# -----------------------------------
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutCreateWindow(b"Boundary Fill Triangle")
glClearColor(0.0, 0.0, 0.0, 1.0)
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(show)
glutMainLoop()