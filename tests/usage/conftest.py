import pygame
import pytest

import src.pygamepopup as pygamepopup


@pytest.fixture(autouse=True, scope="session")
def setup_pygamepopup():
    pygame.init()
    pygamepopup.init()


@pytest.fixture(autouse=True, scope="session")
def screen():
    return pygame.display.set_mode((500, 500))
