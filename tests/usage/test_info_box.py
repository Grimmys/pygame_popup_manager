import pytest

from src.pygamepopup.components import InfoBox, Button


@pytest.fixture
def sample_menu():
    return InfoBox(
        title="My Test Menu",
        element_grid=[[Button(title="A sample button", callback=lambda: None)]],
    )


def test_minimal_infobox_init(sample_menu):
    title = "My Test Menu"
    row = [Button(title="A sample button", callback=lambda: None)]
    element_grid = [row]
    assert title == sample_menu.title
    assert len(sample_menu.element_grid) == len(element_grid) and len(
        sample_menu.element_grid[0]
    ) == len(row)
    assert sample_menu.has_close_button
    assert sample_menu.visible_on_background


def test_can_be_rendered_multiple_times(sample_menu, screen):
    sample_menu.init_render(screen)
    sample_menu.init_render(screen)


def test_display_on_screen(sample_menu, screen):
    sample_menu.init_render(screen)
    sample_menu.display(screen)
