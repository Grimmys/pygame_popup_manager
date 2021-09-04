import pygame
import pygamepopup
from pygamepopup.components import Button, InfoBox, TextElement
from pygamepopup.menu_manager import MenuManager

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600


class MainMenuScene:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.menu_manager = MenuManager(screen)
        self.exit_request = False

        self.create_main_menu_interface()

    def create_main_menu_interface(self):
        main_menu = InfoBox(
            "Main Menu",
            [
                [
                    Button(
                        title="Open other menu",
                        callback=lambda: self.create_other_menu(),
                    )
                ],
                [
                    Button(
                        title="Exit",
                        callback=lambda: self.exit())
                ],
            ],
            has_close_button=False
        )
        self.menu_manager.open_menu(main_menu)

    def create_other_menu(self):
        other_menu = InfoBox(
            "Smaller menu",
            [
                [
                    TextElement(
                        text="The text content of a menu is automatically splitted in multiple "
                             "part "
                             "to fit in the box. To add a new paragraph, just create another "
                             "TextElement."
                    )
                ]
            ],
            width=300
        )
        self.menu_manager.open_menu(other_menu)

    def exit(self):
        self.exit_request = True

    def display(self) -> None:
        self.menu_manager.display()

    def motion(self, position: pygame.Vector2) -> None:
        self.menu_manager.motion(position)

    def click(self, button: int, position: pygame.Vector2) -> bool:
        self.menu_manager.click(button, position)
        return self.exit_request


def main() -> None:
    pygame.init()
    pygame.display.set_caption("Main Menu Example")

    pygamepopup.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    main_menu_scene = MainMenuScene(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION:
                main_menu_scene.motion(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    running = not main_menu_scene.click(event.button, event.pos)
        screen.fill(pygame.Color("black"))
        main_menu_scene.display()
        pygame.display.update()
    pygame.quit()
    exit()


if __name__ == "__main__":
    main()
