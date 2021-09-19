"""
Defines TextElement class, a BoxElement permitting to easily draw text and let it
be centered on an popup.
"""

import pygame
from pygame.constants import SRCALPHA

from ..configuration import default_fonts
from ..constants import WHITE
from .box_element import BoxElement
from ..types import Position, Margin


class TextElement(BoxElement):
    """
    This class is representing a paragraph of text, displayed on a popup and horizontally
    centered according to its position.

    Keyword arguments:
    text -- the text that should be rendered
    position -- the position of the text on the screen
    font -- the font that should be used to render the text
    margin -- a tuple containing the margins of the box,
    should be in the form "(top_margin, right_margin, bottom_margin, left_margin)"
    text_color -- the color of the rendered text
    """

    def __init__(
        self,
        text: str,
        position: Position = pygame.Vector2(0, 0),
        font: pygame.font.Font = None,
        margin: Margin = (0, 0, 0, 0),
        text_color: pygame.Color = WHITE,
    ) -> None:
        if not font:
            font = default_fonts["text_element_content"]
        self.font = font
        self.text = text
        self.text_color = text_color
        rendered_text: pygame.Surface = font.render(text, True, text_color)
        super().__init__(position, rendered_text, margin)

    def verify_rendered_text_size(
        self, rendered_text: pygame.Surface, text: str, container_width: int
    ) -> pygame.Surface:
        """
        Split a given text in multiple lines until it could fit properly in its container

        Return the final rendered text

        Keyword arguments:
        rendered_text -- the current rendering of the text, to check if it fits in the container
        text -- the text that would be split if necessary
        container_width -- the width of the container
        """
        final_render = rendered_text

        if final_render.get_width() + 20 > container_width:
            first_part, second_part = TextElement.divide_text(text)
            first_part_render = self.font.render(first_part, True, self.text_color)
            first_part_render = self.verify_rendered_text_size(
                first_part_render, first_part, container_width
            )
            second_part_render = self.font.render(second_part, True, self.text_color)
            second_part_render = self.verify_rendered_text_size(
                second_part_render, second_part, container_width
            )
            final_render = pygame.Surface(
                (
                    container_width,
                    first_part_render.get_height() + second_part_render.get_height(),
                ),
                SRCALPHA,
            )
            first_part_x = (
                final_render.get_width() // 2 - first_part_render.get_width() // 2
            )
            final_render.blit(first_part_render, (first_part_x, 0))
            second_part_x = (
                final_render.get_width() // 2 - second_part_render.get_width() // 2
            )
            final_render.blit(
                second_part_render, (second_part_x, first_part_render.get_height())
            )
        return final_render

    @staticmethod
    def divide_text(text: str) -> tuple[str, str]:
        """
        Divide a text in two parts of a similar size, avoiding to cut a word in two.

        Return the split text in two different strings.

        Keyword argument:
        text -- the text that should be divided
        """
        separation_index: int = TextElement.get_middle_text(text)
        return text[:separation_index], text[separation_index:]

    @staticmethod
    def get_middle_text(text: str) -> int:
        """
        Returns the index of the first whitespace character that is after the middle of the provided
        string.
        If there is no whitespace character after the middle of the string, -1 is returned.

        Keyword attributes:
        text -- the string that should be used to make the computation
        """
        absolute_middle = len(text) // 2
        for i in range(absolute_middle, len(text)):
            if text[i] == " ":
                return i
        return -1
