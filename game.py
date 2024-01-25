import pygame

pygame.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Tạo cửa sổ game
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Hero War')

# Xây dựng kịch bản game
    # player
player = pygame.image.load('img/player.png')
player = pygame.transform.scale(player,(100, 50))
player_rect = player.get_rect()
player_rect.x = 0
player_rect.y = SCREEN_HEIGHT/2
speed = 2
    # bullet
bullet = pygame.image.load('img/bullet.png')
bullet = pygame.transform.scale(bullet, (80,30))
bullet_rect = bullet.get_rect()
bullet_rect.x = 100
bullet_rect.y = 100
speed_bullet = 1
    # gem
gem = pygame.image.load('img/gem.png')
gem = pygame.transform.scale(gem,(90, 50))
gem_rect = gem.get_rect()
gem_rect.x = 300
gem_rect.y = 300
# score: surface text
f_game = pygame.font.Font('./fonts/font_game.otf', 32)
score = 0
score_title = f_game.render(f'Score {score}', True, 'Red', 'White')
score_title_rect = score_title.get_rect()
score_title_rect.x = SCREEN_WIDTH - score_title.get_width() - 10
score_title_rect.y = 10
# background
bg = pygame.image.load('./img/bg_game.jpg')
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Thiết lập vòng lặp game
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        # Xử lý bắn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect.x = player_rect.x
                bullet_rect.y = player_rect.y
    # Kịch bản game
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and player_rect.y > 50:
        player_rect.y -= speed
    elif key[pygame.K_DOWN] and player_rect.y < SCREEN_HEIGHT - player_rect.height:
        player_rect.y += speed
    if key[pygame.K_LEFT] and player_rect.x > 0:
        player_rect.x -= speed
    elif key[pygame.K_RIGHT] and player_rect.x < SCREEN_WIDTH - player_rect.width:
        player_rect.x += speed
    # Xử lý đạn
    bullet_rect.x += speed_bullet
    # screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(player, player_rect)
    screen.blit(bullet, bullet_rect)
    screen.blit(gem, gem_rect)
    # score
    score_title
    screen.blit(score_title, (score_title_rect))
    # Cập nhật game
    pygame.display.flip()

pygame.quit()