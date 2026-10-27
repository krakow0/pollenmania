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
    grass = (46,139,87)
    
    #load the entire bee_idle spritesheet
    bee_idle = pygame.image.load("assets/Bee/Spritesheets/Bee_Idle.png").convert_alpha()
    #select column 3, row 2's sprite for our main bee
    ourBee = bee_idle.subsurface((128,64,64,64))
    #resizing the bee to 50x50 pixels
    ourBee = pygame.transform.scale(ourBee, (160,160))
    
    #rarity dictionary, which is corresponding to the values of pollen given
    rarity_type = {"common": 15, "uncommon": 25, "rare" : 50, "legendary":100} #pollen amts
    probability = {"common": 50, "uncommon": 30, "rare": 15, "legendary": 5} #probability weights
    
    #flower list
    flowers_list = [pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/TulipOUTLINED.png").convert_alpha(), #common
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/RoseOUTLINED.png").convert_alpha(), #common
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/PoppyOUTLINED.png").convert_alpha(), #common
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/OrchidOUTLINED.png").convert_alpha(), #uncommon 
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LilyOUTLINED.png").convert_alpha(), #uncommon      
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LavenderOUTLINED.png").convert_alpha(), #uncommon   
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/DaisyOUTLINED.png").convert_alpha(), #rare
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/DaffodilOUTLINED.png").convert_alpha(), #rare   
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/LilyOfTheValleyOUTLINED.png").convert_alpha(), #rare  
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/CosmoOUTLINED.png").convert_alpha(), #legendary
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/PansyOUTLINED.png").convert_alpha(),  #legendary
    pygame.image.load("assets/Bee/Flowers/Flowers_Separated/Flowers_With_Ouline/SunflowerOUTLINED.png").convert_alpha(),  # legendary
    ]
    
    flowers_odds = { #rarity corresponds to the image of the flowers in that rarity type
   "common": flowers_list[0:3],
    "uncommon": flowers_list[3:6],
    "rare": flowers_list[6:9],
    "legendary": flowers_list[9:12],    
    }
    generated_flowers = [] #this will store the randomly selected flowers
    for i in range(20): #generates (parameter) number of flowers
    # 1. selecting one rarity KEY based on probability weights
        selected_rarity = random.choices(list(probability.keys()), weights=list(probability.values()), k=1)[0]
    # 2. Select a random flower from that rarity
        selected_flower = random.choice(flowers_odds[selected_rarity]) #selecting the value based on the previously selected key
    # 3. Generate random x and y coordinates
        flowerRandx = random.randint(0, screen_width - selected_flower.get_width())
        flowerRandy = random.randint(0, screen_height - selected_flower.get_height())
    # 4. creating interaction boxes for each flower
        flowerInteractionBox = selected_flower.get_rect(topleft = (flowerRandx, flowerRandy))
        flowerInteractionBox = flowerInteractionBox.inflate(-20, -20) #keeps the box centered but makes it smaller
    # 5. Append flower information to generated_flowers (flower image, x, y, rarity_type)
        pollen_value = rarity_type[selected_rarity]
        generated_flowers.append((selected_flower, flowerRandx, flowerRandy, pollen_value, flowerInteractionBox))

    clock = pygame.time.Clock() #sets up the game clock
    
    #initializing our bee (character)
    bee_width, bee_height = 50,50
    speed = 10
    bee_x, bee_y = screen_width // 4, screen_height // 4
    
    #pollen counter
    total_pollen = 0
    collection_time = 1000 #1 second in milliseconds
    collection_start = None #stores when pollen collection began
    active_flower = None #tracks which flower you're collecting from

    while True: #main game loop, everything should be in this loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.flip() #updates display
        
        keys = pygame.key.get_pressed() #setting up the controls
        if keys[pygame.K_a]:
            bee_x -= speed
        if keys[pygame.K_d]:
            bee_x += speed
        if keys [pygame.K_w]:
            bee_y -= speed
        if keys[pygame.K_s]:
            bee_y += speed
        
        bee_rect = pygame.Rect(bee_x+60 , bee_y+45 , 80, 75)
        touching_flower = None
        #pollen collection and bee/flower collision
        for flower_data in generated_flowers:
            flower, x, y, pollen_value, flowerInteractionBox = flower_data
            if bee_rect.colliderect(flowerInteractionBox):
                touching_flower = flower_data
                break
        #check if player is holding E
        if touching_flower is not None and keys[pygame.K_e]:
            print("Collecting pollen!")
            
            #start collecting a new flower
            if active_flower is not touching_flower:
                active_flower = touching_flower
                collection_start = pygame.time.get_ticks()
             # calculate how long E has been held for
            elapsed_time = pygame.time.get_ticks() - collection_start
            print("Elapsed time:", elapsed_time)
        
            #calculate progress from 0.0 to 1.0
            progress = min(elapsed_time / collection_time, 1.0)
        
            #collection complete
            if progress >= 1.0:
                total_pollen += touching_flower[3]
                generated_flowers.remove(touching_flower)
                
                print("Total pollen:", total_pollen)
                
                active_flower = None
                collection_start = None
        else:
        #Reset if E is released or if bee moves away from flower
            active_flower = None
            collection_start = None
        
        #DRAW EVERYTHIHNG
        screen.fill(grass) #makes the screen grass colored
        
        #draw our bee on screen
        screen.blit(ourBee, (bee_x, bee_y))
        
        #draw flowers 
        for selected_flower, x, y, pollen_value, flowerInteractionBox in generated_flowers:
            screen.blit(selected_flower, (x,y))
        
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
        
main()