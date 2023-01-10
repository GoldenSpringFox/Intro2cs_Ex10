import game_utils
from typing import List, Tuple

class WallHandler:
    def __init__(self) -> None:
        self.__walls: List[Tuple[int, int]] = []

    def generate_new_wall(self):
        ...

    def get_walls_coordinates(self) -> List[Tuple[int, int]]:
        return self.__walls
