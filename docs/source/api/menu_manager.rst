Menu Manager
==============

.. py:module:: menu_manager

.. py:class:: MenuManager

    This class represents a manager for the interfaces of a screen.

    It display all the menus currently registered in the manager.

    Handle the opening of a new menu and the closing of the active one.
    Handle the triggering of user motion events and user click events on the active menu.

    :param pygame.Surface screen: The screen on which the menus should be displayed and on which the user events should be handle
    :ivar pygame.Surface screen: The screen on which the menus should be displayed and on which the user events should be handled
    :ivar Optional[InfoBox] active_menu: The current menu in the foreground, the only one that will react to user events.
    :ivar list[InfoBox] background_menus: The ordered sequence of menus that are in the background.

    .. py:method:: open_menu(self, menu)

        Open the given menu.
        Initialize the rendering of the menu, and set it as the new active menu.

        Previous active menu is sent to the background.

        :param InfoBox menu: The popup that should be open.
        :rtype: None

    .. py:method:: replace_given_menu(self, menu_identifier, new_menu, all_occurrences)

        Replace a menu by a new one according to its identifier.
        By default, only first occurrence
        is replaced if many menus in the manager have the given identifier.

        :param str menu_identifier: The identifier of the menu to be replaced.
        :param InfoBox new_menu: The menu that should replace the given one
        :param bool all_occurrences: Whether all found occurrences should be replaced or only the first one, defaults to false.
        :return: Whether the replacement has succeeded or not.
        :rtype: bool

    .. py:method:: close_active_menu(self)

        Close the active menu by 'destroying' it.
        Take the next menu in the background to move it to foreground if there is any.

        :rtype: None

    .. py:method:: close_given_menu(self, menu_identifier, all_occurrences)

        Close menu corresponding to the given identifier.
        By default, only first occurrence is closed if many menus in the manager have the given identifier.

        :param str menu_identifier: The identifier of the menu to be closed.
        :param bool all_occurrences: Whether all found occurrences should be closed or only the first one, defaults to false.
        :return: Whether at least one menu has been closed or not.
        :rtype: bool

    .. py:method:: clear_menus(self)

        Close all the menus (in foreground and in background).

        :rtype: None

    .. py:method:: reduce_active_menu(self)

        Move the active menu to the background.

        :rtype: None

    .. py:method:: display(self)

        Display all the visible menus in the background in order first, then display the active menu.

        :rtype: None

    .. py:method:: click(self, button, position)

        Handle the triggering of a click event.
        Delegate this event to the active menu if there is any and if it's a left click.

        :param int button: An integer value representing which mouse button has been pressed (1 for left button, 2 for middle button, 3 for right button).
        :param Position position: The position of the mouse.
        :rtype: None

    .. py:method:: motion(self, position)

        Handle the triggering of a motion event.
        Delegate this event to the active menu if there is any.

        :param Position position: The position of the mouse.
        :rtype: None