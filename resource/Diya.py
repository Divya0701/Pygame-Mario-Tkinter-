import pygame
pygame.init()
win=pygame.diplay.ser_mode((500,480));
pygame.display.set_caption("moving monkey");
walkRight=[pygame.image.load("R1E.png"),pygame.image.load("R2E.png"),pygame.image.load("R3E.png"),pygame.image.load("R4E.png"),pygame.image.load("R5E.png"),pygame.image.load("R6E.png"),pygame.image.load("R7E.png"),pygame.image.load("R8E.png"),pygame.image.load("R9E.png"),pygame.image.load("R10E.png"),pygame.image.load("R11E.png")]
walkleft=[pygame.image.load("L1E.png"),pygame.image.load("L2E.png"),pygame.image.load("L3E.png"),pygame.image.load("L4E.png"),pygame.image.load("L5E.png"),pygame.image.load("L6E.png"),pygame.image.load("R=L7E.png"),pygame.image.load("L8E.png"),pygame.image.load("L9E.png"),pygame.image.load("L10E.png"),pygame.image.load("L11E.png")]
x=300
y=410
height=64
width=64
run=True
val=5
while run:
     pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>vel:
        x-=vel
    if keys[pygame.K_RIGHT] and x<500-width-vel:
        x+=vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
           y-=vel
        if keys[pygame.K_DOWN]and y<500-height-vel:
           y+=vel
        if keys[pygame.K_SPACE]:
            isJump=True
    else:
        if jumpCount>=-10:
            neg=1
            if jumpCount<0:
                neg=-1
            y-=(jumpCount**0.5)*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=10
        
    win.fill((0,0,0))
    #pygame.draw.rect(win,(0,0,255),(x,y,width,height))
    #pygame.display.update()
    
pygame.quit()
