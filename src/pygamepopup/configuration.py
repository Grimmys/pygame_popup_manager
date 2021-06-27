import pkg_resources

resource_package = __name__

default_sprites = {
    "button_background": {
        "inactive": pkg_resources.resource_filename(resource_package,
                                                    '/'.join(('images', 'default_box.png'))),
        "active": pkg_resources.resource_filename(resource_package,
                                                  '/'.join(('images', 'default_box_hover.png')))
    },
    "dynamic_button_background": {
        "inactive": pkg_resources.resource_filename(resource_package,
                                                    '/'.join(('images', 'default_box.png'))),
        "active": pkg_resources.resource_filename(resource_package,
                                                  '/'.join(('images', 'default_box_hover.png')))
    },
    "info_box_background": pkg_resources.resource_filename(resource_package, '/'.join(
        ('images', 'default_box.png')))
}