##»­sinÇúÏß
import random,math,pygame,time
pygame.init()
screen = pygame.display.set_mode([640,320])
circle = 2
screen.fill([255,255,255])
for i in range(640):
    pygame.draw.circle(screen,[random.randint(0,255),random.randint(0,255),\
                               random.randint(0,255)],[i,160-int(160*math.sin(float(i+1)/640*circle*2*math.pi))],1,0)

    time.sleep(0.01)
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
