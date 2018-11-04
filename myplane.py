import pygame
from pygame.locals import* 


class Myplane(pygame.sprite.Sprite):
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.image1=pygame.image.load('images/me1.png').convert_alpha()
        self.image2=pygame.image.load('images/me2.png').convert_alpha()
        self.destroy_images=[pygame.image.load('images/me_destroy_1.png').convert_alpha(),                pygame.image.load('images/me_destroy_2.png').convert_alpha(),               pygame.image.load('images/me_destroy_3.png').convert_alpha(),               pygame.image.load('images/me_destroy_4.png').convert_alpha()]
        self.sound=pygame.mixer.Sound('sound/me_down.wav')
        self.rect=self.image1.get_rect()
        self.rect.x=(width-self.rect.width)/2
        self.rect.y=height-self.rect.height- 160
        self.speed=10
        self.active=True
        self.life_num=3
        self.switch=0
        self.destroy_index=0
        self.mask=pygame.mask.from_surface(self.image1)
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[K_w]:
            if self.rect.y>0:
                self.rect.y=self.rect.y-self.speed
        if keys[K_s]:
            if self.rect.y<(self.height-self.rect.height- 160):
                self.rect.y=self.rect.y+self.speed
        if keys[K_a]:
            if self.rect.x>0:
                self.rect.x=self.rect.x-self.speed
        if keys[K_d]:
            if self.rect.x<(self.width-self.rect.width):
                self.rect.x=self.rect.x+self.speed
    def draw(self,surface):
        if self.active:
            self.draw_active(surface)
        else:
            self.draw_destroy(surface)
    def draw_active(self,surface):
        if self.switch% 5 !=0:
            surface.blit(self.image1,self.rect)
        else:
            surface.blit(self.image2,self.rect)
        self.switch+=1
    def draw_destroy(self,surface):
        if self.destroy_index<20:
            surface.blit(self.destroy_images[self.destroy_index//5],self.rect)
            self.destroy_index+=1
        elif self.life_num>0:
            self.life_num-=1
            self.reset()
    def reset(self):
        self.rect.x=(self.width-self.rect.width)/2
        self.rect.y=self.height- self.rect.height- 160
        self.active=True
        self.switch=0
        self.destroy_index=0
    def collide(self,enemys_group):
        emlist=pygame.sprite.spritecollide(self,enemys_group,False,pygame.sprite.collide_mask)
        
        if emlist !=[]:
            self.active=False
        elif self.life_num>3:
            self.life_num-=1
        for em in emlist:
            em.active=False
    
