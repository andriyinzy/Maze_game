#створи гру "Лабіринт"!
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self, ) -> None:
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H-80:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < W-80:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= W-250:
            self.direction = 'right'
        if self.rect.x >= W-85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_w, wall_h):
        self.color = color
        self.width = wall_w
        self.height = wall_h
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

W,H = 700, 500
win = display.set_mode((W,H))
display.set_caption("Maze")
bg = transform.scale(image.load("background.jpg"), (W,H))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

player = Player('hero.png', 5, H-80, 65,65,4)
enemy = Enemy("cyborg.png", W-80, H-200, 65, 65, 1)
treasure = GameSprite("treasure.png", W-100, H-100, 65, 65, 0)
wall_1 = Wall((154,205,50), 100, 20, 450, 10)
wall_2 = Wall((154,205,50), 100, 20, 10, 350)
wall_3 = Wall((154,205,50), 100, 480, 350, 10)


game = True
clock = time.Clock()
FPS = 60
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    win.blit(bg, (0,0))

    player.update()
    player.reset()
    enemy.update()
    enemy.reset()
    treasure.update()
    treasure.reset()
    wall_1.draw()
    wall_2.draw()
    wall_3.draw()
    display.update()
    clock.tick(FPS)