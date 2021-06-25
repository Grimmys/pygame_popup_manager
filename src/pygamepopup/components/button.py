"""
Defines Button class, a BoxElement able to react to user actions.
"""

import pkg_resources
resource_package = 'pygamepopup'
from enum import Enum
from typing import Union, Callable

import pygame

from .box_element import BoxElement
from ..constants import WHITE, BUTTON_SIZE
from ..fonts import fonts
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
    sprite -- the pygame Surface corresponding to the sprite of the element
    sprite_hover -- the pygame Surface corresponding to the sprite of the element
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
        sprite: pygame.Surface = None,
        sprite_hover: pygame.Surface = None,
        margin: Margin = (10, 0, 10, 0),
        linked_object: any = None,
        disabled: bool = False,
        font: pygame.font.Font = None,
    ) -> None:
        super().__init__(position, None, margin)
        self.callback: Union[Enum, Callable] = callback
        self.size: tuple[int, int] = size

        if not font:
            font = fonts["DEFAULT_FONT"]
        title = font.render(title, True, WHITE)

        raw_sprite = (
            sprite if sprite else pygame.image.load(pkg_resources.resource_filename(resource_package, '/'.join(('images', 'default_box.png'))))
        )
        sprite = pygame.transform.scale(raw_sprite.convert_alpha(), size)
        sprite.blit(
            title,
            (
                sprite.get_width() // 2 - title.get_width() // 2,
                sprite.get_height() // 2 - title.get_height() // 2,
            ),
        )
        raw_sprite_hover = (
            sprite_hover
            if sprite_hover
            else pygame.image.load(pkg_resources.resource_filename(resource_package, '/'.join(('images', 'default_box_hover.png'))))
        )
        sprite_hover = pygame.transform.scale(raw_sprite_hover.convert_alpha(), size)
        sprite_hover.blit(
            title,
            (
                sprite_hover.get_width() // 2 - title.get_width() // 2,
                sprite_hover.get_height() // 2 - title.get_height() // 2,
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
