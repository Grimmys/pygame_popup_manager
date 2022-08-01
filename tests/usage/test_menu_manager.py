import pytest

from src.pygamepopup.components import InfoBox, Button
from src.pygamepopup.menu_manager import MenuManager


@pytest.fixture
def sample_menu():
    return InfoBox(
        title="My Test Menu",
        element_grid=[[Button(title="A sample button", callback=lambda: None)]],
    )


@pytest.fixture
def other_menu():
    return InfoBox(
        title="My New Menu",
        element_grid=[[Button(title="A different button", callback=lambda: None)]],
    )


@pytest.fixture
def menu_with_identifier():
    return InfoBox(
        title="My Special Menu",
        element_grid=[[Button(title="A sample button", callback=lambda: None)]],
        identifier="UnicMenuIdentifier",
    )


@pytest.fixture
def sample_menu_manager(screen):
    return MenuManager(screen)


def test_menu_manager_init(screen, sample_menu_manager):
    assert screen == sample_menu_manager.screen
    assert not sample_menu_manager.active_menu
    assert not sample_menu_manager.background_menus


def test_replace_existing_menu(
    sample_menu_manager, sample_menu, other_menu, menu_with_identifier
):
    sample_menu_manager.background_menus = [
        sample_menu,
        sample_menu,
        menu_with_identifier,
        sample_menu,
    ]

    has_replacement_been_done = sample_menu_manager.replace_given_menu(
        "UnicMenuIdentifier", other_menu
    )

    assert has_replacement_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        other_menu,
        sample_menu,
    ]


def test_replacement_is_for_active_menu(
    sample_menu_manager, sample_menu, other_menu, menu_with_identifier
):
    sample_menu_manager.active_menu = menu_with_identifier
    sample_menu_manager.background_menus = [sample_menu, sample_menu, sample_menu]

    has_replacement_been_done = sample_menu_manager.replace_given_menu(
        "UnicMenuIdentifier", other_menu
    )

    assert has_replacement_been_done
    assert sample_menu_manager.active_menu == other_menu
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        sample_menu,
    ]


def test_does_not_replace_missing_menu(sample_menu_manager, sample_menu, other_menu):
    sample_menu_manager.background_menus = [sample_menu, sample_menu, sample_menu]

    has_replacement_been_done = sample_menu_manager.replace_given_menu(
        "UnicMenuIdentifier", other_menu
    )

    assert not has_replacement_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        sample_menu,
    ]


def test_replace_first_occurrence_if_existing_menu_is_present_twice(
    sample_menu_manager, sample_menu, other_menu, menu_with_identifier
):
    sample_menu_manager.background_menus = [
        sample_menu,
        menu_with_identifier,
        menu_with_identifier,
        sample_menu,
    ]

    has_replacement_been_done = sample_menu_manager.replace_given_menu(
        "UnicMenuIdentifier", other_menu
    )

    assert has_replacement_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        other_menu,
        menu_with_identifier,
        sample_menu,
    ]


def test_replace_all_occurrences(
    sample_menu_manager, sample_menu, other_menu, menu_with_identifier
):
    sample_menu_manager.background_menus = [
        sample_menu,
        menu_with_identifier,
        menu_with_identifier,
        sample_menu,
    ]

    has_replacement_been_done = sample_menu_manager.replace_given_menu(
        "UnicMenuIdentifier", other_menu, all_occurrences=True
    )

    assert has_replacement_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        other_menu,
        other_menu,
        sample_menu,
    ]


def test_close_existing_menu(sample_menu_manager, sample_menu, menu_with_identifier):
    sample_menu_manager.background_menus = [
        sample_menu,
        sample_menu,
        menu_with_identifier,
        sample_menu,
    ]

    has_closing_been_done = sample_menu_manager.close_given_menu("UnicMenuIdentifier")

    assert has_closing_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        sample_menu,
    ]


def test_closing_is_for_active_menu(
    sample_menu_manager, sample_menu, menu_with_identifier
):
    sample_menu_manager.active_menu = menu_with_identifier
    sample_menu_manager.background_menus = [sample_menu, sample_menu, sample_menu]

    has_closing_been_done = sample_menu_manager.close_given_menu("UnicMenuIdentifier")

    assert has_closing_been_done
    assert not sample_menu_manager.active_menu
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        sample_menu,
    ]


def test_does_not_close_missing_menu(sample_menu_manager, sample_menu):
    sample_menu_manager.background_menus = [sample_menu, sample_menu, sample_menu]

    has_closing_been_done = sample_menu_manager.close_given_menu("UnicMenuIdentifier")

    assert not has_closing_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        sample_menu,
        sample_menu,
    ]


def test_close_first_occurrence_if_existing_menu_is_present_twice(
    sample_menu_manager, sample_menu, menu_with_identifier
):
    sample_menu_manager.background_menus = [
        sample_menu,
        menu_with_identifier,
        menu_with_identifier,
        sample_menu,
    ]

    has_closing_been_done = sample_menu_manager.close_given_menu("UnicMenuIdentifier")

    assert has_closing_been_done
    assert sample_menu_manager.background_menus == [
        sample_menu,
        menu_with_identifier,
        sample_menu,
    ]


def test_close_all_occurrences(sample_menu_manager, sample_menu, menu_with_identifier):
    sample_menu_manager.background_menus = [
        sample_menu,
        menu_with_identifier,
        menu_with_identifier,
        sample_menu,
    ]

    has_closing_been_done = sample_menu_manager.close_given_menu(
        "UnicMenuIdentifier", all_occurrences=True
    )

    assert has_closing_been_done
    assert sample_menu_manager.background_menus == [sample_menu, sample_menu]
