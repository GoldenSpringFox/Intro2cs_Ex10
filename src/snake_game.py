from typing import Optional, List, Tuple
from game_display import GameDisplay
from game_objects.apple_handler import AppleHandler
from game_objects.wall_handler import WallHandler
from game_objects.snake import Snake
from game_utils import size, get_random_apple_data


class SnakeGame:

    def __init__(self, args) -> None:
        self.__rounds = args.rounds
        self.__max_apples = args.apples
        self.__debug = args.debug
        self.__board_width = size[0]
        self.__board_height = size[1]
        self.__snake = Snake((self.__board_width//2, self.__board_height//2))
        self.__apple_handler = AppleHandler()
        self.__wall_handler = WallHandler()
        self.__key_clicked = None
        self.__score = 0
        self.__is_snake_dead = False

    def _is_cell_empty(self, x: int, y: int):
        return (x, y) not in (
                self.__snake.body_coordinates +
                self.__apple_handler.get_apples_coordinates() +
                self.__wall_handler.get_walls_coordinates())

    def _are_cells_empty(self, cells: List[Tuple[int, int]]):
        return all(self._is_cell_empty(*cell) for cell in cells)

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def _snake_collided_with_wall(self):
        return not (0 <= self.__snake.head_coordinate[0] < self.__board_width and
            0 <= self.__snake.head_coordinate[1] < self.__board_height)

    def _check_snake_collision(self):
        if self._snake_collided_with_wall() or self.__snake.is_head_on_body():
            self.__snake.remove_snake_head()
            self.__is_snake_dead = True
        elif self.__snake.head_coordinate in self.__apple_handler.get_apples_coordinates():
            self.__score += int(self.__snake.body_length ** 0.5)
            self.__snake.grow(3)

    def update_objects(self) -> None:
        new_apple = get_random_apple_data()
        if self._is_cell_empty(new_apple[0], new_apple[1]) and len(self.__apple_handler.get_apples_coordinates()) < self.__max_apples:
            self.__apple_handler.generate_new_apple(new_apple)

        if not self.__debug:
            self.__snake.move(self.__key_clicked)
        self._check_snake_collision()

    def draw_board(self, gd: GameDisplay) -> None:
        if not self.__debug:
            for cord in self.__snake.body_coordinates:
                gd.draw_cell(*cord, 'black')
        for apple in self.__apple_handler.get_apples_coordinates():
            gd.draw_cell(*apple, 'green')

    def end_round(self) -> None:
        self.__rounds -= 1

    def is_over(self) -> bool:
        return self.__rounds == 0 or self.__is_snake_dead

    @property
    def score(self):
        return self.__score
