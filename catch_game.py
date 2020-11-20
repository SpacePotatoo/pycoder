import pygame
pygame.init() 
from pygame import mixer 
mixer.init() 

wn = pygame.display.set_mode((863,486))
pygame.display.set_caption('game of squares') 
bgimage = pygame.image.load(r'D:\\baban\\PicVidAud\\pictures\\nebula.jpg')    

bluex = 100
bluey = 100
redx = 300
redy = 300
bluevel = 6
redvel = 5
run = True

def draw_game():
    wn.blit(bgimage, (0,0))
    pygame.draw.rect(wn, (0,0,255), (bluex,bluey,20,20))
    pygame.draw.rect(wn, (255,0,0), (redx,redy,40,40))
    pygame.display.update()
    
mixer.music.load("D:\\baban\\PicVidAud\\music\\song3.mp3") 
mixer.music.set_volume(0.7)    
mixer.music.play(-1)
   
while run:
    pygame.time.delay(90)
    
    if redx < bluex - 10:
        redx = redx + redvel
        draw_game()
        
    elif redx > bluex + 10:
        redx = redx - redvel
        draw_game()
        
    elif redy < bluey - 10:
        redy = redy + redvel
        
    elif redy > bluey + 10:
        redy = redy - redvel
        
    else:
        run = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bluex -= bluevel

    if keys[pygame.K_RIGHT]:
        bluex += bluevel
      
    if keys[pygame.K_UP]:
        bluey -= bluevel
      
    if keys[pygame.K_DOWN]:
        bluey += bluevel
      
    draw_game()

        
pygame.quit()         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        