Getting started
===============

Installation
------------

The easiest way to install this package is to do it with pip:

.. code-block:: console

   (.venv) $ pip install pygame-popup

Use
-------------

:func:`pygamepopup.init` function should be call right after
:func:`pygame.init` function in your code and before any further usage of elements coming from Pygame Popup Manager.

The whole system is working around the :class:`MenuManager <pygamepopup.menu_manager.MenuManager>` class that is the controller of all the popups in background and in foreground.

An unique instance per scene/window has to be created and the pygame screen on which the popups will appear should be provided, like this:

.. code-block:: python

    from pygamepopup.menu_manager import MenuManager

    screen = pygame.display.set_mode(WINDOW_SIZE)

    menu_manager = MenuManager(screen)

The :meth:`display <pygamepopup.menu_manager.MenuManager.display>`, :meth:`motion <pygamepopup.menu_manager.MenuManager.motion>` and :meth:`click <pygamepopup.menu_manager.MenuManager.click>` methods of this class should be called in the application main loop in order to notify the manager of any pygame event.

To open a new popup menu, you should first create it by instantiate the :class:`InfoBox <pygamepopup.components.info_box.InfoBox>` class.
The components that should be in the menu should be provided.

Next, don't forget to call the :meth:`open_menu <pygamepopup.menu_manager.MenuManager.open_menu>` method of the menu manager to notify it about the new menu.

For example, the following code will open a popup with a "do-nothing" button and a close button (added by default by the :class:`InfoBox <pygamepopup.components.info_box.InfoBox>`).

.. code-block:: python

    from pygamepopup.components import Button, InfoBox

    my_custom_menu = InfoBox(
        "Title of the Menu",
        [
            Button(
                title="Hello World!",
                callback=lambda: None
            )
        ]
    )

    menu_manager.open_menu(my_custom_menu)

If you want more code illustrations, go check out the :doc:`examples`.