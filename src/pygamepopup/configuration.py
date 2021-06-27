import os
import pkg_resources

resource_package = __name__

default_sprites = {
    "button_background": {
        "inactive": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box.png"))
        ),
        "active": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box_hover.png"))
        ),
    },
    "dynamic_button_background": {
        "inactive": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box.png"))
        ),
        "active": pkg_resources.resource_filename(
            resource_package, "/".join(("images", "default_box_hover.png"))
        ),
    },
    "info_box_background": pkg_resources.resource_filename(
        resource_package, "/".join(("images", "default_box.png"))
    ),
}


def set_button_background(
    button_background_path: str, button_hovered_background_path: str
) -> None:
    default_sprites["button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    default_sprites["button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_dynamic_button_background(
    button_background_path: str, button_hovered_background_path: str
) -> None:
    default_sprites["dynamic_button_background"]["inactive"] = os.path.abspath(
        button_background_path
    )
    default_sprites["dynamic_button_background"]["active"] = os.path.abspath(
        button_hovered_background_path
    )


def set_info_box_background(info_box_background_path: str) -> None:
    default_sprites["info_box_background"] = os.path.abspath(info_box_background_path)
