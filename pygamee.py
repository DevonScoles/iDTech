import pygame, sys

#always initialize pygame's internal variables first
pygame.init()

#set up screen size variable
size = width, height = 640,480

#initialize window with screen size that was set before
screen = pygame.display.set_mode(size)

#clock is used to control fps
clock = pygame.time.Clock()

#variables to store location and size to draw
shape_position = (width / 2, height / 2)
shape_size = (100,100)

#pygame.Rect variable for the shape:
shape_Rect = pygame.Rect(shape_position,shape_size)

#RGB colors for drawing
shape_color = (188, 58, 0)
line_color = (128, 0, 0)
circle_color = (255,192,203)

# Circle
circle_pos = (50,50)

while True:
    # tick forward at 60 frames per second
    clock.tick(60)

    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            sys.exit()
        # pygame.MOUSEBUTTONDOWN occurs when the user clicks any mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Events will include what button was pushed, which you can check in if statements
            if event.button == pygame.BUTTON_LEFT:
                # if it was a left click, get the clicked position and move our rectangle there
                shape_Rect.center = event.pos
            elif event.button == pygame.BUTTON_RIGHT:
                # if it was a right click, get the clicked position and move the circle there
                circle_pos = event.pos

        # if event.type == pygame.KEYDOWN:
        #     # KEYDOWN happens when a keyboard key is pressed. You can check the key with event.key.
        #     if event.key == pygame.K_SPACE:
        #         # if spacebar is pressed, move some colors around
        #         shape_color_original = shape_color
        #         shape_color = circle_color
        #         circle_color = line_color
        #         line_color = shape_color_original

    # Fill the screen with a solid color
    screen.fill((50,50,30))

    # Fill a rectangular area with the shape color. This is the fastest way to draw rectangles to the screen.
    screen.fill(shape_color, rect = shape_Rect)

    # If you need more complex shapes or lines use pygame.draw.

    # Draws a circle on the given surface, color, position, and radius.
    pygame.draw.circle(screen, circle_color, circle_pos, 25)

    # Draws a line on the given surface, color, start position, end position, and line width in pixels.
    # This draws a line between the two shapes
    pygame.draw.line(screen, line_color, circle_pos, shape_Rect.center, 8)
  
    # At the end of each game loop, call pygame.display.flip() to update the screen with what you drew.
    pygame.display.flip()