import pygame
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
PURPLE = ( 255,   0, 255)

global x_coord,y_coord




def enter():
    
    
    
    hi=pygame.image.load("Lamboenter.png")

    screen = pygame.display.set_mode([800,600])
    def aventador(hi,x_coord, y_coord):
   
        screen.blit(hi,[x_coord,y_coord])
    
    
    

    x_coord = -10
    y_coord = 300

    damn=pygame.image.load("road.png")
    
    


    GAMELOOP = False

    clock = pygame.time.Clock()

    x_speed = 0
    y_speed = 0

    

    while not GAMELOOP:
    
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                GAMELOOP = True 
            

            if event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_LEFT:
                    x_speed =- 5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed =- 5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5

            if event.type == pygame.KEYUP:
            
                if event.key == pygame.K_LEFT:
                    x_speed=0
                elif event.key == pygame.K_RIGHT:
                    x_speed=0
                elif event.key == pygame.K_UP:
                    y_speed=0
                elif event.key == pygame.K_DOWN:
                    y_speed=0

        
        if (x_coord)>810:
            pass
            
            #right fourth
        
        
            
            
            
        


    
        x_coord = x_coord + x_speed
        y_coord = y_coord + y_speed


        screen.fill(BLACK)
        screen.blit(damn,[0,0])
        
        
        
   
    
        

        aventador(hi, x_coord, y_coord)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
pygame.mixer.init()
pygame.mixer.music.load("Rollin.mp3")
pygame.mixer.music.play(-1,0.0)

enter()

