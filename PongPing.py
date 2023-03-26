from pygame import * 
from random import randint
from time import time  as timer
back = (200, 255, 255)
win_width = 600
win_height = 500 
window = display.set_mode((win_width, win_height))
window.fill(back)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x = 65, size_y = 65):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
clock = time.Clock()
FPS = 60
Game = True
rocket = Player("ufo.png",50,450, 5)
rocket2 = Player2("ufo.png",450,450, 5)
Ball = GameSprite("asteroid.png", 250, 250, 5)
speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 Loses', True, (180, 0 , 0))
lose2 = font1.render('Player 2 Loses', True, (180, 0 , 0))

finish = False
while Game:
    for e in event.get():
        if e.type == QUIT:
            Game = False
    
    window.fill(back)
    rocket.reset()
    rocket.update()
    rocket2.reset()
    rocket2.update()
    Ball.reset()
    if finish != True:
        Ball.rect.x += speed_x
        Ball.rect.y += speed_y
    
    if Ball.rect.y > win_height-50 or Ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(rocket, Ball) or sprite.collide_rect(rocket2, Ball):
        speed_x *= -1

    if Ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))

    if Ball.rect.x > 550:
        finish = True
        window.blit(lose2, (200, 200))
    
    display.update()
    clock.tick(FPS) 

