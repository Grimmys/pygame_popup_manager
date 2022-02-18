InfoBox
==============

.. py:module:: info_box

.. py:class:: InfoBox

    This class is defining any kind of popup that can be found in the app.

    It can be used to represent the interface of a menu, or a simple text message.
    Some elements can be buttons, that will react to user clicks (see the button component
    for more information).

    :param str title: The title of the infoBox.
    :param list[list[BoxElement]] element_grid: A grid containing the components that should be rendered by the infoBox.
    :param int width: The width of the infoBox, defaults to DEFAULT_POPUP_WIDTH.
    :param pygame.Rect element_linked: The pygame Rect of the element linked to this infoBox, the infoBox will be displayed beside the element if provided.
    :param bool has_close_button: Whether a close button should be added at the bottom or not.
    :param pygame.Color title_color: The color of the title, defaults to WHITE.
    :param str background_path: The path corresponding to the image that should be the sprite of the infoBox.
    :param str close_button_sprite: The path to the image corresponding to the sprite of the close button if there should be one.
    :param str close_button_sprite_hover: The path to the image corresponding to the sprite of the close button when it is hovered if there should be one.
    :param bool visible_on_background: Whether the popup is visible on background or not, defaults to True.
    :param bool has_vertical_separator: Whether there should be a line splitting the infoBox in two at middle width or not, defaults to False.
    :param str identifier: A string permitting to identify the menu among others if needed, defaults to empty string

    .. py:method:: init_render(self, screen, close_button_callback)

        Initialize the rendering of the popup.

        Compute it size and its position according to the given screen.
        Determine the position of each component.

        :param pygame.Surface screen: The screen on which the popup is.
        :param Callable close_button_callback: The callback that should be executed when clicking on the close button, defaults to a callback only closing the popup.
        :rtype: None

    .. py:method:: init_elements(self)

        Initialize the graphical elements associated to the formal data that the infoBox should represent.

        :return: The elements in a 2D structure corresponding to the relative position of each element.
        :rtype: list[_Row]

    .. py:method:: determine_position(self, screen)

        Compute the position of the infoBox to be beside the linked element.

        If no element is linked to the infoBox, the position will be determine at display time
        according to the screen.

        :param pygame.Surface screen: The screen on which the infoBox is rendered.
        :return: The Computed position.
        :rtype: Optional[Position]

    .. py:method:: find_buttons(self)

        Search in all elements for buttons.

        :return: The found buttons.
        :rtype: Sequence[Button]

    .. py:method:: determine_elements_position(self)

        Compute the position of each element and update it if needed.

        :rtype: None

    .. py:method:: display(self)

        Display the infoBox and all its elements.

        :param pygame.Surface screen: The screen on which the displaying should be done.
        :rtype: None

    .. py:method:: click(self, position)

        Handle the triggering of a click event.

        :param Position position: The position of the mouse.
        :return: The data corresponding to the action that should be done if the click was done on a button, else None.
        :rtype: Optional[Callable]

    .. py:method:: motion(self, position)

        Handle the triggering of a motion event.
        Test if the mouse entered in a button or left one.

        :param Position position: The position of the mouse.
        :rtype: None