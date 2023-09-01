from dataclasses import dataclass


@dataclass
class GameInformation:
    left_hits: int
    right_hits: int
    left_score: int
    right_score: int
