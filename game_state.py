from enum import Enum


class GameState(Enum):
    GAME_PAUSE = 0
    GAME_RUNNING = 1
    GAME_MENU = 2