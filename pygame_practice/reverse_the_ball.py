import pygame,time
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
for i in range(400):
    if i <= 225:
        j = 100 + 2 * i
    else:
        j = 550 - 2 * (i - 225)
    screen.blit(my_ball,[j,100])
    pygame.display.flip()
    time.sleep(0.01)
    pygame.draw.rect(screen,[255,255,255],[j,100,90,90],0)
    pygame.display.flip()
    # screen.blit(my_ball,[100+i,100])
    # pygame.display.flip()
    # time.sleep(0.01)
screen.blit(my_ball,[j,100])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
