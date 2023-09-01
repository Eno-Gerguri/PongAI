import PySimpleGUI as sg


def play_vs_ai_menu() -> tuple[str] | None:
    play_vs_ai_layout = [
        [
            sg.Radio("Play:",
                     key="PLAY BEST",
                     group_id="AI OPTIONS",
                     enable_events=True),
            sg.Text("best.pickle"),
        ],
        [
            sg.Radio("Play Custom:",
                     key="PLAY CUSTOM",
                     group_id="AI OPTIONS",
                     enable_events=True)
        ],
        [
            sg.FileBrowse(disabled=True, key="Browse Best AI"),
            sg.Input(key="AI Text Path", disabled=True)
        ],
        [sg.Button("Play", pad=((5, 3), (20, 3)), disabled=True)]
    ]

    play_vs_ai_window = sg.Window("Play VS AI", play_vs_ai_layout)

    while True:
        event, values = play_vs_ai_window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "PLAY BEST":
            play_vs_ai_window["Play"].update(disabled=False)
            play_vs_ai_window["Browse Best AI"].update(disabled=True)

        elif event == "PLAY CUSTOM":
            play_vs_ai_window["Play"].update(disabled=False)
            play_vs_ai_window["Browse Best AI"].update(disabled=False)

        elif event == "Play":
            play_vs_ai_window.close()

            if values["PLAY BEST"]:
                ai_path = "best.pickle"
            elif values["PLAY CUSTOM"]:
                ai_path = values["Browse Best AI"]

            return (ai_path,)

    play_vs_ai_window.close()
    return None
