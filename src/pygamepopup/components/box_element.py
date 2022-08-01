"""
Defines BoxElement class, useful for drawing elements.
All other components that should be drawn on a popup inherit from this class.
"""

from __future__ import annotations

from typing import Optional

import pygame

from .. import initialization
from .._exceptions.wrong_initialization_exception import WrongInitializationException
from ..types import Position, Margin


class BoxElement:
    """
    This element acts as a wrapper for a gui element.
    In fact, it adds a margin to any border of an element to have a cleaner interface.

    Keyword arguments:
        position (Position): the position of the box on the screen
        content (Optional[pygame.Surface]): a surface that will be wrapped by the box
        margin (Margin): a tuple containing the margins of the box, should be in the form
            "(top_margin, right_margin, bottom_margin, left_margin), defaults to (0, 0, 0, 0)"

    Attributes:
        position (Position): the position of the box on the screen
        content (Optional[pygame.Surface]): the element wrapped in the box
        size (tuple[int, int]): the size of the content following the format "(width, height)"
        margin (dict[str, int]): a dict containing all the values for margins TOP, BOTTOM, LEFT and RIGHT
    """

    def __new__(cls, *args, **kwargs):
        if not initialization._is_initialized:
            raise WrongInitializationException(
                "pygamepopup.init() has to be called before any other interaction with "
                "pygamepopup"
            )
        return super().__new__(cls)

    def __init__(
        self,
        position: Position,
        content: Optional[pygame.Surface],
        margin: Margin = (0, 0, 0, 0),
    ) -> None:
        self.position: Position = position
        self.content: pygame.Surface = content
        self.size: tuple[int, int] = (0, 0)
        if self.content:
            self.size = (self.content.get_width(), self.content.get_height())
        self.margin: dict[str, int] = {
            "TOP": margin[0],
            "BOTTOM": margin[2],
            "LEFT": margin[3],
            "RIGHT": margin[1],
        }

    def get_width(self) -> int:
        """
        Returns:
             int: the width of the content more the left and right margins
        """
        return self.margin["LEFT"] + self.size[0] + self.margin["RIGHT"]

    def get_height(self) -> int:
        """
        Returns:
             int: the height of the content more the top and bottom margins
        """
        return self.margin["TOP"] + self.size[1] + self.margin["BOTTOM"]

    def get_margin_top(self) -> int:
        """
        Returns:
             int: top margin
        """
        return self.margin["TOP"]

    def get_margin_bottom(self) -> int:
        """
        Returns:
             int: bottom margin
        """
        return self.margin["BOTTOM"]

    def get_margin_left(self) -> int:
        """
        Returns:
             int: left margin
        """
        return self.margin["LEFT"]

    def get_margin_right(self) -> int:
        """
        Returns:
             int: right margin
        """
        return self.margin["RIGHT"]

    def get_rect(self) -> pygame.Rect:
        """
        Returns:
             pygame.Rect: a pygame rect containing the position of the element and its size
        """
        return pygame.Rect(
            self.position[0] + self.margin["LEFT"],
            self.position[1] + self.margin["TOP"],
            self.size[0],
            self.size[1],
        )

    def display(self, screen: pygame.Surface) -> None:
        """
        Display the content of the box, following the margins that should be added around it.

        Keyword arguments:
            screen (pygame.Surface): the screen on which the content of the box should be drawn
        """
        screen.blit(
            self.content,
            (
                self.position[0] + self.margin["LEFT"],
                self.position[1] + self.margin["TOP"],
            ),
        )
