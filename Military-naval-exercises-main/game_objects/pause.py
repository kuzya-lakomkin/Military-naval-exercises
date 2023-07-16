"""
экран предупреждения о вреде для глаз
"""

import sys

import pygame

from countdown import Countdown
from game_objects import colors
from scene import Scene
from shell import Shell


class Pause(Scene):
    def __init__(self, shell: Shell):

        Scene.__init__(self, shell)
        self.countdown = Countdown(10 * 60)
        self.background_image = pygame.image.load('images/pause.jpg')

    def run(self):
        while True:
            if self.countdown.update():
                return
            self.main_background()
            self.handle_events()
            pygame.display.update()
            self.shell.tick()

    def main_background(self) -> None:
        self.shell.surface.blit(self.background_image, (0, 0))

        pygame.draw.rect(self.shell.surface, colors.GREEN, (10, 154, 1180, 12))
        pygame.draw.rect(self.shell.surface, colors.WHITE, (11, 155, 1178, 10))
        dx = self.countdown.counted_time / self.countdown.max_time
        pygame.draw.rect(self.shell.surface, colors.GREEN, (12, 156, 1176 * dx, 8))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
