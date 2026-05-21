from pygame import *
import random
font.init()

win_back = (100, 255, 255)

win_width = 600
win_height = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_height))
window.fill((win_back))
game = True
finish = False
match_over = False
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
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y += self.speed
        

ball = GameSprite('tennis.png', 275, 275, 50, 50, 3)
pl_l = Player('platformleft.png', 30, 100, 50, 200, 3)
pl_r = Player('platform.png', 570, 100, 50, 200, 3)
font1 = font.Font(None, 35)

score_text1 = font1.render ('Выйграл первый игрок', True, (255, 1, 1))
score_text2 = font1.render ('Выйграл второй игрок', True, (255, 1, 1))
run = True
finish = False
speed_x = random.choice([-3, 3])
speed_y = random.choice([-3, 3])
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False



    if not finish and not match_over: #Если мач и партия не окончены
        window.fill((120, 130, 140))
        ball.update()
        ball.reset()
        pl_l.update_l()
        pl_l.reset()
        pl_r.update_r()
        pl_r.reset()
        ball.rect.x += speed_x 
        ball.rect.y += speed_y
    elif finish and not match_over:
         window.fill(back)
         ball.rect.y = 275
         ball.rect.x = 275
         pl_l.rect.y = 100
         pl_r.rect.y = 100
         ball.reset()
         pl_l.reset()
         pl_r.reset()
         display.update()
         time.wait(2000)
         finish = False
         speed_x = random.randint([-3, 3])
         speed_y = random.choice([-3, 3])

    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(pl_l, ball) or sprite.collide_rect(pl_r, ball):
        speed_x *= -1.07
    '''if ball.rect.x > 550:
        speed_x *= -1
    if ball.rect.x < 50:
        speed_x *= -1'''
    if ball.rect.x <= 0:
        score2 += 1
        finish = True
    if ball.rect.x >= 560:
        score1 += 1
        finish = True
    if score1 == max_score or score2 == max_score:
        match_over = True
    if score1 == 3:
        window.blit(score_text1, (100, 230))
    if score2 == 3:
        window.blit(score_text2, (100, 230))
    score_text = font1.render(str(score1) + ' : ' + str(score2), True, (0, 0, 0))
    window.blit(score_text, (280, 20))

    
    
    if score1 == 3:
        window.blit(score_text1, (100, 230))
    if score2 == 3:
        window.blit(score_text2, (100, 230))
    score_text = font1.render(str(score1) + ' : ' + str(score2), True, (0, 0, 0))
    window.blit(score_text, (280, 20))

        
    display.update()
    clock.tick(55)

    
