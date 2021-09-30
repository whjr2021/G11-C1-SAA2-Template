# Import pygame library
import pygame

# Initialize pygame
pygame.init()

# Create the game window/screen
screen = pygame.display.set_mode((400,600))

# Create a rectangle for paddle object 
paddle = pygame.Rect(150,500,100,30)

# Create a rectangle for ball object and position it on top of paddle at its center


# Game loop
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    # Draw blue colored paddle on screen
    pygame.draw.rect(screen,(23,100,100),paddle)
    
    # Draw an orange colored ball on screen 
    
    
    pygame.display.update()