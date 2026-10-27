import random
import pygame
import sys

def main():
    pygame.init() #initializing game
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height)) #setting up the window
    pygame.display.set_caption("Pollenmania")

    #defined colors
    lightblue = (105,203,255)
    black = (0,0,0)
    yellow = (255,220,67)
    
    
    clock = pygame.time.Clock() #sets up the game clock
    
    #initializing our bee (character)
    bee_width, bee_height = 50,50
    speed = 10
    bee_x, bee_y = screen_width // 4, screen_height // 4
    
    while True: #main game loop, everything should be in this loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip() #updates display
        clock.tick(60) #sets up the FPS
        
        keys = pygame.key.get_pressed() #setting up the controls
        if keys[pygame.K_a]:
            bee_x -= speed
        if keys[pygame.K_d]:
            bee_x += speed
        if keys [pygame.K_w]:
            bee_y -= speed
        if keys[pygame.K_s]:
            bee_y += speed
        
        screen.fill(lightblue) #makes the screen lightblue
        
        #load the entire bee_idle spritesheet
        bee_idle = pygame.image.load("assets/Bee/Spritesheets/Bee_Idle.png").convert_alpha()
        
        # select column 3, row 2's sprite for our main bee
        ourBee = bee_idle.subsurface((128,64,64,64))
        
        #resizing the bee to 50x50 pixels
        ourBee = pygame.transform.scale(ourBee, (160,160))
        
        #draw our bee on screen
        screen.blit(ourBee, (bee_x, bee_y))
        
        #update display
        pygame.display.flip()
        clock.tick(30)
        
        #keeping the character inside the screen's bounds
        if bee_x < 0:
            bee_x = 0
        if bee_x > screen_width - bee_width:
            bee_x = screen_width - bee_width
        if bee_y < 0:
            bee_y = 0
        if bee_y > screen_height - bee_height:
            bee_y = screen_height - bee_height
            

main()