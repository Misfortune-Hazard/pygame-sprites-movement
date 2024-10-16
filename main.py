import pygame
from config import *
from sprite import Sprite

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Spritesheets")

clock = pygame.time.Clock()

spritesheet = pygame.image.load("assets/Soldier/Soldier-Walk.png").convert_alpha()
num_frames = 8

sprite = Sprite(spritesheet, num_frames, SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 0.1)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite)

run = True
while run:
  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()
  dx, dy = 0, 0

  if keys[pygame.K_LEFT]:
    dx = -5
  if keys[pygame.K_RIGHT]:
    dx = 5
  if keys[pygame.K_UP]:
    dy = -5
  if keys[pygame.K_DOWN]:
    dy = 5

  sprite.move(dx, dy)
     
  all_sprites.update()

  screen.fill(CUSTOM_COLOR)
  
  all_sprites.draw(screen)

  pygame.display.update()

  clock.tick(60)

pygame.quit()