import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pixel Grid")

pygame.draw.circle(screen,(0,0,255),(50,100),10)
pygame.display.flip()
# Define grid parameters
grid_size = 10  # Size of each grid cell
grid_width = screen_width // grid_size
grid_height = screen_height // grid_size

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the grid
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(screen, WHITE, (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(screen, WHITE, (0, y), (screen_width, y))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
