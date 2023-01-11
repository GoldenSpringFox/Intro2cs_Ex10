from wall_handler import WallHandler

def test__get_wall_coordinates():
    wall_handler = WallHandler()
    assert set(wall_handler.calculate_wall_coordinates(5, 5, 'Left')) == {(4, 5), (5, 5), (6, 5)}
    assert set(wall_handler.calculate_wall_coordinates(5, 5, 'Right')) == {(4, 5), (5, 5), (6, 5)}
    assert set(wall_handler.calculate_wall_coordinates(5, 5, 'Up')) == {(5, 4), (5, 5), (5, 6)}
    assert set(wall_handler.calculate_wall_coordinates(5, 5, 'Down')) == {(5, 4), (5, 5), (5, 6)}

    wall_handler = WallHandler(5)
    assert set(wall_handler.calculate_wall_coordinates(5, 5, 'Up')) == {(5, 3), (5, 4), (5, 5), (5, 6), (5, 7)}


def test_get_walls_coordinates():
    wall_handler = WallHandler()
    wall_handler.add_wall((3, 3, 'Right'))
    wall_handler.add_wall((5, 5, 'Up'))
    assert wall_handler.walls_coordinates == {(3, 3, 'Right'): [(2, 3), (3, 3), (4, 3)], (5, 5, 'Up'): [(5, 4), (5, 5), (5, 6)]}
