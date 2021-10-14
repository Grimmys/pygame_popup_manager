"""
Defines MenuManager class, the main class to handle the displaying of all menus on a screen and
handle the triggering of user events on the elements of the active menu
"""

from typing import Optional, List

import pygame

from .components.info_box import InfoBox
from .types import Position


class MenuManager:
    """
    This class represents a manager for the interfaces of a screen.
    Display all menu currently registered in the manager.
    Handle the opening of a new menu and the closing of the active one.
    Handle the triggering of user motion events and user click events on the active menu.

    Keyword arguments:
    screen -- the screen on which the menus should be displayed and on which the
    user events should be handled

    Attributes:
    screen -- the screen on which the menus should be displayed and on which the
    user events should be handled
    active_menu -- the current menu in the foreground, the only one that will react to user events
    background_menus -- the ordered sequence of menus that are in the background
    """

    def __init__(self, screen: pygame.Surface) -> None:
        self.screen: pygame.Surface = screen
        self.active_menu: Optional[InfoBox] = None
        self.background_menus: List[InfoBox] = []

    def open_menu(self, menu: InfoBox) -> None:
        """
        Open the given menu.
        Initialize the rendering of the menu, and set it as the new active menu.
        Previous active menu is sent to the background.

        Keyword arguments:
        menu -- the popup that should be open
        """
        menu.init_render(self.screen, close_button_callback=lambda: self.close_active_menu())
        if self.active_menu:
            self.background_menus.append(self.active_menu)
        self.active_menu = menu

    def close_active_menu(self) -> None:
        """
        Close the active menu by 'destroying' it.
        Take the next menu in the background to move it to foreground if there is any.
        """
        self.active_menu = (
            self.background_menus.pop() if len(self.background_menus) != 0 else None
        )
        if self.active_menu:
            # Trigger an irrelevant motion event to refresh the hovering of buttons on the new menu
            self.active_menu.motion(pygame.Vector2(pygame.mouse.get_pos()))

    def reduce_active_menu(self) -> None:
        """
        Move the active menu to the background.
        """
        if self.active_menu:
            self.background_menus.append(self.active_menu)
            self.active_menu = None

    def display(self) -> None:
        """
        Display all the visible menus in the background in order first, then display the active menu
        """
        for menu in self.background_menus:
            if menu.visible_on_background:
                menu.display(self.screen)
        if self.active_menu:
            self.active_menu.display(self.screen)

    def click(self, button: int, position: Position) -> None:
        """
        Handle the triggering of a click event.
        Delegate this event to the active menu if there is any and if it's a left click.

        Keyword arguments:
        button -- an integer value representing which mouse button has been pressed
        (1 for left button, 2 for middle button, 3 for right button)
        position -- the position of the mouse
        """
        if button == 1:
            if self.active_menu:
                self.active_menu.click(position)()

    def motion(self, position: Position) -> None:
        """
        Handle the triggering of a motion event.
        Delegate this event to the active menu if there is any.

        Keyword arguments:
        position -- the position of the mouse
        """
        if self.active_menu:
            self.active_menu.motion(position)
