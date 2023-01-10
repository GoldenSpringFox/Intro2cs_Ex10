from src import game_utils
from typing import List, Tuple


class WallHandler:
    DIRECTION_DICT = {'Up': [(0, 1), (0, -1)], 'Down': [(0, 1), (0, -1)],'Right': [(1, 0), (-1, 0)], 'Left': [(1, 0), (-1, 0)]}
    MOVEMENT_DICT = {'Up': (0, 1), 'Down': (0, -1), "Left": (1, 0), 'Right': (1, 0)}

    def __init__(self) -> None:
        self.__walls: List[Tuple[int, int, str]] = []

    def generate_new_wall(self, wall):
        self.__walls.append(wall)

    def move_wall(self):
        for wall in self.__walls:
            wall_cord = (wall[0], wall[1])
            wall = self._adding_tuples(wall_cord, self.MOVEMENT_DICT[wall[2]])


    def _adding_tuples(self, wall_mid_cord: Tuple[int, int], cord: Tuple[int, int]):
        new_wall_cord = wall_mid_cord[0] + cord[0], wall_mid_cord[1] + cord[1]
        return new_wall_cord

    @property
    def num_of_walls(self):
        return len(self.__walls)

    def get_walls_coordinates(self) -> List[Tuple[int, int]]:
        lst = []
        for wall in self.__walls:
            wall_cord = (wall[0], wall[1])
            lst.append(wall_cord)
            for cord in self.DIRECTION_DICT[wall[2]]:
                lst.append(self._adding_tuples(wall_cord, cord))
        return lst
