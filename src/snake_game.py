import game_utils
from typing import Optional
from game_display import GameDisplay

class SnakeGame:

    def __init__(self) -> None:
        self.__x = 5
        self.__y = 5
        self.__key_clicked = None

    def read_key(self, key_clicked: Optional[str])-> None:
        self.__key_clicked = key_clicked

    def update_objects(self)-> None:
        if (self.__key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
        elif (self.__key_clicked == 'Right') and (self.__x < game_utils.size.width - 1):
            self.__x += 1
        elif (self.__key_clicked == 'Down') and (self.__y > 0):
            self.__y -= 1
        elif (self.__key_clicked == 'Up') and (self.__y < game_utils.size.height - 1):
            self.__y += 1

    def draw_board(self, gd: GameDisplay) -> None:
        gd.draw_cell(self.__x, self.__y, "blue")

    def end_round(self) -> None:
        pass

    def is_over(self) -> bool:
        return False