### -*- coding: cp936 -*-
###some methods in pygame
import pygame
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])

##pygame.draw.circle
pygame.draw.circle(screen,[111,111,111],[100,100],10,0)
pygame.display.flip()
pygame.time.delay(1000)

##pygame.draw.rect
pygame.draw.rect(screen,[11,11,11],[200,200,10,10],0)
pygame.display.flip()
pygame.time.delay(1000)

##pygame.draw.lines
dots = [[300,300],[311,311]]
pygame.draw.lines(screen,[99,99,99],False,dots,2)
pygame.display.flip()
pygame.time.delay(1000)

##screen.set_at
screen.set_at([500,300],[0,0,0])##����������Ϊ����ɫ
pygame.display.flip()
pygame.time.delay(1000)

##screen.get_at
color1 = screen.get_at([500,300])##�������µ���ɫ
print color1

##pygame.image.load("") +  pygame.slit("",[x,y])  ����ͼƬ
image = pygame.image.load("beach_ball.png")
screen.blit(image,[200,250])
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()