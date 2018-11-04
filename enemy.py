import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('images/enemy1.png').convert_alpha()
        self.destroy_list=[pygame.image.load('images/enemy1_down1.png').convert_alpha(),
        pygame.image.load('images/enemy1_down2.png').convert_alpha(),
        pygame.image.load('images/enemy1_down3.png').convert_alpha(),
        pygame.image.load('images/enemy1_down4.png').convert_alpha()]
        self.sound=pygame.mixer.Sound('sound/enemy1_down.wav')
        self.rect=self.image.get_rect()
        self.rect.x=randint(0,width- self.rect.width)
        self.rect.y=randint(-5*height,0)
        self.active=True
        self.speed=5
        self.mask=pygame.mask.from_surface(self.image)
        self.destroy_index=0
        self.width,self.height=width,height
        self.flag=1
        self.score=0
        self.blood=1
    def move(self):
        self.rect.y+=self.speed
        if self.rect.y>self.height:
            self.reset()
    def draw_active(self,surface):
        

        surface.blit(self.image,self.rect)

    def draw_destroy(self,surface):
        if self.destroy_index < 12:
            surface.blit(self.destroy_list[self.destroy_index//3],self.rect)
            self.destroy_index+=1
        else:
            
            self.reset()
            self.score=1000
    def draw(self,surface):
        if self.active:
            self. draw_active(surface)
        else:
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index=0
        self.rect.x=randint(0,self.width-self.rect.width)
        self.rect.y=randint(-5*self.height,0)
        self.active=True
        self.score=0
class Enemyz(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load('images/enemy2_hit.png').convert_alpha()
        self.image=pygame.image.load('images/enemy2.png').convert_alpha()
        self.destroy_list=[pygame.image.load('images/enemy2_down1.png').convert_alpha(),
        pygame.image.load('images/enemy2_down2.png').convert_alpha(),
        pygame.image.load('images/enemy2_down3.png').convert_alpha(),
        pygame.image.load('images/enemy2_down4.png').convert_alpha()]
        self.sound=pygame.mixer.Sound('sound/enemy1_down.wav')
        self.rect=self.image.get_rect()
        self.rect.x=randint(0,width- self.rect.width)
        self.rect.y=randint(-5*height,0)
        self.active=True
        self.speed=2
        self.mask=pygame.mask.from_surface(self.image)
        self.destroy_index=0
        self.width,self.height=width,height
        self.flag=2
        self.score=0
        self.blood=6
    def move(self):
        self.rect.y+=self.speed
        if self.rect.y>self.height:
            self.reset()
    def draw_active(self,surface):
        if self.blood<4:
            surface.blit(self.image1,self.rect)
        else:
            surface.blit(self.image,self.rect)

    def draw_destroy(self,surface):
        if self.destroy_index < 20:
            surface.blit(self.destroy_list[self.destroy_index//5],self.rect)
            self.destroy_index+=1
        else:
            
            self.reset()
            self.score=2000
    def draw(self,surface):
        if self.active:
            self. draw_active(surface)
        else:
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index=0
        self.rect.x=randint(0,self.width-self.rect.width)
        self.rect.y=randint(-5*self.height,0)
        self.active=True
        self.score=0
class Enemyd(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.image2=pygame.image.load('images/enemy3_hit.png').convert_alpha()
        self.image=pygame.image.load('images/enemy3_n1.png').convert_alpha()
        self.destroy_list=[pygame.image.load('images/enemy3_down1.png').convert_alpha(),
        pygame.image.load('images/enemy3_down2.png').convert_alpha(),
        pygame.image.load('images/enemy3_down3.png').convert_alpha(),
        pygame.image.load('images/enemy3_down4.png').convert_alpha(),
        pygame.image.load('images/enemy3_down5.png').convert_alpha(),
        pygame.image.load('images/enemy3_down6.png').convert_alpha()]
        self.sound=pygame.mixer.Sound('sound/enemy1_down.wav')
        self.rect=self.image.get_rect()
        self.rect.x=randint(0,width- self.rect.width)
        self.rect.y=randint(-5*height,0)
        self.active=True
        self.speed=1
        self.mask=pygame.mask.from_surface(self.image)
        self.destroy_index=0
        self.width,self.height=width,height
        self.flag=3
        self.score=0
        self.blood=12
    def move(self):
        self.rect.y+=self.speed
        if self.rect.y>self.height:
            self.reset()
    def draw_active(self,surface):
        if self.blood<6:
            surface.blit(self.image2,self.rect)
        else:
            surface.blit(self.image,self.rect)

    def draw_destroy(self,surface):
        if self.destroy_index <24 :
            surface.blit(self.destroy_list[self.destroy_index//4],self.rect)
            self.destroy_index+=1
        else:
            
            self.reset()
            self.score=4000
    def draw(self,surface):
        if self.active:
            self. draw_active(surface)
        else:
            self.draw_destroy(surface)
    def reset(self):
        self.destroy_index=0
        self.rect.x=randint(0,self.width-self.rect.width)
        self.rect.y=randint(-5*self.height,0)
        self.active=True
        self.score=0
