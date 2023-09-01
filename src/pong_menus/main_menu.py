import PySimpleGUI as sg

from .train_ai_menu import train_ai_menu
from .play_vs_ai_menu import play_vs_ai_menu
from .settings_menu import settings_menu


def main_menu() -> tuple[str, tuple | None, str]:
    """
    Gets the decision from the user.
    :return: The user's decision, its arguments and the pong configuration path
    """
    main_layout = [
        [sg.Button("Train AI")],
        [sg.Button("Play VS AI")],
        [sg.Button("Player 1 VS Player 2")],
        [sg.Button("Settings")]
    ]

    main_window = sg.Window("Home", main_layout)

    pong_configuration_path = ""

    while True:
        event, values = main_window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "Train AI":
            if decision := train_ai_menu():
                main_window.close()
                return event, decision, pong_configuration_path

        elif event == "Play VS AI":
            if decision := play_vs_ai_menu():
                main_window.close()
                return event, decision, pong_configuration_path

        elif event == "Player 1 VS Player 2":
            main_window.close()
            return event, None, pong_configuration_path

        elif event == "Settings":
            if new_pong_configuration_path := settings_menu():
                pong_configuration_path = new_pong_configuration_path

    main_window.close()
    return "CLOSED", None, pong_configuration_path
