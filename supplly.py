import pygame
from random import randint



class Bomb_subbly(pygame.sprite.Sprite):
    def __init__(self,width,height):
        self.image=pygame.image.load('images/bomb_supply.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/use_bomb.wav')
        self.active=False
        self.speed=4
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.x=randint(0,width-self.rect.width)
        self.rect.y=0
        self.width=width
        self.height=height
        self.num=0
    def move(self):
        if not self.active:
            return
        self.rect.y+=self.speed
        if self.rect.y>self.height:
            self.reset()

    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
            
    def reset(self):
        self.rect.x=randint(0,self.width-self.rect.width)
        self.rect.y=0
        self.active=False
        
    def collide(self,plane):
        if pygame.sprite.collide_mask(self,plane):
                
            if self.num<3:
                self.num+=1
            self.active=False
            self.reset()
            
    def use(self,enmgroup):
        
        if self.num>0:
            self.num-=1
            for enm in enmgroup:
                if enm.rect.y>0:
                    enm.active=False
class Buet_subbly(pygame.sprite.Sprite):
    def __init__(self,width,height):
        self.image=pygame.image.load('images/bullet_supply.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/use_bomb.wav')
        self.active=False
        self.speed=3
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
        self.rect.x=randint(0,width-self.rect.width)
        self.rect.y=0
        self.width=width
        self.height=height
        self.num=0
        self.flag=0
    def move(self):
        if not self.active:
            return
        self.rect.y+=self.speed
        if self.rect.y>self.height:
            self.reset()

    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)
            
    def reset(self):
        self.rect.x=randint(0,self.width-self.rect.width)
        self.rect.y=0
        self.active=False
        
    def collide(self,plane):
        if pygame.sprite.collide_mask(self,plane):
                
            if self.flag==0:
                self.flag+=500
                self.active=False
                self.reset()
    
      
             

             
