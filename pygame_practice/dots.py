# -*- coding: cp936 -*-
"""
程序使用了draw.lines() 函数和一个点列表来创建图
形。要想看到这个神秘的图片，必须键入代码清单16-9 中的程序。
"""
import pygame
dots = [[221, 432], [225, 331], [133, 342], [141, 310],\
[51, 230], [74, 217], [58, 153], [114, 164],\
[123, 135], [176, 190], [159, 77], [193, 93],\
[230, 28], [267, 93], [301, 77], [284, 190],\
[327, 135], [336, 164], [402, 153], [386, 217],\
[409, 230], [319, 310], [327, 342], [233, 331],\
[237, 432]]
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
pygame.draw.lines(screen,[0,0,0],True,dots,1)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
pygame.quit()


"""
逐点绘制
"""
import pygame,time
dots = [[221, 432], [225, 331], [133, 342], [141, 310],\
[51, 230], [74, 217], [58, 153], [114, 164],\
[123, 135], [176, 190], [159, 77], [193, 93],\
[230, 28], [267, 93], [301, 77], [284, 190],\
[327, 135], [336, 164], [402, 153], [386, 217],\
[409, 230], [319, 310], [327, 342], [233, 331],\
[237, 432]]
dots.append(dots[0])
print dots
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
for i in range(len(dots)-1):
    pygame.draw.lines(screen,[0,0,0],True,[dots[i],dots[i+1]],1)
    pygame.display.flip()
    time.sleep(0.1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
