from src.pygamepopup.components import Button


def test_standard_button_init():
    title = "My Test Button"
    callback = lambda: print("Hello World!")
    button = Button(title=title, callback=callback)

    assert button.callback == callback


def test_button_hitbox_does_not_include_margin():
    title = "My Test Button"
    callback = lambda: print("Hello World!")
    margin = (10, 10, 10, 10)
    size = (40, 40)
    button = Button(title=title, callback=callback, margin=margin, size=size)
    position_in_margin = (margin[0] // 2, margin[1] // 2)
    assert not button.get_rect().collidepoint(position_in_margin)
    position_inside_button_box = (margin[0] + size[0] // 2, margin[1] + size[1] // 2)
    assert button.get_rect().collidepoint(position_inside_button_box)
    position_bottom_right_button_box = (
        margin[0] + size[0] - 1,
        margin[1] + size[1] - 1,
    )
    assert button.get_rect().collidepoint(position_bottom_right_button_box)
