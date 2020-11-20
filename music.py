from pygame import mixer
mixer.init()

mixer.music.load("D:\\baban\\PicVidAud\\music\\song2.mp3") 
mixer.music.set_volume(0.7) 
mixer.music.play() 

while True: 
        print("Press 'p' to pause, 'r' to resume") 
        print("Press 'e' to exit the program") 
        query = input(" ") 
        if query == 'p': 
                mixer.music.pause()         
        elif query == 'r': 
                mixer.music.unpause() 
        elif query == 'e': 
                mixer.music.stop() 
                break

import pygame 
pygame.init() 

display_surface = pygame.display.set_mode((863,486)) 

pygame.display.set_caption('Image') 

bgimage = pygame.image.load(r'D:\\baban\\PicVidAud\\pictures\\nebula.jpg') 

while True :
        display_surface.blit(bgimage, (0, 0))  
        for event in pygame.event.get() : 

                if event.type == pygame.QUIT : 
                        pygame.quit() 
                        quit() 
                pygame.display.update() 
