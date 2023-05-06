import pygame
w = 750
h = 550
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Pin-Pong")
background = pygame.transform.scale(pygame.image.load("background.jpg"),(w,h))
class GameSprite(sprite.Sprite):
    def __init__ (self, width, height, player_image,player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image),(width,height))
        self.speed = player_speed
        self.rect = self.image.get_rect() # Створити рамку навколо картинки спрайта
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self): # Функція для того щоб намалювати спрайт на екрані
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y <= 600:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x <= 600:
            self.rect.x += self.speed
game = True
finish = False
clock = time.Clock()
FPS = 80

racket1 = Player('mishka_player.jpg', 5, 50, 10)
racket2 = Player('monster_player.jpg', 5, 50, 10)
ball = ('photo.jpg', 5, 50, 10)

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x +=  speed_x 
        ball.rect.y += speed_y

        if sprite.colide_rect(racket1, ball) or colide_rect(racket2, ball):
            speed_x *= -1
            speed_y = 1

        
        if ball.rect.x < 0:
            finish = True
            window.blit (lose1, (200, 200))
            game_over = True

        racket1.reset()
        racket1.reset()
        racket1.reset()

        if finish != True:
            window.fill(back)
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.x += speed_x
            
            if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
                speed_x *= 1

            if ball.rect.y > win_height-50 or ball.rect.y < 0:
                speed y *= -1
                speed y *= 1

            if ball.rect.x < 0:
                finish = True
                window.blit(lose1, (200, 200))
                game_over = True

            if win_height, win_width:
                finish = True
                window.blit(lose2, (200, 200))
                game_over = True

            racket1.reset()
            racket1.reset()
            racket1.reset()















            


