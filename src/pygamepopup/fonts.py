"""
Defines fonts that will be used all over the application.
The init_fonts function should be called at the beginning of the application
after pygame initialization.
"""

import pygame

from .configuration import default_fonts


def init() -> None:
    """
    Load all fonts registered in default_fonts.
    System font will be load if the keyword 'default' is present in the description provided.
    These fonts will be available in all modules by importing the fonts dictionary.
    """
    for font_name, font in default_fonts.items():
        if font["is_system_font"]:
            # Use pygame's default font
            is_bold = font["is_bold"] if "is_bold" in font else False
            default_fonts[font_name] = pygame.font.SysFont(
                "arial", font["size"], is_bold
            )
        else:
            default_fonts[font_name] = pygame.font.Font(font["name"], font["size"])
