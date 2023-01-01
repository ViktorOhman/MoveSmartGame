import pygame

pygame.init()
#Initialize pygame and make the window
pygame.display.set_caption("PYwindow")
screen = pygame.display.set_mode((600,600))
#Setup some general varibles
xpos = 0
ypos = 0
enemy_pos = [(0,0)] #This one is really interesting
death = False
count = 0
#Setup the assets
bg_img = pygame.image.load('assets/600x600grid.png')
enemy_img = pygame.image.load('assets/Enemy.png')
plr_img = pygame.image.load('assets/PLR.png')
lose_img = pygame.image.load('assets/lose_screen.png')
win_img = pygame.image.load('assets/win_screen.png')
win_img.set_alpha(200)
lose_img.set_alpha(200)
#Make a function for checking if the player has collided with an enemy
def checkPos(xpos,ypos,enemy_pos):
    for enmy_spwnposT in enemy_pos:
        enmy_posx, enmy_posy = enmy_spwnposT
        if (xpos == enmy_posx and ypos == enmy_posy):
            return True
    return False
#MMMMMMMHHHHH Main loop
while True:
    for event in pygame.event.get():
        #Make sure we can close the window
        if event.type == pygame.QUIT:
            pygame.quit()
        #Check for input ad move the player accordingly
        if event.type == pygame.KEYDOWN:
            count+=1#<- btw i dont know how this actually works it just does
            if event.key == pygame.K_KP2 and ypos+180 <= 540 and death == False:
                ypos += 180  
                death = checkPos(xpos,ypos,enemy_pos)

            if event.key == pygame.K_KP8 and ypos-180 >= 0 and death == False:
                ypos -= 180
                death = checkPos(xpos,ypos,enemy_pos)

            if event.key == pygame.K_KP4 and xpos-180 >= 0 and death == False:
                xpos -= 180
                death = checkPos(xpos,ypos,enemy_pos)

            if event.key == pygame.K_KP6 and xpos+180 <= 540 and death == False:
                xpos += 180
                death = checkPos(xpos,ypos,enemy_pos)

            if event.key == pygame.K_KP9 and xpos+120 <= 540 and ypos-120 >= 0 and death == False:
                xpos += 120  
                ypos -= 120
                death = checkPos(xpos,ypos,enemy_pos)
 
            if event.key == pygame.K_KP3 and xpos+120 <= 540 and ypos+120 <= 540 and death == False:
                xpos += 120
                ypos += 120
                death = checkPos(xpos,ypos,enemy_pos)
                
            if event.key == pygame.K_KP1 and xpos-120 >= 0 and ypos+120 <= 540 and death == False:
                xpos -= 120
                ypos += 120
                death = checkPos(xpos,ypos,enemy_pos)
                
            if event.key == pygame.K_KP7 and xpos-120 >= 0 and ypos-120 >= 0 and death == False:
                xpos -= 120
                ypos -= 120
                death = checkPos(xpos,ypos,enemy_pos)
        enemy_pos.append((xpos,ypos)) #Add the new enemy that appears behind us to the position list
    
    screen.blit(bg_img, (0,0))
    #Show the enemies
    for enmy_spwnposT in enemy_pos:
        enmy_posx, enmy_posy = enmy_spwnposT
        screen.blit(enemy_img,(enmy_posx,enmy_posy))
    #Death screen
    if death == True:
        screen.blit(lose_img,(0,100))
        screen.blit(plr_img,(xpos,ypos))
    #Win screen :D
    elif count == 100:
        screen.blit(win_img,(0,100))
        screen.blit(plr_img,(xpos,ypos))
    else:
        screen.blit(plr_img,(xpos,ypos))

    pygame.display.flip()
