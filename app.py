import pygame
from pygame.locals import *
import sys
import os
import time
import random
import math
import variables

paused = variables.paused

pygame.init()


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load("images/background.png"), (0, 0))
        self.screen.blit(pygame.image.load("images/title.png"), (0, 0))
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.Font("fonts/Korean_Calligraphy.ttf", 20)
        self.lives = 1
        self.level = 1
        self.game_over = False
        self.game_over_text = self.font.render("YOU DIED", True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (self.weight / 2, self.height / 2)
        self.game_over_rect.top = self.game_over_rect.top - 100
        self.game_over_rect.left = self.game_over_rect.left - 100
        self.game_over_rect.right = self.game_over_rect.right + 100
        self.game_over_rect.bottom = self.game_over_rect.bottom + 100
        self.player = Player(self.screen)
        self.enemies = []
        self.enemy_count = 0
        self.enemy_spawn_rate = 1
        self.enemy_spawn_rate_max = 1
        self.enemy_spawn_rate_min = 1
        self.enemy_spawn_rate_decrease = 0.01
        self.enemy_spawn_rate_increase = 0.01
        self.enemy_spawn_rate_increase_rate = 0
            

    def on_init(self):
        self._running = True
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((0, 0, 0))
        self._display_surf.blit(pygame.image.load("images/background.png"), (0, 0))
        self._display_surf.blit(pygame.image.load("images/title.png"), (0, 0))
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.font = pygame.font.SysFont("monospace", 20)
        self.lives = 1
        self.level = 1
        self.game_over = False
        self.game_over_text = self.font.render("YOU DIED", True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (self.weight / 2, self.height / 2)
        self.game_over_rect.top = self.game_over_rect.top - 100
        self.game_over_rect.left = self.game_over_rect.left - 100
        self.game_over_rect.right = self.game_over_rect.right + 100
        self.game_over_rect.bottom = self.game_over_rect.bottom + 100
        self.player = Player(self.screen)
        self.enemies = []
        self.enemy_count = 0
        self.enemy_spawn_rate = 1
        self.enemy_spawn_rate_max = 1
        self.enemy_spawn_rate_min = 1
        self.enemy_spawn_rate_decrease = 0.01
        self.enemy_spawn_rate_increase = 0.01
        self.enemy_spawn_rate_increase_rate = 0

    def on_event(self, event, paused):  # event handler
        if event == pygame.QUIT:
            self._running = False
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                if paused == "True":
                    paused = False
                else:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    paused = False
                                if event.key == pygame.K_p:
                                    paused = False
                        self.screen.fill((0, 0, 0))
                        self.screen.blit(pygame.image.load("images/background.png"), (0, 0))
                        self.screen.blit(pygame.image.load("images/pause.png"), (0, 0))
                        pygame.display.flip()
    
    def on_loop(self):  # game logic
        if self.game_over:
            self.screen.blit(self.game_over_text, self.game_over_rect)
            pygame.display.flip()
            return
        self.player.update()
    
    def on_render(self):  # draw graphics
        self.screen.fill((0, 0, 0))
        self.screen.blit(pygame.image.load("images/background.png"), (0, 0))
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        pygame.display.flip()
    

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.x = 400
        self.y = 550
        self.width = 50
        self.height = 50
        self.speed = 5
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        self.rect.center = (self.x, self.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.move()
        self.draw()

def main():
    game = App()
    game.on_init()

    while game._running:
        game.on_event(pygame.event.get(), False)
        game.on_loop()
        game.on_render()
        game.clock.tick(game.fps)

main()