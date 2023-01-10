from typing import List, Tuple


class AppleHandler:
    def __init__(self) -> None:
        self.__apples: List[Tuple[int, int]] = []

    def generate_new_apple(self, cord):
        self.__apples.append(cord)

    def get_apples_coordinates(self) -> List[Tuple[int, int]]:
        return self.__apples

    def remove_apple(self, apple):
        self.__apples.remove(apple)
