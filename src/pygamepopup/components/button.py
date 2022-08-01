"""
Defines Button class, a BoxElement able to react to user actions.
"""

from __future__ import annotations

import os.path
from enum import Enum
from typing import Union, Callable, Sequence

import pygame

from ..configuration import _default_sprites, _default_fonts
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
        callback (Callable): the reference to the function that should be call after a click.
        size (tuple[int, int]): the size of the button following the format "(width, height)", defaults to BUTTON_SIZE.
        title (str): the text that should be displayed at the center of the element.
        position (Position): the position of the element on the screen.
        background_path (str): the path to the image corresponding to the sprite of the element.
        background_hover_path (str): the path to the image corresponding to the sprite of the element
            when it has the focus.
        no_background (bool): specify whether a background should be present or not, defaults to False.
        margin (Margin): a tuple containing the margins of the box,
            should be in the form "(top_margin, right_margin, bottom_margin, left_margin)", defaults to (0, 0, 0, 0).
        disabled (bool): a boolean indicating if it is not possible to interact with the button, defaults to False.
        font (pygame.font.Font): the font that should be used to render the text content.
        text_color (pygame.Color): the color of the text content, defautls to WHITE.
        font_hover (pygame.font.Font): the font that should be used to render the text content when the mouse is over
            the button.
        text_hover_color (pygame.Color): the color of the text content when the mouse is over the button,
            defaults to WHITE.
        complementary_text_lines (str): the other text lines that should be displayed in addition of
            the title.

    Attributes:
        callback (Callable): the reference to the function that should be call after a click.
        sprite (pygame.Surface): the pygame Surface corresponding to the sprite of the element.
        sprite_hover (pygame.Surface): the pygame Surface corresponding to the sprite of the element
            when it has the focus.
    """

    def __init__(
        self,
        callback: Callable = lambda: None,
        size: tuple[int, int] = BUTTON_SIZE,
        title: str = "",
        position: Position = pygame.Vector2(0, 0),
        background_path: str = None,
        background_hover_path: str = None,
        no_background: bool = False,
        margin: Margin = (0, 0, 0, 0),
        disabled: bool = False,
        font: pygame.font.Font = None,
        text_color: pygame.Color = WHITE,
        font_hover: pygame.font.Font = None,
        text_hover_color: pygame.Color = WHITE,
        complementary_text_lines: Sequence[str] = None,
    ) -> None:
        super().__init__(position, None, margin)
        self.callback: Union[Enum, Callable] = callback
        self.size: tuple[int, int] = size

        if complementary_text_lines is None:
            complementary_text_lines = []
        text_lines = [title] + complementary_text_lines

        if not font:
            font = _default_fonts["button_title"]
        rendered_text_lines = Button.render_text_lines(text_lines, text_color, font)
        if no_background:
            self.size = (
                rendered_text_lines[0].get_width(),
                rendered_text_lines[0].get_height() * len(rendered_text_lines),
            )

        if no_background:
            background_path = None
        elif background_path:
            background_path = os.path.abspath(background_path)
        else:
            background_path = _default_sprites["button_background"]["inactive"]
        self.sprite = self.render_sprite(background_path, rendered_text_lines)

        if not font_hover:
            font_hover = font
        rendered_text_lines_hover = Button.render_text_lines(
            text_lines, text_hover_color, font_hover
        )

        if no_background:
            background_hover_path = None
        elif background_hover_path:
            background_hover_path = os.path.abspath(background_hover_path)
        else:
            background_hover_path = _default_sprites["button_background"]["active"]
        self.sprite_hover = self.render_sprite(
            background_hover_path, rendered_text_lines_hover
        )

        self.content = self.sprite
        self.disabled = disabled

    @staticmethod
    def render_text_lines(
        text_lines: Sequence[str],
        text_color: pygame.Color,
        font: pygame.font.Font,
    ) -> Sequence[pygame.Surface]:
        """
        Compute the rendering of the given text.

        Returns:
            Sequence[pygame.Surface]: the rendered text lines.

        Keyword arguments:
            text_lines (Sequence[str]): the sequence in order of text lines to be rendered.
            text_color (pygame.Color): the color of the text.
            font (pygame.font.Font): the font that should be used to render the text.
        """
        return [font.render(text_line, True, text_color) for text_line in text_lines]

    def render_sprite(
        self, background_path: str, rendered_text_lines: Sequence[pygame.Surface]
    ) -> pygame.Surface:
        """
        Compute the rendering of the button with the given background and text lines.
        If no background is provided, render the text on an empty surface.

        Returns:
             pygame.Surface: the generated surface.

        Keyword arguments:
            background_path (str): the path to the image corresponding to the sprite of the button.
            rendered_text_lines (Sequence[pygame.Surface]): the sequence of text lines in order that should be clipped
                on the surface.
        """
        raw_sprite = (
            pygame.image.load(background_path)
            if background_path
            else pygame.Surface((0, 0))
        )
        sprite = pygame.transform.scale(raw_sprite.convert_alpha(), self.size)
        text_lines_count = len(rendered_text_lines)

        for index, rendered_text_line in enumerate(rendered_text_lines):
            sprite.blit(
                rendered_text_line,
                (
                    sprite.get_width() // 2 - rendered_text_line.get_width() // 2,
                    (2 * index + 1) * sprite.get_height() // (2 * text_lines_count)
                    - rendered_text_line.get_height() // 2,
                ),
            )
        return sprite

    def set_hover(self, is_mouse_hover: bool) -> None:
        """
        Change the current sprite between sprite or sprite_hover
        depending on whether the mouse is over the element or not.

        Keyword arguments:
            is_mouse_hover (bool): a boolean value indicating if the mouse is over the element or not
        """
        self.content = self.sprite_hover if is_mouse_hover else self.sprite

    def action_triggered(self) -> Callable:
        """
        Method that should be called after a click.

        Returns:
             Callable: the callback that should be executed, a callback doing nothing would be returned
             if the button is disabled.
        """
        if self.disabled:
            return lambda: None
        return self.callback
