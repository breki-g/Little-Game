# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
man_position = [640, 600] # Man position
man_speed = 5  # Speed of man

def man():
    # Draw an ellipse: pygame.draw.ellipse(surface, color, (x, y, width, height))
    pygame.draw.ellipse(screen, "white", (man_position[0]-25, man_position[1]+25, 50, 100))  # Body
    # Draw a circle: pygame.draw.circle(surface, color, (center_x, center_y), radius)
    pygame.draw.circle(screen, "white", (man_position[0], man_position[1]), 30) # Head
    pygame.draw.circle(screen, "black", (man_position[0], man_position[1]), 26)
    

    
def level():
    # Draw a line: pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), width)
    pygame.draw.line(screen, "white", (0, 720), (1280, 720), 5)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if man_position[0] > 10:
            man_position[0] -= man_speed

    if keys[pygame.K_RIGHT]:
        if man_position[0] < 1270: 
            man_position[0] += man_speed
        
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    level()
    man()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()