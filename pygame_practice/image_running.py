import pygame,time
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
my_ball = pygame.image.load("beach_ball.png")
for i in range(100):
    screen.blit(my_ball,[100+2*i,100])
    pygame.display.flip()
    time.sleep(0.01)
    pygame.draw.rect(screen,[255,255,255],[100+2*i,100,90,90],0)
    pygame.display.flip()
    # screen.blit(my_ball,[100+i,100])
    # pygame.display.flip()
    # time.sleep(0.01)
screen.blit(my_ball,[100+2*i,100])
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
