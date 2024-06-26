"""
Defines utility functions to configure the default values used across the library.
"""

from __future__ import annotations

import os
from os.path import abspath
from typing import Union

from importlib import resources
import pygame

from .constants import WHITE

resource_package = __name__

_default_sprites: dict[str, Union[dict[str, str], str]] = {
    "button_background": {
        "inactive": resources.files(resource_package)  / 'images' / 'default_box.png',
        "active": resources.files(resource_package) / 'images' / 'default_box_hover.png',
    },
    "dynamic_button_background": {
        "inactive": resources.files(resource_package) / 'images' / 'default_box.png',
        "active": resources.files(resource_package) / 'images' / 'default_box_hover.png',
    },
    "info_box_background": resources.files(resource_package) / 'images' / 'default_box.png',
}

_default_fonts_description: dict[str, dict[str, any]] = {
    "button_title": {"is_system_font": True, "size": 20, "is_bold": True},
    "dynamic_button_title": {"is_system_font": True, "size": 20, "is_bold": True},
    "text_element_content": {"is_system_font": True, "size": 20, "is_bold": True},
    "info_box_title": {"is_system_font": True, "size": 40, "is_bold": True},
}

_default_fonts: dict[str, pygame.font.Font] = {}

_default_texts: dict[str, str] = {"close_button": "Close"}

_default_colors: dict[str, dict[str, pygame.Color]] = {
    "button_text_color": {"inactive": WHITE, "active": WHITE}
}


def set_button_background(
    button_background_path: str, button_hovered_background_path: str
) -> None:
    """
    Set the default backgrounds for buttons.

    Keyword Args:
        button_background_path (str): the path to the background sprite to be set.
        button_hovered_background_path (str): the path to the background sprite when hovering to be set.
    """
    _default_sprites["button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    _default_sprites["button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_dynamic_button_background(
    button_background_path: str, button_hovered_background_path: str
) -> None:
    """
    Set the default backgrounds for dynamic buttons.

    Keyword Args:
        button_background_path (str): the path to the background sprite to be set.
        button_hovered_background_path (str): the path to the background sprite when hovering to be set.
    """
    _default_sprites["dynamic_button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    _default_sprites["dynamic_button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_info_box_background(info_box_background_path: str) -> None:
    """
    Set the default background for infoboxes.

    Keyword Args:
        info_box_background_path (str): the path to the background sprite to be set.
    """
    _default_sprites["info_box_background"] = abspath(info_box_background_path)


def set_button_title_font(font: pygame.font.Font) -> None:
    """
    Set the default font for the title of the buttons.

    Keyword Args:
        font (pygame.font.Font): the loaded font to be set.
    """
    _default_fonts["button_title"] = font


def set_dynamic_button_title_font(font: pygame.font.Font) -> None:
    """
    Set the default font for the title of the dynamic buttons.

    Keyword Args:
        font (pygame.font.Font): the loaded font to be set.
    """
    _default_fonts["dynamic_button_title"] = font


def set_text_element_font(font: pygame.font.Font) -> None:
    """
    Set the default font for the text of the text elements.

    Keyword Args:
        font (pygame.font.Font): the loaded font to be set.
    """
    _default_fonts["text_element_content"] = font


def set_info_box_title_font(font: pygame.font.Font) -> None:
    """
    Set the default font for the title of InfoBox.

    Keyword Args:
        font (pygame.font.Font): the loaded font to be set.
    """
    _default_fonts["info_box_title"] = font


def set_close_button_text(text: str) -> None:
    """
    Set the default text for the close button of InfoBox.

    Keyword Args:
        text (str): the default text to be set.
    """
    _default_texts["close_button"] = text


def set_button_text_color(color: pygame.Color, hover_color: pygame.color) -> None:
    """
    Set the default text colors for buttons.

    Keyword Args:
        color (pygame.Color): the default text color to be set.
        hover_color (pygame.Color): the default text color for when the button is hover to be set.
    """
    _default_colors["button_text_color"]["inactive"] = color
    _default_colors["button_text_color"]["active"] = hover_color
