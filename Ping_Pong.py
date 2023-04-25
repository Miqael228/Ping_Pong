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
class Ball(GameSprite):
    def __init__(self, rect_x, rect_y, im, speed, w, h):
        super().__init__(rect_x, rect_y, im, speed, w, h)
        self.speed_x = speed
        self.speed_y = speed

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        




ball = Ball(350, 250, 'Ball.png', 2, sprite_side, sprite_side)
player_left = Player(65, 0, 'Stick.png', 3, 15, 100)
player_right = Player(600, 0, 'Stick.png', 3, 15, 100)



    








while Game:
    win.fill(background)
    player_left.update_L()
    player_right.update_R()
    player_left.reset()
    player_right.reset()
    ball.update()
    ball.reset()
    if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
        ball.speed_x *= -1
        ball.speed_y *= 1
    if ball.rect.y > height - sprite_side or ball.rect.y < 0:
        ball.speed_y *= -1


    for e in event.get():
        if e.type == QUIT:
            Game = False
    display.update()
    clock.tick(FPS)
