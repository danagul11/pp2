import pygame,time
import random
from pygame.locals import *
# Initialize pygame program
pygame.init()

# Surface
SCREEN_WIDTH, SCREEN_HEIGHT = 800,500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hungry lion")
font = pygame.font.SysFont('Arial', 30)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

running = True

clock = pygame.time.Clock()
# Frames Per Second
FPS = 30
x,y,dx,dy=100,100,10,10
block=10
score=0
enemy = []
food = []
 
# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    ex = random.randrange(10, SCREEN_WIDTH-50)
    ey = random.randrange(10, SCREEN_HEIGHT-50)
    enemy.append([ex, ey,30,20])

for i in range(10):
    fx = random.randrange(10, SCREEN_WIDTH-50)
    fy = random.randrange(10, SCREEN_HEIGHT-50)
    food.append([fx, fy,30,20])

# Main loop
while running:
  # Event loop
  pressed_keys = pygame.key.get_pressed()
  if pressed_keys[K_LEFT]:
    x-=block
  if pressed_keys[K_RIGHT]:
    x+=block
  if pressed_keys[K_UP]:
    y-=block
  if pressed_keys[K_DOWN]:
    y+=block

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # if event.type == pygame.KEYDOWN:

  screen.fill(WHITE)
  show = font.render('Score: ' + str(score), True, BLACK)

  pygame.draw.rect(screen,BLUE,(x,y,dx,dy))
  for i in range(len(enemy)):
    pygame.draw.rect(screen,RED,enemy[i])

    # Move the snow flake down one pixel
    enemy[i][1] += 1

    # If the snow flake has moved off the bottom of the screen
    if (x>=enemy[i][0] and x<=enemy[i][0]+30 and y>=enemy[i][1] and y<=enemy[i][1]+30) or (x <=enemy[i][0] and x+10>=enemy[i][0] and y<=enemy[i][1] and y+10>=enemy[i][1]):
      pygame.mixer.music.load('lose.wav')
      pygame.mixer.music.play(1)
      score-=1
      ey = random.randrange(-50, -10)
      enemy[i][1] = ey
      # Give it a new x position
      ex = random.randrange(10, SCREEN_WIDTH-50)
      enemy[i][0] = ex
    if enemy[i][1] > SCREEN_HEIGHT:
        # Reset it just above the top
        ey = random.randrange(-50, -10)
        enemy[i][1] = ey
        # Give it a new x position
        ex = random.randrange(10, SCREEN_WIDTH-50)
        enemy[i][0] = ex

  for i in range(len(food)):
      pygame.draw.rect(screen,GREEN,food[i])
      ran=random.randrange(-3,3)
      food[i][0] += ran
      food[i][1] += ran
      if (x>=food[i][0] and x<=food[i][0]+30 and y>=food[i][1] and y<=food[i][1]+30) or (x <=food[i][0] and x+10>=food[i][0] and y<=food[i][1] and y+10>=food[i][1]):
        pygame.mixer.music.load('coin.wav')
        pygame.mixer.music.play(1)
        score+=1
        fy = random.randrange(10, SCREEN_HEIGHT-50)
        food[i][1] = fy
        # Give it a new x position
        fx = random.randrange(10, SCREEN_WIDTH-50)
        food[i][0] = fx
      # If the snow flake has moved off the bottom of the screen
      if food[i][1] > SCREEN_HEIGHT or food[i][1] <0 or food[i][0] > SCREEN_WIDTH or food[i][0] <0  :
          # Reset it just above the top
          fy = random.randrange(10, SCREEN_HEIGHT-50)
          food[i][1] = fy
          # Give it a new x position
          fx = random.randrange(10, SCREEN_WIDTH-50)
          food[i][0] = fx
  screen.blit(show, (20, 20))
  if score<0:
    for i in range(500):
      screen.fill(WHITE)  
      font2 = pygame.font.SysFont('Arial', 50)
      GO = font2.render('Game is OVER '+ 'Your Score: ' + str(score), True, BLACK)
      screen.blit(GO, (100, 200))
      pygame.display.flip()

    running=False
  pygame.display.flip()

  clock.tick(FPS)


pygame.quit()