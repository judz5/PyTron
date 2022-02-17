import pygame, sys, os
from pygame.locals import *
 
pygame.init()
pygame.font.init()
 
fps = 60
fpsClock = pygame.time.Clock()

p1_path = []
p2_path = []

particles = []
 
win = pygame.display.set_mode((960,640), pygame.FULLSCREEN)

mainFont = pygame.font.Font('dogicapixel.ttf', 100)
normFont = pygame.font.Font('dogicapixel.ttf', 50)

joystick = pygame.joystick.Joystick(0)
joystick.init()
joystick2 = pygame.joystick.Joystick(1)
joystick2.init()


class color():
    p1 = (64,207,255)
    p2 = (234,0,255)

class bike():
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,15,15)
        self.boost = False
        self.boostLeft = 100
    
    def update(self):
        if(self.boost and not (-10 in (self.dx, self.dy)) and not(10 in (self.dx, self.dy))):
            self.dx = self.dx * 2
            self.dy = self.dy * 2
        self.x += self.dx
        self.y += self.dy

    def drawBike(self):
        self.rect = pygame.Rect(self.x, self.y, 15, 15)
        pygame.draw.rect(win, self.color, self.rect)

def draw_text(text, font, color, surface, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=(win.get_width()/2, y))
    #textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Game loop.
def game():
    global p1_path, p2_path
    p1_path.clear()
    p2_path.clear()
    # add variables
    player_1 = bike(win.get_width()/4,win.get_height()/2, 5, 0, color.p1)
    player_2 = bike(win.get_width()-win.get_width()/4, win.get_height()/2, -5, 0, color.p2)

    check = False
        
    while True:
        win.fill((0, 0, 50))
        fpsClock.tick(60)
    
        #draw_text(str(fpsClock.get_fps()), normFont, (255,255,255),win, 100)
    
        p1_path.append(pygame.Rect(player_1.rect.centerx, player_1.rect.centery, 4, 4))
        p2_path.append(pygame.Rect(player_2.rect.centerx, player_2.rect.centery, 4, 4))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # -----------------
        
        if joystick.get_axis(1) > .5 and player_1.dy != 5:
            player_1.dy = -5
            player_1.dx = 0               
        if joystick.get_axis(1) < -.5 and player_1.dy != -5:
            player_1.dy = 5
            player_1.dx = 0
        if joystick.get_axis(0) > .5 and player_1.dx != 5:
            player_1.dx = -5
            player_1.dy = 0
        if joystick.get_axis(0) < -.5 and player_1.dx != -5:
            player_1.dx = 5
            player_1.dy = 0
            # if event.key == K_SPACE and player_1.boostLeft > 0:
            #     player_1.boost = True
            # -----------------
        if joystick2.get_axis(1) > .5 and player_2.dy != 5:
            player_2.dy = -5
            player_2.dx = 0
        if joystick2.get_axis(1) < -.5 and player_2.dy != -5:
            player_2.dy = 5
            player_2.dx = 0
        if joystick2.get_axis(0) > .5 and player_2.dx != 5:
            player_2.dx = -5
            player_2.dy = 0
        if joystick2.get_axis(0) < -.5 and player_2.dx != -5:
            player_2.dx = 5
            player_2.dy = 0
            
                # if event.key == K_RSHIFT and player_2.boostLeft>0:
                #     player_2.boost = True
                # -----------------
            # if event.type == KEYUP:
            #     if event.key == K_SPACE:
            #         player_1.boost = False
            #     if event.key == K_RSHIFT:
            #         player_2.boost = False
        
        # Update.
        player_1.update()
        player_2.update()
        
        # Draw.
        player_1.drawBike()
        player_2.drawBike()
       
        if player_1.x:
        
        
            for p in p1_path:
                pygame.draw.rect(win, color.p1, p)
       
        x = 0
        while(x<len(p1_path)):
            if(x<(len(p1_path)-5)):
                if(p1_path[x].colliderect(player_1.rect)):
                    deathScreen(False)
            if(p2_path[x].colliderect(player_1.rect)):
                deathScreen(False)
            x = x + 1

        for p in p2_path:
            pygame.draw.rect(win, color.p2, p)

        x = 0
        while(x<len(p2_path)):
            if(x<(len(p2_path)-5)):
                if(p2_path[x].colliderect(player_2.rect)):
                    deathScreen(True)
            if(p1_path[x].colliderect(player_2.rect)):
                deathScreen(True)
            x = x + 1
        

        pygame.display.update()


def menu():
    win.fill((0,0,0))

    while True:
        win.fill((0,0,50))
        fpsClock.tick(60)

        draw_text('PyTron', mainFont, color.p1, win, (win.get_height()/3)+(win.get_height()/9))
        draw_text('Press Coin To Start', normFont, color.p2, win, (win.get_height()/3)+(win.get_height()/5)+50)

        #draw_text(str(fpsClock.get_fps()), normFont, (255,255,255),win, 100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if joystick.get_button(4):
            game()
        if joystick.get_button(5):
            pygame.quit()
            sys.exit()

        pygame.display.update()
    

def deathScreen(blueWon):
    win.fill((0,0,0))
    
    while True:
        win.fill((0,0,50))
        fpsClock.tick(60)

        if(blueWon):
            draw_text('BLUE WON!', mainFont, color.p1, win, win.get_height()/2)
        else:
            draw_text('PINK WON!', mainFont, color.p2, win, win.get_height()/2)

        for event in pygame.event.get():
             if event.type == QUIT:
                 pygame.quit()
                 sys.exit()
             if event.type == KEYDOWN:
                 if event.key == K_SPACE:
                     menu()

        pygame.display.update()
        pygame.time.delay(3000)
        menu()

menu()
