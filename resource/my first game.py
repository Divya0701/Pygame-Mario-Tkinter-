import pygame
pygame.init()
win =pygame.display.set_mode((500,480))
pygame.display.set_caption("my first game")
walkRight=[pygame.image.load("R1.png"),pygame.image.load("R2.png"),pygame.image.load("R3.png"),pygame.image.load("R4.png"),pygame.image.load("R5.png"),pygame.image.load("R6.png"),pygame.image.load("R7.png"),pygame.image.load("R8.png"),pygame.image.load("R9.png")]
walkLeft=[pygame.image.load("L1.png"),pygame.image.load("L2.png"),pygame.image.load("L3.png"),pygame.image.load("L4.png"),pygame.image.load("L5.png"),pygame.image.load("L6.png"),pygame.image.load("L7.png"),pygame.image.load("L8.png"),pygame.image.load("L9.png")]
bg=pygame.image.load("bg.jpg")
char=pygame.image.load("standing.png")

clock =pygame.time.Clock()
class player(object):
    def __init__(self,x,y,height,width):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.walkCount=0
        self.left=False
        self.right=False
        self.isJump=False
        self.vel=5
        self.jumpCount=10
    def draw(self,win):
    
        if self.walkCount+1 >= 27:
            
            self.walkCount=0
        if self.left:
            win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        elif self.right:
            win.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount+=1
        else:
            win.blit(char,(self.x,self.y))
            
man=player(300,410,64,64)
def red():
    win.blit(bg,(0,0))
    man.draw(win)
    pygame.display.update()
run=True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
    elif keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel:
        man.x+=man.vel
        man.left=False
        man.right=True
    else:
        man.left=False
        man.right=False
        man.walkCount=0
        
    if not(man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump=True
            man.left=False
            man.right=False
            man.walkCount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:
                neg=-1
            y-=(man.jumpCount**2)*0.5*neg
            man.jumpCount-=1
        else:
            man.isJump=False
            man.jumpCount=10
        
    red()
    
pygame.quit()
