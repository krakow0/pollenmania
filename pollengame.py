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
    grass = (46,139,87)
    
    
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
        
        #flower generation
        flowers_list = [
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/TulipOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/SunflowerOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/RoseOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/PoppyOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/PansyOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/OrchidOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LilyOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LilyOfTheValleyOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LavenderOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/DaisyOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/DaffodilOUTLINED.png").convert_alpha(),
            pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/CosmoOUTLINED.png").convert_alpha(),
                ]
        screen.fill(grass) #makes the screen lightblue
        
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
        
        #keeping the character inside the screen's bounds (collisions)
        #Collision offsets
        left_offset = 60 #orig = 80
        right_offset = -60 # orig = -40
        top_offset = 45 # orig = 60
        bottom_offset = -40 # orig = no value
        
        #Left boundary
        if bee_x + left_offset < 0:
            bee_x = -left_offset
        #Right boundary
        if bee_x + bee_width - right_offset > screen_width:
            bee_x = screen_width - bee_width + right_offset
        #Top Boundary
        if bee_y + top_offset < 0:
            bee_y = -top_offset
        #Bottom boundary
        if bee_y + bee_height - bottom_offset > screen_height:
            bee_y = screen_height - bee_height + bottom_offset
        
        random_flower = random.choice(flowers_list)
        screen.blit(random_flower, (50,50))
        pygame.display.flip()
        
        

main()