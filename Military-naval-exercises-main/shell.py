import time

import pygame

from config import Config


# класс описывает окно программы, позволяет переключать сцены
from countdown import Countdown


class Shell:
    def __init__(self, config: Config):
        self.state = 1
        self.config = config

        # время, проведённое в игре
        self.totalInGameTime = 0
        self.lastInGameTime = 0

        # настройка звука
        pygame.mixer.init(44100, -16, 2, 4096)
        pygame.init()
        pygame.font.init()

        self.surface = pygame.display.set_mode((config.screen_width, config.screen_height))
        pygame.display.set_caption("Военно-морские учения")
        self.clock = pygame.time.Clock()
        self.countdown = Countdown(self.config.max_in_game_time)

    def tick(self):
        self.clock.tick(self.config.fps)

