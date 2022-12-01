import pygame as pg


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
        clock.tick(200)

        # event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # draw
        screen.fill((0, 0, 0))

        # map color to mouse position
        color = (pg.mouse.get_pos()[0] % 255, pg.mouse.get_pos()[1] % 255, pg.mouse.get_pos()[0]*pg.mouse.get_pos()[1] % 255)

        # add squares to memory
        if pg.mouse.get_pressed()[0] and pg.mouse.get_pos() not in squares:
            squares.append(drawcenteredsquare(screen, color, pg.mouse.get_pos(), 10))

        # on right click, emtpy the list
        if pg.mouse.get_pressed()[2]:
            squares = []

        # draw all squares in the list to the screen
        for square in squares:
            pg.draw.rect(screen, square[1], square[2])

        # print the framerate and the difference between the current and the last frame
        print(clock.get_fps(), clock.get_time())

        # update screen
        pg.display.flip()

        # q: how can I make the list with squares more efficient

