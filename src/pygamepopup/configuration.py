import os
from typing import Union

import pkg_resources
import pygame

resource_package = __name__

default_sprites = {
    "button_background": {
        "inactive": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box.png"))
        ),
        "active": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box_hover.png"))
        ),
    },
    "dynamic_button_background": {
        "inactive": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box.png"))
        ),
        "active": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box_hover.png"))
        ),
    },
    "info_box_background": pkg_resources.resource_filename(
        resource_package, "/".join(("images", "default_box.png"))
    ),
}

default_fonts: dict[str, Union[dict[str, any], pygame.font.Font]] = {
    "button_title": {"is_system_font": True, "size": 20, "is_bold": True},
    "dynamic_button_title": {"is_system_font": True, "size": 20, "is_bold": True},
    "text_element_content": {"is_system_font": True, "size": 20, "is_bold": True},
    "info_box_title": {"is_system_font": True, "size": 40, "is_bold": True}
}


def set_button_background(
        button_background_path: str, button_hovered_background_path: str
) -> None:
    default_sprites["button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    default_sprites["button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_dynamic_button_background(
        button_background_path: str, button_hovered_background_path: str
) -> None:
    default_sprites["dynamic_button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    default_sprites["dynamic_button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_info_box_background(info_box_background_path: str) -> None:
    default_sprites["info_box_background"] = os.path.abspath(info_box_background_path)


def set_button_title_font(font: pygame.font.Font) -> None:
    default_fonts["button_title"] = font


def set_dynamic_button_title_font(font: pygame.font.Font) -> None:
    default_fonts["dynamic_button_title"] = font


def set_text_element_font(font: pygame.font.Font) -> None:
    default_fonts["text_element_content"] = font


def set_info_box_title(font: pygame.font.Font) -> None:
    default_fonts["info_box_title"] = font
