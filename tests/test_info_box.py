import pytest

from src.pygamepopup.components import InfoBox, Button


class TestInfoBox:
    @pytest.fixture
    def sample_menu(self):
        return InfoBox(
            title="My Test Menu",
            element_grid=[
                [Button(title="A sample button", callback=lambda: None)]
            ])

    def test_minimal_infobox_init(self, sample_menu):
        title = "My Test Menu"
        row = [
            Button(title="A sample button", callback=lambda: None)
        ]
        element_grid = [row]
        assert title == sample_menu.title
        assert len(sample_menu.element_grid) == len(element_grid) and len(sample_menu.element_grid[0]) == len(row)
        assert sample_menu.has_close_button
        assert sample_menu.visible_on_background

    @pytest.mark.skip(reason="not implemented yet")
    def test_can_be_rendered_multiple_times(self, sample_menu, screen):
        sample_menu.init_render(screen)
        sample_menu.init_render(screen)
