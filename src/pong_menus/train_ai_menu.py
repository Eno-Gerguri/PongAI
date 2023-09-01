import PySimpleGUI as sg


def train_ai_menu() -> tuple[str, bool, bool, int] | None:
    train_ai_layout = [
        [sg.Checkbox("Draw Scores", key="DRAW SCORES")],
        [sg.Checkbox("Draw Hits", key="DRAW HITS")],
        [
            sg.Text("No. of Generations:"),
            sg.Input("20", key="NUMBER OF GENERATIONS")
        ],
        [sg.Checkbox(
                "Train From CheckPoint:",
                enable_events=True,
                key="TRAIN FROM CHECKPOINT"
        )],
        [
            sg.FileBrowse(disabled=True, key="Browse Checkpoint"),
            sg.Text(key="File Path Text")
        ],
        [sg.Button("Train", pad=((5, 3), (20, 3)))]
    ]

    train_ai_window = sg.Window("Train AI", train_ai_layout)

    while True:
        event, values = train_ai_window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == "TRAIN FROM CHECKPOINT":
            if values["TRAIN FROM CHECKPOINT"]:
                train_ai_window["Browse Checkpoint"].update(disabled=False)
            else:
                train_ai_window["Browse Checkpoint"].update(disabled=True)

        elif event == "Train":
            train_ai_window.close()

            try:
                number_of_generations = int(values["NUMBER OF GENERATIONS"])
            except (ValueError, TypeError) as error:
                continue
            draw_scores = values["DRAW SCORES"]
            draw_hits = values["DRAW HITS"]
            checkpoint_path = values["Browse Checkpoint"] \
                if values["TRAIN FROM CHECKPOINT"] else None

            return (
                checkpoint_path,
                draw_scores,
                draw_hits,
                number_of_generations
            )

    train_ai_window.close()
    return None
