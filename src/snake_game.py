from typing import Optional, List, Tuple
from game_display import GameDisplay
from game_objects.apple_handler import AppleHandler
from game_objects.wall_handler import WallHandler
from game_objects.snake import Snake
from game_utils import size, get_random_apple_data, get_random_wall_data


class SnakeGame:
    def __init__(self, args) -> None:
        self.__rounds = args.rounds
        self.__max_apples = args.apples
        self.__max_walls = args.walls
        self.__debug = args.debug
        self.__board_width = size[0]
        self.__board_height = size[1]
        self.__snake = Snake((self.__board_width//2, self.__board_height//2))
        self.__apple_handler = AppleHandler()
        self.__wall_handler = WallHandler()
        self.__key_clicked = None
        self.__score = 0
        self.__is_snake_dead = False
    
    
    ######################
    #   Public Methods   #
    ######################

    def read_key(self, key_clicked: Optional[str]) -> None:
        self.__key_clicked = key_clicked

    def update_objects(self) -> None:
        self._create_objects()
        self._move_objects()
        self._handle_collisions()

    def draw_board(self, gd: GameDisplay) -> None:
        if not self.__debug:
            for cord in self.__snake.body_coordinates:
                gd.draw_cell(*cord, 'black')
        for apple in self.__apple_handler.apples_coordinates:
            gd.draw_cell(*apple, 'green')
        for wall in self.__wall_handler.walls_coordinates.values():
            for coordinate in wall:
                if self._is_cell_out_of_bounds(*coordinate):
                    continue
                gd.draw_cell(*wall, 'blue')

    def end_round(self) -> None:
        self.__rounds -= 1

    def is_over(self) -> bool:
        return self.__rounds == 0 or self.__is_snake_dead

    @property
    def score(self):
        return self.__score
    

    #######################
    #   Private Methods   #
    #######################

    def _is_cell_empty(self, x: int, y: int):
        return (x, y) not in (
                self.__snake.body_coordinates +
                self.__apple_handler.apples_coordinates +
                self.__wall_handler.walls_coordinates.values())

    def _are_cells_empty(self, cells: List[Tuple[int, int]]):
        return all(self._is_cell_empty(*cell) for cell in cells)
    
    def _is_cell_out_of_bounds(self, x, y):
        return not (0 <= x < self.__board_width and 0 <= y < self.__board_height)
    

    def _create_objects(self):
        if self.__wall_handler.num_of_walls < self.__max_walls:
            new_wall = get_random_wall_data()
            new_wall_coordinates = self.__wall_handler.calculate_wall_coordinates(*new_wall)
            if self._are_cells_empty(new_wall_coordinates):
                self.__wall_handler.add_wall(new_wall)
        
        if self.__apple_handler.apple_count < self.__max_apples:
            new_apple = get_random_apple_data()
            if self._is_cell_empty(*new_apple):
                self.__apple_handler.add_apple(new_apple)


    def _move_objects(self):
        if self.__rounds%2 == 0:
            self.__wall_handler.move_wall()

        if not self.__debug:
            self.__snake.move(self.__key_clicked)


    def _handle_collisions(self):
        self._handle_snake_collisions()
        self._handle_wall_collisions()

    def _handle_snake_collisions(self):
        if self._is_snake_out_of_bounds() or self.__snake.is_head_on_body():
            self.__snake.remove_snake_head()
            self.__is_snake_dead = True
        elif self.__snake.head_coordinate in self.__apple_handler.apples_coordinates:
            self.__apple_handler.remove_apple(self.__snake.head_coordinate)
            self.__score += int(self.__snake.body_length ** 0.5)
            self.__snake.grow(3)

    def _is_snake_out_of_bounds(self):
        return self._is_cell_out_of_bounds(*self.__snake.head_coordinate)

    def _handle_wall_collisions(self):
        for wall, wall_coordinates in self.__wall_handler.walls_coordinates.items():
            if self._is_wall_out_of_bounds(wall_coordinates):
                self.__wall_handler.remove_wall(wall)

    def _is_wall_out_of_bounds(self, wall_coordinates: List[Tuple[int, int]]):
        return not any(self._is_cell_out_of_bounds(*coordinate) for coordinate in wall_coordinates)


