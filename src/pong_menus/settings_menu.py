import PySimpleGUI as sg


def settings_menu() -> str:
    settings_layout = [
        [sg.Text("Pong Configuration File:")],
        [sg.FileBrowse(
                key="Browse Pong Configuration File",
                file_types=(("JSON Files", "*.json"),)
        ),
         sg.Input(key="PONG CONFIG PATH")],
        [sg.Button("Confirm", pad=((225, 3), (5, 3)))]
    ]

    settings_window = sg.Window("Settings", settings_layout)

    while True:
        event, values = settings_window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "Confirm":
            settings_window.close()
            return values["PONG CONFIG PATH"]

    settings_window.close()
    return ""
