# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Two player game")
robot1 = pygame.image.load("robot.png")
robot2 = pygame.image.load("robot.png")

x1, y1 = 1, 1
x2, y2 = 100, 100

to_right1 = to_left1 = up1 = down1 = False
to_right2 = to_left2 = up2 = down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True

            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False

            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False


    if to_right1 and x1 + robot1.get_width() < 640:
        x1 += 1
    if to_left1 and x1 > 0:
        x1 -= 1
    if up1 and y1 > 0:
        y1 -= 1
    if down1 and y1 + robot1.get_height() < 480:
        y1 += 1


    if to_right2 and x2 + robot2.get_width() < 640:
        x2 += 1
    if to_left2 and x2 > 0:
        x2 -= 1
    if up2 and y2 > 0:
        y2 -= 1
    if down2 and y2 + robot2.get_height() < 480:
        y2 += 1

   
    window.fill((0, 0, 0)) 
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()
    clock.tick(60)
