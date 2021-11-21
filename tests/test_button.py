from src.pygamepopup.components import Button


def test_standard_button_init():
    title = "My Test Button"
    callback = lambda: print("Hello World!")
    button = Button(title=title, callback=callback)

    assert button.callback == callback
