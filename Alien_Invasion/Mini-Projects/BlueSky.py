import sys
import pygame

class settings:
    width = 300
    height = 600
    background_color = (25, 25, 255)
    screen = pygame.display.set_mode((width, height))
    screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


class Santa:
    def __init__(self, santa_pic):
        self.screen = santa_pic.screen
        self.screen_rect = santa_pic.screen.get_rect()
        self.image = pygame.image.load('../images/santa.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
