# -*- coding: cp936 -*-
##画sin曲线
import random,sys,math,pygame
pygame.init()
screen = pygame.display.set_mode([640,320])
circle = 8
A = []
screen.fill([255,255,255])
for i in range(640):
    y = 160-int(160*math.sin(float(i+1)/640*circle*2*math.pi))
    A.append([i,y])
for i in range(639):
    pygame.draw.lines(screen,[random.randint(0,255),random.randint(0,255),random.randint(0,255)],True,[A[i],A[i+1]],1)
#    time.sleep(0.01)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
