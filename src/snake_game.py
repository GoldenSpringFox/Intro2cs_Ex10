from typing import Optional, List, Tuple
from game_display import GameDisplay
from game_objects.apple_handler import AppleHandler
from game_objects.wall_handler import WallHandler
from game_objects.snake import Snake
from game_utils import size, get_random_apple_data


class SnakeGame:

    def __init__(self, rounds: int, max_apples) -> None:
        self.__snake = Snake((size[0] // 2, size[1] // 2))
        self.__apple_handler = AppleHandler()
        self.__wall_handler = WallHandler()
        self.__key_clicked = None
        self.__score = 0
        self.__max_apples = max_apples
        self.rounds = rounds


    def is_cell_empty(self, x: int, y: int):
        return (x, y) not in (
                self.__snake.body_coordinates +
                self.__apple_handler.get_apples_coordinates() +
                self.__wall_handler.get_walls_coordinates())

    def are_cells_empty(self, cells: List[Tuple[int, int]]):
        return all(self.is_cell_empty(*cell) for cell in cells)

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        new_apple = get_random_apple_data()
        if self.is_cell_empty(new_apple[0], new_apple[1]) and len(self.__apple_handler.get_apples_coordinates()) < self.__max_apples:
            self.__apple_handler.generate_new_apple(new_apple)

        self.__snake.move(self.__key_clicked)

    def draw_board(self, gd: GameDisplay) -> None:
        for cord in self.__snake.body_coordinates:
            gd.draw_cell(*cord, 'black')
        # gd.draw_cell(*self.__snake.get_snake_coordinates()[0], "black")
        for apple in self.__apple_handler.get_apples_coordinates():
            gd.draw_cell(*apple, 'green')

    def end_round(self) -> None:
        self.rounds -= 1

    def is_over(self) -> bool:
        return self.rounds == 0

    @property
    def score(self):
        return self.__score
