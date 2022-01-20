import pygame, sys, os
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

p1_path = []
p2_path = []
 
win = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

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
    
    def update(self):
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
        win.fill((0, 0, 0))
    
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
                if event.key == K_w and player_1.dy == 0:
                    player_1.dy = -5
                    player_1.dx = 0               
                if event.key == K_s and player_1.dy == 0:
                    player_1.dy = 5
                    player_1.dx = 0
                if event.key == K_a and player_1.dx == 0:
                    player_1.dx = -5
                    player_1.dy = 0
                if event.key == K_d and player_1.dx == 0:
                    player_1.dx = 5
                    player_1.dy = 0
                # -----------------
                if event.key == K_UP and player_2.dy == 0:
                    player_2.dy = -5
                    player_2.dx = 0
                if event.key == K_DOWN and player_2.dy == 0:
                    player_2.dy = 5
                    player_2.dx = 0
                if event.key == K_LEFT and player_2.dx == 0:
                    player_2.dx = -5
                    player_2.dy = 0
                if event.key == K_RIGHT and player_2.dx == 0:
                    player_2.dx = 5
                    player_2.dy = 0
                # -----------------
        
        # Update.
        player_1.update()
        player_2.update()
        
        # Draw.
        player_1.drawBike()
        player_2.drawBike()
        
        for p in p1_path:
            pygame.draw.rect(win, color.p1, p)
       
        x = 0
        while(x<len(p1_path)):
            if(x<(len(p1_path)-5)):
                if(p1_path[x].colliderect(player_1.rect)):
                    print("Blue hit self")
                    pygame.quit()
                    sys.exit()
            if(p2_path[x].colliderect(player_1.rect)):
                print("Blue hit pink")
                pygame.quit()
                sys.exit()
            x = x + 1

        for p in p2_path:
            pygame.draw.rect(win, color.p2, p)

        x = 0
        while(x<len(p2_path)):
            if(x<(len(p2_path)-5)):
                if(p2_path[x].colliderect(player_2.rect)):
                    print("pink hit self")
                    pygame.quit()
                    sys.exit()
            if(p1_path[x].colliderect(player_2.rect)):
                print("pink hit blue")
                pygame.quit()
                sys.exit()
            x = x + 1

        pygame.display.flip()
        fpsClock.tick(fps)

class Button():
    def __init__(self, height, width, y, text):
        self.height = height
        self.width = width
        self.y = y
        self.rect = pygame.Rect(250-(self.width/2), self.y, self.width, self.height)
        self.text = text
        self.color = (255,255,255)

    def draw_button(self):
        pygame.draw.rect(win, self.color, self.rect)

    def add_text(self):
        draw_text(self.text, button_Font, (0,0,0), win, self.rect.centery)

def menu():
    win.fill((0,0,0))

    while True:
        


game()
