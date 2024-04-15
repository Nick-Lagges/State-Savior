"""
Nick Lagges
Button Class
"""

import pygame

class Button:
    def __init__(self, font, color, x, y, width, height, text):
        self.font = font
        self.color = color
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.text = text

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        #draw_text(text, font, (0,0,0), screen, x + width / 2, y + height / 2)
        text_obj = self.font.render(self.text, True, (0,0,0))
        text_rect = text_obj.get_rect()
        text_rect.center = (self.x + self.width / 2, self.y + self.height / 2)
        screen.blit(text_obj, text_rect)
