import pygame

from pong_menus.main_menu import main_menu
from pong.pong_config import PongConfig
from pong_neat.pong_functions import (
    run_neat,
    play_ai,
    player_vs_player
)


NEAT_CONFIG_PATH = "config.txt"

if __name__ == "__main__":
    while True:
        pygame.init()
        user_decision = main_menu()
        pong_config = PongConfig.get_pong_configurations(user_decision[2]) \
            if user_decision[2] else PongConfig.get_pong_configurations(
                PongConfig.DEFAULT_PONG_CONFIG_FILE_PATH
        )

        match user_decision[0]:
            case "Train AI":
                run_neat(*user_decision[1], pong_config, NEAT_CONFIG_PATH)

            case "Play VS AI":
                play_ai(user_decision[1][0], pong_config, NEAT_CONFIG_PATH)

            case "Player 1 VS Player 2":
                player_vs_player(pong_config)

            case "CLOSED":
                break
