# pygamepopup simple demo
# Contains 2 menus, independently controllable by keyboard or button
import pygame
import pygamepopup
from pygamepopup.components import Button, InfoBox, TextElement
from pygamepopup.constants import BUTTON_SIZE
from pygamepopup.menu_manager import MenuManager

MAIN_MENU_ID = "main_menu"
CLOSABLE_MENU_ID = "closable_menu"
CUSTOMIZED_MENU_ID = "customized_menu"
SIDE_MENU_ID = "side_menu"

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 30
clock = pygame.time.Clock()

BALL_RADIUS = 10
x_pos = 250
y_pos = 150
x_velocity = 5
y_velocity = -5

# initialize pygame
pygame.init()
pygame.display.set_caption("Main Menu Example")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# initialize pygamepopup
pygamepopup.init()
menu_manager = MenuManager(screen)

# Define a main menu popup, with 4 buttons and a close button
main_menu = InfoBox(
    "Main Menu",
    [
        [
            Button(
                title="Open side menu",
                callback=lambda: menu_manager.open_menu(side_menu),
                size=(320, BUTTON_SIZE[1]),
            )
        ],
        [
            Button(
                title="Open closable menu",
                callback=lambda: menu_manager.open_menu(closable_menu),
                size=(320, BUTTON_SIZE[1]),
            )
        ],
        [
            Button(
                title="Open customized menu",
                callback=lambda: menu_manager.open_menu(customized_menu),
                size=(320, BUTTON_SIZE[1]),
            )
        ],
        [Button(title="Exit App", callback=lambda: exit(), size=(320, BUTTON_SIZE[1]))],
    ],
    width=420,
    identifier=MAIN_MENU_ID,
)

# Define submenu that can be closed by clicking outside
closable_menu = InfoBox(
    "Closable menu",
    [
        [
            TextElement(
                text="This menu can be close by clicking on the \"Close\" button but also by clicking outside of it."
            )
        ]
    ],
    width=350,
    identifier=CLOSABLE_MENU_ID,
)

customized_menu = InfoBox(
    "Customized menu",
    [
        [
            TextElement(
                text="This menu has customized content, such as close button with different label"
            )
        ]
    ],
    width=400,
    identifier=CUSTOMIZED_MENU_ID,
    title_color=pygame.Color("red"),
    close_button_text="Shutdown!"
)

# Define a side menu, with relative positioning and close button
side_menu = InfoBox(
    "Smaller menu",
    [
        [
            TextElement(
                text="The text content of a menu is automatically split in multiple "
                "parts "
                "to fit in the box. To add a new paragraph, just create another "
                "TextElement."
            )
        ]
    ],
    element_linked=pygame.Rect(0, WINDOW_HEIGHT // 2, 1, 1),
    width=310,
    identifier=SIDE_MENU_ID,
)


def display_main_screen():
    global x_pos, y_pos, x_velocity, y_velocity
    screen.fill(pygame.Color("tan"))
    font = pygame.font.Font(None, 36)
    text = font.render(
        "Type M to open Main Menu or S to open Side Menu", True, (100, 100, 20)
    )
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 40))

    # Draw animated Ball
    pygame.draw.circle(screen, pygame.Color("red"), (x_pos, y_pos), BALL_RADIUS, 0)
    x_pos += x_velocity
    y_pos += y_velocity

    if x_pos > WINDOW_WIDTH - BALL_RADIUS or x_pos < BALL_RADIUS:
        x_velocity *= -1
    if y_pos > WINDOW_HEIGHT - BALL_RADIUS or y_pos < BALL_RADIUS:
        y_velocity *= -1


def show_menu(menu):
    # display a menu if it is not already open
    if menu_manager.active_menu is not None:
        if menu_manager.active_menu.identifier == menu.identifier:
            print("Given menu is already opened")
            return
        else:
            menu_manager.close_active_menu()
    menu_manager.open_menu(menu)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    show_menu(side_menu)
                if event.key == pygame.K_m:
                    show_menu(main_menu)
                if event.key == pygame.K_b:
                    print(
                        f"Menus in the background stack: {menu_manager.background_menus}"
                    )
                if event.key == pygame.K_a:
                    print(f"Active menu: {menu_manager.active_menu}")
            elif event.type == pygame.MOUSEMOTION:
                menu_manager.motion(event.pos)  # Highlight buttons upon hover
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    if menu_manager.active_menu.identifier == CLOSABLE_MENU_ID:
                        if not menu_manager.active_menu.is_position_inside(event.pos):
                            menu_manager.close_active_menu()
                    menu_manager.click(event.button, event.pos)
        display_main_screen()
        menu_manager.display()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
