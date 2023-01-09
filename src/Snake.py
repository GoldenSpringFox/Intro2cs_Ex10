class Snake:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width
        self.__size = 3
        self.__direction = 'Up'
        self.__snake_cords = [(width // 2, height // 2), (width // 2, (height // 2) - 1),
                              (width // 2, (height // 2) - 2)]

    def get_snake_coordinates(self):
        return self.__snake_cords

    def move(self, key_clicked):
        if key_clicked is None:
            key_clicked = self.__direction

        if self.__direction == 'Up' and key_clicked == 'Down':
            key_clicked = self.__direction
        elif self.__direction == 'Down' and key_clicked == 'Up':
            key_clicked = self.__direction
        elif self.__direction == 'Left' and key_clicked == 'Right':
            key_clicked = self.__direction
        elif self.__direction == 'Right' and key_clicked == 'Left':
            key_clicked = self.__direction

        if key_clicked == 'Up':
            new_cord = (self.__snake_cords[0][0], self.__snake_cords[0][1] + 1)
            self.__snake_cords.insert(0, new_cord)
        elif key_clicked == 'Down':
            new_cord = (self.__snake_cords[0][0], self.__snake_cords[0][1] - 1)
            self.__snake_cords.insert(0, new_cord)
        elif key_clicked == 'Left':
            new_cord = (self.__snake_cords[0][0] - 1, self.__snake_cords[0][1])
            self.__snake_cords.insert(0, new_cord)
        elif key_clicked == 'Right':
            new_cord = (self.__snake_cords[0][0] + 1, self.__snake_cords[0][1])
            self.__snake_cords.insert(0, new_cord)
        self.__snake_cords.pop()
        self.__direction = key_clicked

    def all_valid_coordinates(self):
        lst = []
        for row in range(self.__height):
            for col in range(self.__width):
                lst.append((row, col))
        return lst

    def is_snake_in_board(self):
        for cord in self.get_snake_coordinates():
            if cord not in self.all_valid_coordinates():
                return False
        return True

    def is_there_a_collision(self):
        for cord in self.get_snake_coordinates():
            if self.get_snake_coordinates().count(cord) > 1:
                return True
        return False
