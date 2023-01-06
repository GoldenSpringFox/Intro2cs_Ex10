from typing import Optional, List, Tuple
from game_display import GameDisplay
from game_objects.snake import Snake
from game_objects.apple_handler import AppleHandler
from game_objects.wall_handler import WallHandler

class SnakeGame:

    def __init__(self, rounds: int) -> None:
        self.__snake = Snake()
        self.__apple_handler = AppleHandler()
        self.__wall_handler = WallHandler()
        self.__key_clicked = None
        self.__score = 0
        self.rounds = rounds

    def is_cell_empty(self, x: int, y: int):
        return (x,y) not in (
            self.__snake.get_snake_coordinates() + 
            self.__apple_handler.get_apples_coordinates() +
            self.__wall_handler.get_walls_coordinates())
    
    def are_cells_empty(self, cells: List[Tuple[int, int]]):
        return all(self.is_cell_empty(*cell) for cell in cells)

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        self.__snake.move(self.__key_clicked)

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(*self.__snake.get_snake_coordinates()[0], "blue")

    def end_round(self) -> None:
        self.rounds -= 1

    def is_over(self) -> bool:
        return self.rounds == 0
    
    @property
    def score(self):
        return self.__score