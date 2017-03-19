import pygame



BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
BLUE   = (   0,   0, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
PURPLE = ( 255,   0, 255)

global x_coord,y_coord




def exit1():
    
    
    
    hi=pygame.image.load("Lambo.gif")

    screen = pygame.display.set_mode([800,600])
    def aventador(hi,x_coord, y_coord):
   
        screen.blit(hi,[x_coord,y_coord])
    
    
    

    x_coord = 780
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
            
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:
            pygame.transform.rotate(hi,-55)
            y_coord-=5
        if key[pygame.K_DOWN]:
            pygame.transform.rotate(hi,55)
            y_coord+=5
        if key[pygame.K_RIGHT]:
            x_coord+=5
        if key[pygame.K_LEFT]:
            x_coord-=5
            

        
        if (x_coord)<-30:
            import os
            os._exit(0)
            
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
pygame.mixer.music.play(1,0.0)
exit1()
