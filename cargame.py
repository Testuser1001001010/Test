import pygame, random
from pygame.locals import *
pygame.init()
score = 0
info = pygame.display.Info()
WIDTH,HEIGHT = info.current_w,info.current_h
road_w = int(WIDTH/1.6)
roadmark_w= int(WIDTH/80)
rightlane = WIDTH/2 + road_w/4
leftlane = WIDTH/2 - road_w/4
pygame.init()
running = True
screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Car Game")


pygame.display.update()
car = pygame.image.load("games/car.png")
carloc = car.get_rect()
carloc.center = rightlane, HEIGHT*0.8
car2 = pygame.image.load("games/othercar.png")
car2loc = car.get_rect()
car2loc.center = leftlane, HEIGHT*0.2
while running:
    if score < 30:
        screen.fill((0,255,0))
    if score >= 30 and score < 60:
        screen.fill((255,255,0))
    if score >= 60:
        screen.fill((255,0,0))
    car2loc[1] += score + 3
    if car2loc[1] > HEIGHT:
        score = score + 0.1
        if random.randint(0,1) == 0:
            car2loc.center = rightlane, -200
        else:
            car2loc.center = leftlane, -200
    if carloc[0] == car2loc[0] and car2loc[1] > carloc[1] - 250:
        print("Game over! You lose")
        print("Your score was: ", round(score * 10))
        break
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_d,K_RIGHT]:
                carloc = carloc.move([+int(road_w/2), 0])
            if event.key in [K_a,K_LEFT]:
                carloc = carloc.move([-int(road_w/2), 0])
    pygame.draw.rect(
        screen,
        (50,50,50),
        (WIDTH/2-road_w/2, 0, road_w, HEIGHT))
    pygame.draw.rect(
        screen,
        (255,240,60),
        (WIDTH/2 - roadmark_w/2,0,roadmark_w,HEIGHT))
    pygame.draw.rect(
        screen,
        (255,255,255),
        (WIDTH/2 - road_w/2 + roadmark_w*2,0,roadmark_w,HEIGHT))
    pygame.draw.rect(
        screen,
        (255,255,255),
        (WIDTH/2 + road_w/2 - roadmark_w*3,0,roadmark_w,HEIGHT))
    screen.blit(car, carloc)
    screen.blit(car2, car2loc)
    
    pygame.display.update()

pygame.quit()