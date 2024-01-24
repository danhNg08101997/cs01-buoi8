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
player_rect.y = 0
    # bullet
bullet = pygame.image.load('img/bullet.png')
bullet = pygame.transform.scale(bullet, (80,30))
bullet_rect = bullet.get_rect()
bullet_rect.x = 100
bullet_rect.y = 100
    # gem
gem = pygame.image.load('img/gem.png')
gem = pygame.transform.scale(gem,(90, 50))
gem_rect = gem.get_rect()
gem_rect.x = 0
gem_rect.y = 0 

# Thiết lập vòng lặp game
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    # Kịch bản game
    screen.fill((255,255,255))
    screen.blit(player, player_rect)
    screen.blit(bullet, bullet_rect)
    # Cập nhật game
    pygame.display.flip()

pygame.quit()