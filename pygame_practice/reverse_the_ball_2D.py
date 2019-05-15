import pygame,time
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
for i in range(4123):
    n = i % 550
    if n <= 225:
        j = 100 + 2 * n
    elif n < 500:
        j = 550 - 2 * (n - 225)
    else:
        j = 2 * ( n - 500)
    m = i % 390
    if m <= 145:
        k = 100 + 2 * m
    elif m < 340 :
        k = 390 - 2 * (m - 145)
    else:
        k = 2 * ( m - 340 )
    for d in range(20):
        screen.blit(my_ball,[j,k])
        pygame.display.flip()
        time.sleep(0.00001)
    pygame.draw.rect(screen,[255,255,255],[j,k,90,90],0)
    pygame.display.flip()
    # screen.blit(my_ball,[100+i,100])
    # pygame.display.flip()
    # time.sleep(0.01)
screen.blit(my_ball,[j,k])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
