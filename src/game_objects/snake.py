from typing import Tuple
from functools import reduce

class Snake:
    MOVEMENT_DICT = {'Up': (0, 1), 'Down': (0, -1), 'Left': (-1, 0), 'Right': (1,0)}

    def __init__(self, position: Tuple[int, int]):
        self.__direction = 'Up'
        self.__body = []
        self.__body.append(position)
        self.__body.append(Snake._position_after_movement(position, 'Down'))
        self.__body.append(Snake._position_after_movement(position, 'Down', 'Down'))

    def _position_after_movement(start: Tuple[int, int], *directions: str):
        return reduce(lambda pos,move_key: tuple(map(lambda x,y: x+y, pos, Snake.MOVEMENT_DICT[move_key])),directions, start)

    @property
    def body_coordinates(self):
        return self.__body

    @property
    def snake_head(self):
        return self.__body[0]

    def _same_axis_as_current_direction(self, move_key: str):
        if move_key not in self.MOVEMENT_DICT:
            raise ValueError(f"Invalid move: {move_key}")

        return all(map(lambda axis1, axis2: (axis1 == 0) == (axis2 == 0), self.MOVEMENT_DICT[self.__direction], self.MOVEMENT_DICT[move_key]))
    
    def _turn(self, move_key):
        if move_key is None or self._same_axis_as_current_direction(move_key):
            return False

        self.__direction = move_key
        return True

    def move(self, move_key):
        if move_key in self.MOVEMENT_DICT:
            self._turn(move_key)
        
        new_cord = Snake._position_after_movement(self.snake_head, self.__direction)
        # new_cord = tuple(map(lambda x,y: x+y, self.snake_head, self.MOVEMENT_DICT[self.__direction]))
        self.__body.insert(0, new_cord)
        self.__body.pop()


    def all_valid_coordinates(self):
        lst = []
        for row in range(self.__height):
            for col in range(self.__width):
                lst.append((row, col))
        return lst

    def is_there_a_collision(self):
        for cord in self.body_coordinates:
            if self.body_coordinates.count(cord) > 1:
                return True
        return False
