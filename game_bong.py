from cgi import test
import pygame
from sys import exit
import random

pygame.init()

# The size of the game's window
width = 1280
height = 720


#all our objects

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bong bong")
clock = pygame.time.Clock()
score_number = 0

font = pygame.font.Font("C:\\Users\\love-\\Documents\\grand9k_pixel\\Grand9K Pixel.ttf", 50)


loading_screen = pygame.image.load("C:\\Users\\love-\\Pictures\\[アパタイト] ボクと奥さんの発情交尾日記～家庭教師は隣の美人妻～\\163_cmnbg9900.png").convert_alpha()

start_button = font.render("Start", True, "White")
start_button_rectangle = start_button.get_rect(midtop = (width/2, 200))

dead = font.render("Game Over", True, "White" )
dead_rectangle = dead.get_rect(center = (width/2, height/2))

#quit_button = font.render("Quit", True, "White")
#quit_button_rectangle = quit_button.get_rect(midtop = (width/2, 800))

kirby = pygame.image.load("C:\\Users\\love-\\Pictures\\pixil-frame-0.png").convert_alpha()
kirby = pygame.transform.scale(kirby, (100, 100))
kirby_rectangle = kirby.get_rect(topleft = (200, 500))  

pipe = pygame.image.load("C:\\Users\\love-\\Documents\\pipe-pixel-art.png").convert_alpha()
pipe = pygame.transform.scale(pipe, (200, 600))
pipe_rectangle = pipe.get_rect(bottomright = (1280, 1000))


  
#kirby's position


#pipe's position
pipe_x_pos = 800
pipe_y_pos_possible = [620, 520, 420, 320, 220]

def game():
    kirby_gravity = 0
    score_number = 0
    mouse_pos = pygame.mouse.get_pos()
    game_active = True
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #if event.type == pygame.MOUSEMOTION:
            #    print(event.pos)

            # Player's movement
            if event.type == (pygame.KEYUP or pygame.K_w or pygame.K_SPACE):
                kirby_gravity  = -10
            if event.type == kirby_rectangle.collidepoint(mouse_pos):
                if event.type == pygame.mouse.get_pressed():
                    kirby_gravity = -10
            # Player's collisions
            #if event.type == kirby_rectangle.contains(pipe_rectangle):
                
                #With the floor
            if event.type == kirby_rectangle.bottom > 720:
                pygame.quit()
                quit()

        if game_active:
            #Show the surface
            screen.blit(loading_screen,(0,0))


            #Button
            screen.blit(start_button, start_button_rectangle)
            #if start_button_rectangle.collidepoint(mouse_pos):
            #    print(pygame.mouse.get_pressed())

            #screen.blit(quit_button, start_button_rectangle)  

            #Score
            score = font.render(f"Score: {score_number}", True, "White")
            score_rectangle = score.get_rect(center = (1100, 20))
            screen.blit(score, score_rectangle)

            
            
            #Kirby

                #Falling
            kirby_gravity +=1
            kirby_rectangle.bottom += kirby_gravity
            screen.blit(kirby, kirby_rectangle)
            #print(screen.blit(kirby, kirby_rectangle))


            #Pipes
            pipe_rectangle.left -= 6
            screen.blit(pipe, pipe_rectangle)
            if pipe_rectangle.left < 0:
                score_number += 1
                pipe_rectangle.x = 1280
                pipe_rectangle.y = random.choice(pipe_y_pos_possible)
                print(score_number)
                
            #Collisions 
            if kirby_rectangle.colliderect(pipe_rectangle) or kirby_rectangle.y > 750 or kirby_rectangle.bottom < 0:
                game_active = False
            
        else:
            screen.blit(loading_screen,(0,0))
            screen.blit(dead, dead_rectangle)

        

        



        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]:
            #print("jump")

            

    
        pygame.display.update()
        clock.tick(60)

game()