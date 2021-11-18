import pygame,sys,random
from pygame.locals import *

pygame.init()
# creating screen
display_width= 800
display_height = 533
screen = pygame.display.set_mode((display_width,display_height))

#Title and Icon
pygame.display.set_caption("Not Fruit Ninja")
icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

#Background Image
background = pygame.image.load('background.png')

#fruit
appleImg= pygame.image.load('apple.png').convert()
appleX = 200
appleY = 10
fruitType = 'apple'
rect_apple = appleImg.get_rect()
rect_apple.center = display_width//2, display_height//2

#strawberry
strawberryImg = pygame.image.load('strawberry.png').convert()
strawberryX = 100
strawberryY = 5
rect_strawberry = strawberryImg.get_rect()
rect_strawberry.center = display_width//2, display_height//2
moving = False
transparent = (0,0,0,0)



class fruit:
    def _init_ (self, image, x , y, fruitType):
        self.image = image
        self.x = x
        self.y = y
        self.fruitType = fruitType

def appleDraw(self,x,y):
    screen.blit(appleImg, (x,y))

def strawberryDraw(x,y):
    screen.blit(strawberryImg,(x,y))
'''
def strawberryDraw():
    strawberryImg1 = pygame.image.load('strawberry.png').convert()
    strawberryX1 = 300
    strawberryY1 = 200
    rect_strawberry1 = strawberryImg1.get_rect()
    rect_strawberry1.center = display_width // 2, display_height // 2
   # screen.blit(strawberryImg1, strawberryX1,strawberryY1)
'''



offset = [0,0]
running = True

# Game Loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    appleY += 5
    strawberryY += 1

    '''
    #Draw Text
    text = 'Welcome'
    font = pygame.font.get_default_font()
    font1 = pygame.font.Font(font,200)
    text_surface = font1.render(text,True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.center = (20,70)
    screen.blit(text_surface,tex_rect)
    '''
    #Display Text
    text = 0
    font = pygame.font.Font('freesansbold.ttf',32)

    def displayText():
        text1 = font.render('Welcome',True, (0,0,0))
        screen.blit(text1, (display_height//2,display_width//2 ))





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        '''if event.type == MOUSEBUTTONDOWN:
            #left mouse click  
            if event.button == 1:
                appleX
            #right mouse click
            if event.button == 3:

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
        '''

        #if event.type == pygame.MOUSEBUTTONDOWN:
             #player.drag = True
        #if event.type == pygame.MOUSEBUTTONUP:
           # player.Past = []
           # player.drag = False
        if event.type == MOUSEBUTTONDOWN:
            print("Down!")
            #detects collisions - collideoint
           # if rect_strawberry.collidepoint(event.pos):
             #moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False
            #strawberryImg.fill(transparent)  # transparent / removes image
        elif event.type == MOUSEMOTION: #and moving:
            if rect_strawberry.collidepoint(event.pos):
                strawberryImg.fill(transparent)  # transparent / removes image when the oject is sliced
                #moving = True

            ####moves object to where and as the mouse moves (relative movement). - (event. rel)
           #rect_strawberry.move_ip(event.rel)



    #mouse inputs/move objects
        '''
     mouseX,mouseY = pygame.mouse.get_pos()
    # strawberry follows mouse movements
    rot = 0
    loc =[mouseX,mouseY]
    screen.blit(pygame.transform.rotate(strawberryImg,rot),(loc[0]+offset[0], loc[1] + offset[1]))
        '''


    #Displays Welcome on the screen
    displayText()


    #Draws the fruits
    '''appleDraw(appleX,appleY)'''
    strawberryDraw(strawberryX,strawberryY)
    # screen.blit(strawberryImg, rect_strawberry)

    #Draws strawberry
    screen.blit(strawberryImg, rect_strawberry)

    pygame.display.update()

