from pygame import *

# GameSprite class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (weight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# Player class
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


# Scene setup
back = (122, 213, 221)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

# Start game
game = True
finish = False
clock = time.Clock()
FPS = 60

# Create sprites
player1 = Player('racket.png', 30, 200, 4, 50, 150)
player2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)

# Initialize font
font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 Lose", True, (180, 0, 0))
lose2 = font.render("Player 2 Lose", True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)
        player1.update_l()
        player2.update_r()
        
        # Update ball position
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # Ball collision with paddles
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        # Ball collision with top and bottom
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        # Ball out of bounds
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

    player1.reset()
    player2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)