import pygame
import json
from dataclasses import dataclass

pygame.font.init()


@dataclass
class PongConfig:
    DEFAULT_PONG_CONFIG_FILE_PATH: str = "pong/pong_config.json"
    WINDOW_WIDTH: int = 700
    WINDOW_HEIGHT: int = 500
    FPS: int = 60
    PRIMARY_COLOR: tuple = (255, 255, 255)
    BACKGROUND_COLOR: tuple = (0, 0, 0)
    SECONDARY_COLOR: tuple = (255, 0, 0)
    PADDLE_WIDTH: int = 20
    PADDLE_HEIGHT: int = 100
    PADDLE_VELOCITY: int = 4
    BALL_MAXIMUM_VELOCITY: int = 5
    BALL_RADIUS: int = 7
    _SCORE_FONT: tuple = ("comicsans", 50)
    SCORE_FONT: pygame.font.Font = pygame.font.SysFont(*_SCORE_FONT)
    _HITS_FONT: tuple = ("comicsans", 50)
    HITS_FONT: pygame.font.Font = pygame.font.SysFont(*_HITS_FONT)
    WINNING_SCORE: int = 3

    def store_default_settings():
        with open(PongConfig.DEFAULT_PONG_CONFIG_FILE_PATH, "w") as f:
            to_dump = vars(PongConfig())
            to_dump = {
                k: v
                for k, v in to_dump.items()
                if not isinstance(v, pygame.font.Font)
            }
            json.dump(to_dump, f, indent=2)

    def get_pong_configurations(file_path: str):
        with open(file_path, "r") as f:
            pong_config = json.load(f)
            for key, value in list(pong_config.items()):
                if "FONT" in key:
                    pong_config[key[1:]] = pygame.font.SysFont(*value)
            pong_config = PongConfig(**pong_config)
            return pong_config
