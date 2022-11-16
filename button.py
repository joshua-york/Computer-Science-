import pygame,sys,random
from pygame.locals import *
pygame.font.init()

red = ((255,0,0))
font = pygame.font.SysFont("comicsans",30,True)


class images():
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self._image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self._rect = self._image.get_rect()
        self._rect.topleft = (x,y)

    def draw(self,surface):
        surface.blit(self._image,(self._rect.x,self._rect.y))


class buttons(images):
    def __init__(self,x,y,image,scale):
        super().__init__(x,y,image,scale)#inheriting this from images
        self.clicked = False#making sure that things are only pressed once, like a toggle

    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()#getting the position of the mouse

        if self._rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.clicked == False:#checking collision between mouse and buttons
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:#checking if the left mouse button has been clicked
            self.clicked = False

        surface.blit(self._image,(self._rect.x,self._rect.y))#loads the button on screen
        
        return action

class player(images):
    def __init__(self,x,y,max_hp,image,scale):
        super().__init__(x,y,image,scale)
        self.max_hp = max_hp
        self.hp = max_hp
        self.alive = True
        self._rect.center = (x,y)

    def draw(self,screen):
        pygame.draw.rect(screen, (0,128,0),(150,595,50 - (1.75*(10-self.hp)),40))#health bar
        text = font.render(str(self.hp),1,(255,255,255))
        screen.blit(self._image,self._rect)
        screen.blit(text,(155,592))


    def hurt1(self,damage):
        self.hp -= damage

        if self.hp <= 0:
            self.alive = False

        return self.hp,self.alive



class enemy(images):
    def __init__(self,x,y,max_hp,strength,image,scale):
        super().__init__(x,y,image,scale)
        self.x = x
        self.width = image.get_width()
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.alive = True
        self._rect.center = (x,y)
        self.clicked = False
        self.clicked2 = False

    def draw(self,screen):
        pygame.draw.rect(screen, (0,128,0),(700,595,50 - (1.75*(10-self.hp)),40))#health bar
        text = font.render(str(self.hp),1,(255,255,255))
        screen.blit(self._image,self._rect)
        screen.blit(text,(self.x + (self.width*0.5),592))

    def action(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self._rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and self.clicked == False:#checking collision between mouse and buttons
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:#checking if the left mouse button has been clicked
            self.clicked = False

        return action

    def action2(self):
        action2 = False
        pos = pygame.mouse.get_pos()
        
        if self._rect.collidepoint(pos) and pygame.mouse.get_pressed()[2] and self.clicked2 == False:#checking collision between mouse and buttons
            self.clicked2 = True
            action2 = True

        if pygame.mouse.get_pressed()[2] == 0:#checking if the left mouse button has been clicked
            self.clicked2 = False

        return action2
    
    def hurt1(self):
        self.hp -= 10

        if self.hp <= 0:
            self.alive = False

        return self.hp, self.alive

    def hurt2(self,damage):
        self.damage = damage
        self.hp -= damage

        if self.hp <= 0:
            self.alive = False

        return self.hp, self.alive



            
        
