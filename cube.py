import pygame

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


punkty = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

krawedzie = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

# Nie uzywane dopki nie dodasz kolorow
powierzchnie = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

def cube():

    glBegin(GL_QUADS)
    for pow in powierzchnie:
        glColor3ub(148, 148, 148)
        for punkt in pow:
            glVertex3fv(punkty[punkt])
            
    glEnd()
    

    glBegin(GL_LINES)    
    for kr in krawedzie:
        glColor3ub(0, 0, 0)
        for punkt in kr:
            glVertex3fv (punkty[punkt])
            # glColor3fv((0, 0, 0))
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslate(-0.1, 0, 0)
        
                if event.key == pygame.K_d:
                    glTranslate(0.1, 0, 0)

                if event.key == pygame.K_w:
                    glTranslate(0, 0, -0.1)

                if event.key == pygame.K_s:
                    glTranslate(0, 0, 0.1)

                if event.key == pygame.K_j:
                    glRotatef(5, 1, 0, 0)

                if event.key == pygame.K_k:
                    glRotatef(-5, 1, 0, 0)

                if event.key == pygame.K_h:
                    glRotatef(5, 0, 1, 0)

                if event.key == pygame.K_l:
                    glRotatef(-5, 0, 1, 0)

                        
        #glRotatef(1, 3, 1, 1)  # Autorotacja
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube()
        pygame.display.flip()  # Sprobuj pygame.display.update()
        pygame.time.wait(10)


main()