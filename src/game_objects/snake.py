from typing import Tuple, List
from functools import reduce

class Snake:
    MOVEMENT_DICT = {'Up': (0, 1), 'Down': (0, -1), 'Left': (-1, 0), 'Right': (1,0)}

    def __init__(self, position: Tuple[int, int], width=3):
        self.__direction = 'Up'
        self.__grow = 0
        self._initialize_body(position, width)

    def _position_after_movement(start: Tuple[int, int], *directions: str):
        return reduce(lambda pos,move_key: tuple(map(lambda x,y: x+y, pos, Snake.MOVEMENT_DICT[move_key])),directions, start)

    def _initialize_body(self, position, width):
        self.__body = []
        self.__body.append(position)
        for _ in range(width-1):
            self.__body.append(Snake._position_after_movement(self.__body[-1], 'Down'))

    @property
    def body_coordinates(self) -> List[Tuple[int, int]]:
        return self.__body

    @property
    def head_coordinate(self) -> Tuple[int, int]:
        return self.__body[0]
    
    @property
    def body_length(self) -> int:
        return len(self.__body)
    
    def remove_snake_head(self):
        self.__body.pop(0)

    def _same_axis_as_current_direction(self, move_key: str) -> bool:
        if move_key not in self.MOVEMENT_DICT:
            raise ValueError(f"Invalid move: {move_key}")

        return all(map(lambda axis1, axis2: (axis1 == 0) == (axis2 == 0), self.MOVEMENT_DICT[self.__direction], self.MOVEMENT_DICT[move_key]))
    
    def _turn(self, move_key: str) -> bool:
        if move_key is None or self._same_axis_as_current_direction(move_key):
            return False

        self.__direction = move_key
        return True

    def move(self, move_key: str):
        if move_key in self.MOVEMENT_DICT:
            self._turn(move_key)
        
        new_cord = Snake._position_after_movement(self.head_coordinate, self.__direction)
        self.__body.insert(0, new_cord)
        if self.__grow > 0:
            self.__grow -= 1
        else:
            self.__body.pop()

    def is_head_on_body(self):
        return self.head_coordinate in self.__body[1:]
    
    def grow(self, amount):
        self.__grow += amount