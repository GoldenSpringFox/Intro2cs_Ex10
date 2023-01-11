from typing import List, Tuple


class WallHandler:
    MOVEMENT_DICT = {'Up': (0, 1), 'Down': (0, -1), "Left": (1, 0), 'Right': (1, 0)}

    def __init__(self, length=3) -> None:
        self.__walls: List[Tuple[int, int, str]] = []
        self.__length = length

    def add_wall(self, wall: Tuple[int, int, str]):
        self.__walls.append(wall)

    def move_wall(self):
        for _ in range(self.num_of_walls):
            x, y, direction = self.__walls.pop(0)
            x, y = (x + self.MOVEMENT_DICT[direction][0], y + self.MOVEMENT_DICT[direction][1])
            self.__walls.append((x, y, direction))

    @property
    def num_of_walls(self):
        return len(self.__walls)

    def _get_wall_coordinates(self, x, y, direction) -> List[Tuple[int, int]]:
        return [(x + self.MOVEMENT_DICT[direction][1] * i, y + self.MOVEMENT_DICT[direction][0] * i)
                for i in range(-(self.__length//2), self.__length//2 + 1)]
            

    def get_walls_coordinates(self) -> List[Tuple[int, int]]:
        return [coordinate for wall in self.__walls for coordinate in self._get_wall_coordinates(*wall)]
