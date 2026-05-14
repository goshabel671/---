from pygame import *

win_back = (100, 255, 255)

win_width = 600
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_height))
window.fill((win_back))
clock = time.Clock()
img_playr = 'tennis.png'
img_pltfr = 'platform.png'
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y > 5:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        

ball = GameSprite('tennis.png', 275, 275, 50, 50, 3)
pl_l = Player('platform.png', 30, 100, 30, 350, 3)
pl_r = Player('platform.png', 570, 100, 30, 350, 3)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill((120, 130, 140))
        ball.update()
        ball.reset()
        pl_l.update_l()
        pl_l.reset()
        pl_r.update_r()
        pl_r.reset()
    display.update()
    clock.tick(55)
