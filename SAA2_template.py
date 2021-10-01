# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object and position it on top of paddle at its center
paddle = 

# Create a rectangle for ball object
ball = 

while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    # Draw red colored paddle on screen
    pygame.draw.rect(                     )
    
    # Draw the blue colored ball on screen
    pygame.draw.rect(                     )
    
    # Update the display with paddle and ball objects
    pygame.display.update()