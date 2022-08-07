# -*- coding:utf-8 -*-
# authority by Nutter
# exam 12-4

import sys
import pygame


def run_game():
    # 主窗口
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("按键监控")

    # 显示单元
    show_screen = pygame.display.set_mode((200, 100))
    show_rect = show_screen.get_rect()
    show_rect.x = 0
    show_rect.y = 0

    while True:
        screen.fill((230, 0, 0))
        screen.blit(show_screen, show_rect)
        pygame.display.flip()


def show_key_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            return pygame.event


run_game()
