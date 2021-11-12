import pygame
import numpy as np
from data.gamedata import GameData


class Builder:
    """
    Builder class for the game, deals with the building of the game screen and other components.
    """
    game_screen = None
    board = None
    player = None
    game_over = False


    def __init__(self):
        """
        Initializes the game screen, player(1), game_over and the board.
        """
        self.game_screen = pygame.display.set_mode((GameData.screen_dim, GameData.screen_dim))
        self.game_screen.fill(GameData.background_color)
        self.player = 1
        self.game_over = False
        self.board = np.zeros((GameData.rows, GameData.columns))


    def grid_init(self):
        """
        Draws the grid on the screen surface.
        """
        # draw.line(surface, color, start_pos, end_pos, width/thickness)
        pygame.draw.line(
            self.game_screen,
            GameData.line_color,
            (0, GameData.square_size),
            (GameData.screen_dim, GameData.square_size),
            GameData.line_width
        )
        # # 2 horizontal
        pygame.draw.line(
            self.game_screen,
            GameData.line_color,
            (0, 2 * GameData.square_size),
            (GameData.screen_dim,2 * GameData.square_size),
            GameData.line_width
        )

        # # 1 vertical
        pygame.draw.line(
            self.game_screen,
            GameData.line_color,
            (GameData.square_size, 0),
            (GameData.square_size, GameData.screen_dim),
            GameData.line_width
        )
        # # 2 vertical
        pygame.draw.line(
            self.game_screen,
            GameData.line_color,
            (2 * GameData.square_size, 0),
            (2 * GameData.square_size, GameData.screen_dim),
            GameData.line_width)

    def draw_player_symbols (self):
        """
        Draws the player symbols on the board i.e X & O.
        :return:
        """
        for row in range(GameData.rows):
                for col in range(GameData.columns):
                    if self.board[row][col] == 1:
                        pygame.draw.circle(
                            self.game_screen,
                            GameData.circle_color,
                            # Add the offset to center the circle
                            (int(col * GameData.square_size + GameData.square_size // 2),
                             int(row * GameData.square_size + GameData.square_size // 2)),
                            GameData.circle_radius,
                            GameData.circle_width
                        )
                    elif self.board[row][col] == 2:
                        pygame.draw.line(self.game_screen, GameData.cross_color,
                                         (col * GameData.square_size + GameData.space, row * GameData.square_size +
                                          GameData.square_size
                                          - GameData.space),
                                         (col * GameData.square_size + GameData.square_size - GameData.space,
                                          row * GameData.square_size +
                                          GameData.space),
                                         GameData.cross_width)

                        pygame.draw.line(
                            self.game_screen, GameData.cross_color,
                            (col * GameData.square_size + GameData.space, row * GameData.square_size + GameData.space),
                            (col * GameData.square_size + GameData.square_size - GameData.space,
                             row * GameData.square_size + GameData.square_size - GameData.space),
                             GameData.cross_width)

    def draw_player_symbol(self, row, col, player):
        """
        Marks a square on the board with current player (1 or)2.
        """
        self.board[row][col] = player

    def check_tile_availability(self, row, col):
        """
        Checks if the tile/slot is available or not.
        """
        return self.board[row][col] == 0

    def board_tiles_availability(self):
        """
        Checks if the board is fully occupied.
        """
        for row in range(GameData.rows):
            for col in range(GameData.columns):
                if self.board[row][col] == 0:
                    return False
        # Game is draw, no more moves left!
        return True

    def winning_event(self, player):
        """
        Checks if the player has won the game, and draws the winning line.
        :param player: which player has won the game.
        :return: Winning status
        """
        # vertical check
        for col in range(GameData.columns):
            if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
                self.draw_vertical_winning_line(col, player)
                print("Player {} has won the game!".format(player))
                self.game_over = True
                return True

        # horizontal  check
        for row in range(GameData.rows):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                self.draw_horizontal_winning_line(row, player)
                print("Player {} has won the game!".format(player))
                self.game_over = True
                return True

        # ascending diagonal heck
        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            self.draw_asc_diagonal(player)
            print("Player {} has won the game!".format(player))
            self.game_over = True
            return True

        # descending diagonal win chek
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            self.draw_desc_diagonal(player)
            print("Player {} has won the game!".format(player))
            self.game_over = True
            return True

        return False

    def draw_vertical_winning_line(self, col, player):
        """
        Draws the winning line for the vertical winning event.
        """
        # getting the x value from the current column
        posX = col * GameData.square_size + GameData.square_size // 2

        if player == 1:
            color = GameData.circle_color
        elif player == 2:
            color = GameData.cross_color

        pygame.draw.line(
            self.game_screen,
            color, (posX, 15),
            (posX, GameData.screen_dim - 15),
            GameData.line_width)

    def draw_horizontal_winning_line(self, row, player):
        """
        Draws the winning line for the horizontal winning event.
        """
        posY = row * GameData.square_size + GameData.square_size // 2

        if player == 1:
            color = GameData.circle_color
        elif player == 2:
            color = GameData.cross_color

        pygame.draw.line(
            self.game_screen,
            color, (15, posY),
            (GameData.screen_dim - 15, posY),
            GameData.win_line_width
        )


    def draw_asc_diagonal(self, player):
        """
        Draws the winning line for the ascending diagonal winning event.
        """
        if player == 1:
            color = GameData.circle_color
        elif player == 2:
            color = GameData.cross_color

        pygame.draw.line(
            self.game_screen,
            color,
            (15, GameData.screen_dim - 15),
            (GameData.screen_dim - 15, 15), GameData.win_line_width)

    def draw_desc_diagonal(self, player):
        """
        Draws the winning line for the descending diagonal winning event.
        """
        if player == 1:
            color = GameData.circle_color
        elif player == 2:
            color = GameData.cross_color

        pygame.draw.line(self.game_screen, color, (15, 15), (GameData.screen_dim - 15, GameData.screen_dim - 15),
                         GameData.win_line_width)

    def game_restart (self):
        """
        Restarts the game.
        """
        self.game_over = False
        self.player = 1
        self.game_screen.fill(GameData.background_color)
        self.grid_init()
        self.board = np.zeros((GameData.rows, GameData.columns))