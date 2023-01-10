from typing import List, Tuple


class AppleHandler:
    def __init__(self) -> None:
        self.__apples: List[Tuple[int, int]] = []

    def add_apple(self, location: Tuple[int, int]):
        self.__apples.append(location)

    @property
    def apples_coordinates(self) -> List[Tuple[int, int]]:
        return self.__apples

    @property
    def apple_count(self):
        return len(self.__apples)

    def remove_apple(self, apple: Tuple[int, int]):
        self.__apples.remove(apple)
