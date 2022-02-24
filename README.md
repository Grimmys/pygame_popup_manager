# Pygame Popup Manager

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![dl-pypi](https://img.shields.io/pypi/dm/pygame-popup)](https://pypi.org/project/pygame-popup/)
[![license](https://img.shields.io/github/license/grimmys/pygame_popup_manager)](https://github.com/Grimmys/pygame_popup_manager/blob/main/LICENSE)
[![version](https://img.shields.io/pypi/v/pygame-popup)](https://pypi.org/project/pygame-popup/)

Docs are now available at: https://pygame-popup-manager.readthedocs.io/en/latest/

Pygame Popup Manager is a very small engine permitting to easily build all kind of popup in a pygame project.

Here is an example of basic menus that could be created with this manager:

![Main menu with side menu](https://github.com/Grimmys/pygame_popup_manager/blob/main/screenshots/main_menu_with_side_menu.png)
# Installation

The easiest way to install this package is to do it with `pip`:

`pip install pygame-popup`

# Use

First, don't forget to call `pygamepopup.init` function right after 
calling `pygame.init` function.

The whole system is working around the `MenuManager` class that is
the controller of all the popups in background and in foreground.

An unique instance per scene/window has to be created and the pygame screen
on which the popups will appear should be provided, like this:

```py
from pygamepopup.menu_manager import MenuManager

menu_manager = MenuManager(screen)
```

The `display`, `motion` and `click` methods of this class should be called in the application main loop 
in order to notify the manager of any pygame event.

To open a new popup menu, you should first create it by instantiate the `InfoBox` class.
The components that should be in the menu should be provided.
Next, don't forget to call the `open_menu` method of the menu manager to notify it about the new menu.

For example, the following code will open a popup with a "do-nothing" button and a close button (added by default by the `InfoBox`)

```py
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
```
If you want more code illustrations, check the `examples/minimal_main_menu.py` module.

# Customization

The default graphics resources can be easily changed by your own by simply calling certain methods of the `configuration` module, wherever you want, as can be seen below. 

```py
import pygamepopup

pygamepopup.configuration.set_button_background("sprites/inactive_button.png",
                                                "sprites/active_button.png")
pygamepopup.configuration.set_dynamic_button_background("sprites/inactive_button.png",
                                                        "sprites/active_button.png")
pygamepopup.configuration.set_info_box_background("sprites/menu_box.png")
```

It is also possible to directly provide an asset to a specific component, if you want a button to be different from others for example.

```py
Button(
    title="Hello World!",
    callback=lambda: None,
    sprite=pygame.image.load("sprites/different_button.png"),
    sprite_hover=pygame.image.load("sprites/different_button_hover.png")
)
 ```

With this kind of configuration you can made an interface similar to this one: 

![Options menu with assets](https://github.com/Grimmys/pygame_popup_manager/blob/main/screenshots/options_menu_with_assets.png)

# Contact

You can contact me directly by [e-mail](mailto:grimmys.programming@gmail.com?subject=[GitHub]%20Pygame%20Popup%20Manager) if you have any question regarding the package.
Also, I will be really happy to know you are using this package, so don't hesitate to share me the link to your project if you tried something!

For suggestions or bugs, please create an issue in the GitHub repository: https://github.com/Grimmys/pygame_popup_manager/issues

Thanks!
