#
# import pygame
#
#
# class Bullet2(pygame.sprite.Sprite):
#
#     def __init__(self,screen,gun):
#
#         super(Bullet2, self).__init__()
#         self.screen = screen
#         self.rect2 = pygame.Rect(0,0,2,12)
#         self.color2 = 255,0, 0
#         self.speed2 = 3
#         self.rect2.centerx = gun.rect2.centerx
#         self.rect2.top = gun.rect2.top
#         self.y2 = float(self.rect2.y)
#
#     def update2(self):
#         self.y2 -= self.speed2
#         self.rect2.y = self.y2
#
#     def drawBullet2(self):
#         pygame.draw.rect(self.screen, self.color2, self.rect2)
