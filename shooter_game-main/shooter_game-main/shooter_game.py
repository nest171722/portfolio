#Create your own shooter
from pygame import *
from random import *
from time import time as timer

win_width = 700
win_height = 500
mixer.init()
mixer.music.load("fire.ogg")
mixer.music.load("space.ogg")
mixer_music.play()
fire_sound = mixer.Sound("fire.ogg")
score = 0
miss = 0
life = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    
    def show(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width-80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png',self.rect.centerx,self.rect.top,15,20,16)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        global miss
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(1,600)
            self.rect.y = 25 #respawn
            miss = miss + 1

class Object(GameSprite):
    def update(self):
        global miss
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(1,600)
            self.rect.y = 25 #respawn
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

font.init()
font_title = font.SysFont(None,70)
font2 = font.SysFont(None,70)


window = display.set_mode((win_width,win_height))
display.set_caption("galaxy")
background = transform.scale(image.load("galaxy.jpg"),(win_width,win_height))
game = True
finish = False

ufos = sprite.Group()
asteroids = sprite.Group()
for i in range(5):
    ufo = Enemy('ufo.png',randint(1,600),25,80,50,randint(1,3))
    ufos.add(ufo)
for i in range(2):
    asteroid = Object('asteroid.png',randint(1,600),25,80,50,randint(1,3))
    asteroids.add(asteroid)

bullets = sprite.Group()

rocket = Player('rocket.png',0,400,80,100,13)
# ufo = Enemy('ufo.png',randint(1,600),25,randint(1,3))


run = True

rel_time = False

num_fire = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    fire_sound.play()
                    rocket. fire()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True

    if not finish:
        window.blit(background,(0,0))
        
        rocket.update()
        # ufo.update()
        rocket.show()
        # ufo.show()
        ufos.draw(window)
        ufos.update()
        asteroids.draw(window)
        asteroids.update()
        bullets.draw(window)
        bullets.update()

        if rel_time == True:
            now_time = timer()

            if now_time - last_time < 3:
                reload = font2.render('Wait,reload...',1,(150,0,0))
                window.blit(reload, (260,460))
            else:
                num_fire = 0
                rel_time = False

        collides = sprite.groupcollide(ufos, bullets, True,True )
        for c in collides:
            score = score + 1
            ufo = Enemy('ufo.png',randint(1,600),25,80,50,randint(1,3))
            ufos.add(ufo)
        
        if sprite.spritecollide(rocket, ufos, False) or sprite.spritecollide(rocket, asteroids,False):
            sprite.spritecollide(rocket, ufos, True)
            sprite.spritecollide(rocket, asteroids,True)
            life -= 1

        
        if score == 10:
            finish = True
            won_text = font_title.render('YOU WON!',True,(0,100,0))
            window.blit(won_text,(175,250))
        elif miss >= 5:
            finish = True
            lose_text = font_title.render('YOU LOSE',True,(100,0,0))
            window.blit(lose_text,(175,250))
        elif life == 0 :
            finish = True
            lose_text = font_title.render('YOU LOSE',True,(100,0,0))
            window.blit(lose_text,(175,250))
        win_text = font_title.render('miss : ' + str(miss),True,(0, 0,100))
        lose_text = font_title.render('score : ' + str(score),True,(0, 0,100))

        if life == 3:
            color_life = (0,100,0)

        elif life == 2:
            color_life = (50,60,0)

        elif life == 1:
            color_life = (100,0,0)


        life_text = font_title.render('life : ' + str(life),True,(color_life))
        window.blit(win_text,(0,50))

        window.blit(lose_text,(0,10))

        window.blit(life_text,(550,50))
        display.update()

    else:
        finish = False
        score = 0 
        miss = 0
        life = 3
        for i in ufos: 
            i.kill()
        for i in bullets:
            i.kill()
        for i in asteroids:
            i.kill()
        for i in range(5):
            ufo = Enemy('ufo.png',randint(1,600),25,80,50,randint(1,3))
            ufos.add(ufo)
        for i in range(2):
            asteroid = Object('asteroid.png',randint(1,600),25,80,50,randint(1,3))
            asteroids.add(asteroid)
        time.delay(5000)
        

          
        
    time.delay(50)
        #if sprite.collide_rect(rocket, rock) or sprite.spritecollideany()