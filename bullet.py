import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self,prect):
        self.image=pygame.image.load('images/bullet1.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y-=self.speed

    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)

    def reset(self,prect):
        self.rect.x=prect.centerx
        self.rect.y=prect.y
        self.active=True
    def collide(self,enmgroup):
        if not self.active:
            return None
        enmlist=pygame.sprite.spritecollide(self,enmgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active=False
        for enm in enmlist:
            if enm.blood==1:
                enm.active=False
            elif enm.blood>0:
                enm.blood-=1
class DouBullet(pygame.sprite.Sprite):
    def __init__(self,prect):
        self.image=pygame.image.load('images/bullet2.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx- 10
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        self.num=400   
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y-=self.speed
    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)

    def reset(self,prect):
        self.rect.x=prect.centerx- 10
        self.rect.y=prect.y
        self.active=True
    def collide(self,enmgroup):
        if not self.active:
            return None
        enmlist=pygame.sprite.spritecollide(self,enmgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active=False
        for enm in enmlist:
            if enm.blood==1:
                enm.active=False
            elif enm.blood>0:
                enm.blood-=1
class DouBullet1(pygame.sprite.Sprite):
    def __init__(self,prect):
        self.image=pygame.image.load('images/bullet2.png').convert_alpha()
        self.sound=pygame.mixer.Sound('sound/bullet.wav')
        self.rect=self.image.get_rect()
        self.rect.x=prect.centerx+10
        self.rect.y=prect.y
        self.active=True
        self.speed=12
        self.num=400 
        self.mask=pygame.mask.from_surface(self.image)
    def move(self):
        self.rect.y-=self.speed
        
    def draw(self,surface):
        if self.active:
            surface.blit(self.image,self.rect)

    def reset(self,prect):
        
        self.rect.x=prect.centerx+ 10
        self.rect.y=prect.y
        self.active=True
    def collide(self,enmgroup):
        if not self.active:
            return None
        enmlist=pygame.sprite.spritecollide(self,enmgroup,False,pygame.sprite.collide_mask)
        if enmlist!=[]:
            self.active=False
        for enm in enmlist:
            if enm.blood==1:
                enm.active=False
            elif enm.blood>0:
                enm.blood-=1
                
                
        
                
                
        
            
            

        

