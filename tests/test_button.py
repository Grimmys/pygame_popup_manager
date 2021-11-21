from pygamepopup.components import Button
from tests.pygamepopup_test_setup import PygamepopupTestSetup


class TestButton(PygamepopupTestSetup):
    def test_standard_button_init(self):
        title = "My Test Button"
        callback = lambda: print("Hello World!")
        button = Button(title=title, callback=callback)

        assert button.callback == callback
