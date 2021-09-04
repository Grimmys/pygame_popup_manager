"""
Defines Button class, a BoxElement able to react to user actions.
"""
import os.path
from enum import Enum
from typing import Union, Callable

import pygame

from ..configuration import default_sprites, default_fonts
from .box_element import BoxElement
from ..constants import WHITE, BUTTON_SIZE
from ..types import Position, Margin


class Button(BoxElement):
    """
    This class is representing any kind of button that could be seen on an interface.
    A button is receptive to user clicks and returns an id corresponding to a method,
    it may have specific arguments too.
    Mouse motion is also handled: the button appearance can change according to current focus.

    Keyword arguments:
    callback -- the reference to the function that should be call after a click
    size -- the size of the button following the format "(width, height)"
    position -- the position of the element on the screen
    title -- the text that should be displayed at the center of the element
    background_path -- the path to the image corresponding to the sprite of the element
    background_hover_path -- the path to the image corresponding to the sprite of the element
    when it has the focus
    margin -- a tuple containing the margins of the box,
    should be in the form "(top_margin, right_margin, bottom_margin, left_margin)"
    linked_object -- the game entity linked to the button if there is one
    disabled -- a boolean indicating if it is not possible to interact with the button
    font -- the font that should be used to render the title

    Attributes:
    callback -- the reference to the function that should be call after a click
    sprite -- the pygame Surface corresponding to the sprite of the element
    sprite_hover -- the pygame Surface corresponding to the sprite of the element
    when it has the focus
    linked_object -- the game entity linked to the button if there is one,
    would be returned on click
    """

    def __init__(
            self,
            callback: Callable = lambda: None,
            size: tuple[int, int] = BUTTON_SIZE,
            title: str = "",
            position: Position = pygame.Vector2(0, 0),
            background_path: str = None,
            background_hover_path: str = None,
            margin: Margin = (10, 0, 10, 0),
            linked_object: any = None,
            disabled: bool = False,
            font: pygame.font.Font = None,
            text_color: tuple[int, int, int] = WHITE,
            font_hover: pygame.font.Font = None,
            text_hover_color: tuple[int, int, int] = WHITE
    ) -> None:
        super().__init__(position, None, margin)
        self.callback: Union[Enum, Callable] = callback
        self.size: tuple[int, int] = size

        if not font:
            font = default_fonts["button_title"]
        rendered_title = font.render(title, True, text_color)

        if not font_hover:
            font_hover = font
        rendered_title_hover = font_hover.render(title, True, text_hover_color)

        background_path = os.path.abspath(background_path) if background_path \
            else default_sprites["button_background"]["inactive"]
        raw_sprite = pygame.image.load(background_path)
        sprite = pygame.transform.scale(raw_sprite.convert_alpha(), size)
        sprite.blit(
            rendered_title,
            (
                sprite.get_width() // 2 - rendered_title.get_width() // 2,
                sprite.get_height() // 2 - rendered_title.get_height() // 2,
            ),
        )

        background_hover_path = os.path.abspath(background_hover_path) if background_hover_path else \
            default_sprites["button_background"]["active"]
        raw_sprite_hover = pygame.image.load(background_hover_path)
        sprite_hover = pygame.transform.scale(raw_sprite_hover.convert_alpha(), size)
        sprite_hover.blit(
            rendered_title_hover,
            (
                sprite_hover.get_width() // 2 - rendered_title_hover.get_width() // 2,
                sprite_hover.get_height() // 2 - rendered_title_hover.get_height() // 2,
            ),
        )
        self.sprite = sprite
        self.sprite_hover = sprite_hover
        self.content = self.sprite
        self.linked_object = linked_object
        self.disabled = disabled

    def set_hover(self, is_mouse_hover: bool) -> None:
        """
        Change the current sprite between sprite or sprite_hover
        depending on whether the mouse is over the element or not.

        Keyword arguments:
        is_mouse_hover -- a boolean value indicating if the mouse is over the element or not
        """
        self.content = self.sprite_hover if is_mouse_hover else self.sprite

    def action_triggered(self) -> Callable:
        """
        Method that should be called after a click.

        Return the callback that should be executed.
        Return a callback doing nothing if the button is disabled.
        """
        if self.disabled:
            return lambda: None
        return self.callback
