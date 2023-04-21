from pygame import *
width = 700
height = 500
clock = time.Clock()
sprite_side = 50
win = display.set_mode((width, height))
display.set_caption('Ping-Pong')
finish = False
Game = True
FPS = 120
background = (102, 255, 102)



class GameSprite(sprite.Sprite):
    def __init__(self, rect_x, rect_y, im, speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(im), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, rect_x, rect_y, im, speed, w, h):
        super().__init__(rect_x, rect_y, im, speed, w, h)
    def update_L(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    def update_R(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
player_left = Player(65, 0, 'Stick.png', 5, 15, 100)
player_right = Player(600, 0, 'Stick.png', 5, 15, 100)


    








while Game:
    win.fill(background)
    player_left.update_L()
    player_right.update_R()
    player_left.reset()
    player_right.reset()
    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)