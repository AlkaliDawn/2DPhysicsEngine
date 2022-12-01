import pygame as pg
import numpy as np


def drawcenteredsquare(surf, color, pos, size):
    rect = pg.Rect(pos[0] - size / 2, pos[1] - size / 2, size, size)
    pg.draw.rect(surf, color, rect)
    return (surf, color, rect)


if __name__ == '__main__':
    # init pygame
    pg.init()

    # create a screen
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

    # create a clock
    clock = pg.time.Clock()

    # create list to store all the squares
    squares = []

    # game loop
    running = True
    while running:
        # set framerate
        clock.tick(60)

        # event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # draw
        screen.fill((0, 0, 0))
        if pg.mouse.get_pressed()[0]:
            squares.append(drawcenteredsquare(screen, (255, 255, 255), pg.mouse.get_pos(), 10))


        # draw all squares in the list to the screen
        for square in squares:




        # update screen
        pg.display.flip()
