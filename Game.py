import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 612, 389
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Basic Square Game')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load background image
background_image = pygame.image.load('ekm.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Set up initial rectangle position and speed
rect_x, rect_y = 50, 50
rect_width, rect_height = 60, 60
rect_speed_x, rect_speed_y = 5, 5

clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    # Move the square based on the keys being pressed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed_y
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed_y

    # Move the square from left to right and bounce back
    rect_x += rect_speed_x
    if rect_x + rect_width > (WIDTH -25):
        rect_x = (WIDTH-25) - rect_width
        rect_speed_x = -rect_speed_x
    if rect_x < 25:
        rect_x = 25
        rect_speed_x = -rect_speed_x

    # Bounce back from top and bottom
    if rect_y + rect_height > (HEIGHT-20):
        rect_y = (HEIGHT-20) - rect_height
        rect_speed_y = -rect_speed_y
    if rect_y < 20:
        rect_y = 20
        rect_speed_y = -rect_speed_y

    # Draw background image
    screen.blit(background_image, (0, 0))

    # Draw rectangle
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Update screen
    pygame.display.flip()

    # Time delay (60 FPS)
    clock.tick(60)