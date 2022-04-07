import pygame

import sys

pygame.init()

res = (720, 720)

screen = pygame.display.set_mode(res)

# white color
color = (0, 0, 0)

# light shade of the button
color_light = (51, 153, 255)

# dark shade of the button
color_dark = (0, 100, 255)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a ex written in
# this font
ex = smallfont.render('Exit', True, color)
play = smallfont.render('Play', True, color)
ab = smallfont.render('About us', True, color)


while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

            if width / 4 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                import main
                # fills the screen with a color
    screen.fill((0, 153, 153))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 150, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 150, 40])



    if width / 4 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 4, 150, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 4, 150, 40])



    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2, height / 3, 150, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 3, 150, 40])

        # superimposing the ex onto our button
    screen.blit(ex, (width / 2 + 45, height / 2))
    screen.blit(play, (width / 2 + 48, height / 4))
    screen.blit(ab, (width / 2 + 15, height / 3))

    # updates the frames of the game
    pygame.display.update()
