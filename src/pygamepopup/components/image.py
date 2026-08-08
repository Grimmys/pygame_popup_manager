"""Provide a popup component for displaying an image.

The :class:`Image` component renders an image inside a transparent
:class:`~pygamepopup.components.box_element.BoxElement`, leaving a small
padding around the image and sizing the component according to the supplied
dimensions.
"""

from __future__ import annotations

import pygame
from pygame.constants import SRCALPHA
from pygame.surface import Surface

from .box_element import BoxElement
from ..constants import IMAGE_SIZE
from ..type_definitions import Position, Margin


class Image(BoxElement):
    """
    Represents an image, displayed horizontally on a popup and
    centered according to its position.

    Keyword arguments:
        image_path (str): the relative path to the image that should be displayed.
        size (tuple[int, int]): the size of the image following the format "(width, height)",
            defaults to :const:`~pygamepopup.constants.IMAGE_SIZE`.
        position (Position): the position of the image on the screen.
        margin (Margin): a tuple containing the margins of the box,
            should be in the form "(top_margin, right_margin, bottom_margin, left_margin)", defaults to (0, 0, 0, 0).
        column_span (int): the number of columns the element should span, defaults to 1.
    """

    def __init__(
        self,
        image_path: str,
        size: tuple[int, int] = IMAGE_SIZE,
        position: Position = pygame.Vector2(0, 0),
        margin: Margin = (0, 0, 0, 0),
        column_span: int = 1,
    ) -> None:
        super().__init__(position, Surface(size, flags=SRCALPHA), margin, column_span)
        padding: int = self.size[1] // 10
        image = pygame.transform.scale(
            pygame.image.load(image_path),
            (self.size[0] - padding * 2, self.size[1] - padding * 2),
        )
        self.content.blit(image, pygame.Vector2(padding, padding))
