import game_utils
from typing import List, Tuple

class Snake:
    def __init__(self):
        self.__x = 5
        self.__y = 5
    
    def move(self, key_clicked):
        if (key_clicked == 'Left') and (self.__x > 0):
            self.__x -= 1
        elif (key_clicked == 'Right') and (self.__x < game_utils.size.width - 1):
            self.__x += 1
        elif (key_clicked == 'Down') and (self.__y > 0):
            self.__y -= 1
        elif (key_clicked == 'Up') and (self.__y < game_utils.size.height - 1):
            self.__y += 1
    
    def get_snake_coordinates(self) -> List[Tuple[int, int]]:
        return [(self.__x, self.__y)]
