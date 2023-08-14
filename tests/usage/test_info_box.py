import pytest

from src.pygamepopup.components import InfoBox, Button

STATIC_MENU_POSITION = (10, 20)


@pytest.fixture
def sample_menu():
    return InfoBox(
        title="My Test Menu",
        element_grid=[[Button(title="A sample button", callback=lambda: None)]],
    )


@pytest.fixture
def static_menu(screen, request):
    static_menu = InfoBox(
        title="My Test Menu",
        element_grid=[[Button(title="A sample button", callback=lambda: None)]],
        position=request.param
    )
    static_menu.init_render(screen)
    static_menu.display(screen)
    return static_menu


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


@pytest.mark.parametrize("static_menu", [STATIC_MENU_POSITION], indirect=True)
def test_position_is_static_when_providing_specific_position_at_init(screen, static_menu):
    assert static_menu.position == STATIC_MENU_POSITION


@pytest.mark.skip(reason="not implemented yet")
@pytest.mark.parametrize("static_menu", [(0, 0)], indirect=True)
def test_is_position_inside_when_position_is_outside_info_box(screen, static_menu):
    far_away_position = (1200, 1300)
    assert not static_menu.is_position_inside(far_away_position)


@pytest.mark.skip(reason="not implemented yet")
@pytest.mark.parametrize("static_menu", [(0, 0)], indirect=True)
def test_is_position_inside_when_position_is_inside_info_box(screen, static_menu):
    inside_position = (20, 20)
    assert static_menu.is_position_inside(inside_position)
