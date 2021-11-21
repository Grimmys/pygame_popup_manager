import pygame
import pytest

import pygamepopup


class PygamepopupTestSetup:
    @pytest.fixture(autouse=True, scope='class')
    def setup_pygamepopup(self):
        pygame.init()
        pygamepopup.init()

    @pytest.fixture(autouse=True, scope='class')
    def screen(self):
        return pygame.display.set_mode((10, 10))
