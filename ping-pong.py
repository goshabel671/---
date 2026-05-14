from pygame import *

win_back = (100, 255, 255)

win_width = 600
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_height))
window.fill((win_back))
game = True
finish = False
score1 = 0
score2 = 0
max_score = 3
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
font1 = font.Font(None, 35)

run = True
finish = False
speed_x = 2
speed_y = 2
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
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
        score_text = font1.render(str(score1) + ' : ' + str(score2), True, (0, 0, 0))
        window.blit(score_text, (200, 20))
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(pl_l, ball) or sprite.collide_rect(pl_r, ball):
        speed_x *= -1.07
    display.update()
    clock.tick(55)
