import pygame
import time

pygame.init()

# Creating the window and naming the game
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Breakout")

# Drawing the objects
drawGroup = pygame.sprite.Group()

edge = pygame.sprite.Sprite(drawGroup)
paddle = pygame.sprite.Sprite(drawGroup)
ball = pygame.sprite.Sprite(drawGroup)


def draw_objects(obj, w, h, x, y, data):
    obj.image = pygame.image.load(data)
    obj.image = pygame.transform.scale(obj.image, [w, h])
    obj.rect = pygame.Rect(x, y, 0, 0)


def hud_draw(x, y, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(f"{score}", True, (255, 255, 255), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)


draw_objects(edge, 600, 900, 7, 0, "data/Edge.png")
draw_objects(paddle, 40, 60, 270, 700, "data/Paddle.png")
draw_objects(ball, 8, 8, 298, 700, "data/Ball.png")

# Drawing the bricks
colors = ['YellowBrick', 'YellowBrick', 'GreenBrick', 'GreenBrick',
          'OrangeBrick', 'OrangeBrick', 'RedBrick', 'RedBrick']
bricks_count = []
x_pos = []
y_pos = []
y = 300

for i in range(8):
    y = y - 15
    x = 34
    for j in range(12):
        brick = pygame.sprite.Sprite(drawGroup)
        brick.image = pygame.image.load(f"data/{colors[i]}.png")
        brick.image = pygame.transform.scale(brick.image, [40, 11])
        brick.rect = pygame.Rect(x, y, 0, 0)
        x_pos.append(x)
        y_pos.append(y)
        bricks_count.append(brick)

        x = x + 45
print(x_pos)
print(y_pos)
print(bricks_count)

# Initial scores

birth_score = 1
brick_score = 0

# Initial ball coordinates
ball_dx = 4
ball_dy = 4

# Game looping
game_loop = True

while game_loop:

    for event in pygame.event.get():

        # Command to close the game
        if event.type == pygame.QUIT:
            game_loop = False

    # Paddle moves
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if paddle.rect.x == 514:
            paddle.rect.x = 514
        else:
            paddle.rect.x += 4
    if keys[pygame.K_LEFT]:
        if paddle.rect.x == 26:
            paddle.rect.x = 26
        else:
            paddle.rect.x -= 4

    # Ball movement
    ball.rect.x += ball_dx
    ball.rect.y -= ball_dy

    # Collision with the right wall
    if ball.rect.x >= 565:
        ball_dx *= -1

    # Collision with the left wall
    if ball.rect.x <= 25:
        ball_dx *= -1

    # Collision with the roof
    if ball.rect.y <= 15:
        ball_dy *= -1

    # Collision with the paddle
    if ball.rect.y == paddle.rect.y and paddle.rect.x + 40 > ball.rect.x > paddle.rect.x - 30:
        ball_dy *= -1

    # Collision with the floor
    if ball.rect.y > paddle.rect.y + 100:
        time.sleep(2)
        ball.rect.y = paddle.rect.y - 400
        ball.rect.x = 300
        paddle.rect.x = 270
        birth_score += 1

    # Collision with the brick
    if birth_score <= 4:
        for brick in bricks_count:
            if ball.rect.y < brick.rect.y - 10 and brick.rect.x + 20 > ball.rect.x > brick.rect.x - 20:
                brick.rect = pygame.Rect(1000, 1000, 0, 0)
                ball_dy *= -1
                brick_score += 1

    if birth_score > 4:
        paddle.rect.x = -35
        paddle.image = pygame.transform.scale(paddle.image, [655, 60])

        for brick in bricks_count:
            if ball.rect.y < brick.rect.y + 25 and brick.rect.x + 20 > ball.rect.x > brick.rect.x - 20:
                ball_dy *= -1

        if ball.rect.y == 700:
            ball_dy *= -1

    screen.fill([0, 0, 0])

    # Draw Hud
    drawGroup.draw(screen)
    hud_draw(80, 60, '000')
    hud_draw(110, 100, brick_score)
    hud_draw(440, 60, birth_score)
    hud_draw(470, 100, '000')

    # Display update
    pygame.display.update()
