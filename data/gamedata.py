from dataclasses import dataclass


@dataclass
class GameData:
    """
    GameData class holds data for a game.
    """
    screen_dim: int = 600
    game_title: str = 'Tic Tac Toe'
    board_dim: int = 3
    square_size : int = 200
    line_width : int = 15
    rows: int = 3
    columns: int = 3
    win_line_width: int = 15
    circle_radius: int = 60
    circle_width: int = 15
    cross_width: int = 25
    space: int = 55

    # rgb: red green blue
    background_color = (255,192,203)
    line_color = (255,105,180)
    circle_color = (199,21,133)
    cross_color = (66, 66, 66)