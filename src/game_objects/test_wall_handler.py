from wall_handler import WallHandler

def test__get_wall_coordinates():
    wall_handler = WallHandler()
    assert set(wall_handler._get_wall_coordinates(5, 5, 'Up')) == {(4, 5), (5, 5), (6, 5)}
    assert set(wall_handler._get_wall_coordinates(5, 5, 'Down')) == {(4, 5), (5, 5), (6, 5)}
    assert set(wall_handler._get_wall_coordinates(5, 5, 'Left')) == {(5, 4), (5, 5), (5, 6)}
    assert set(wall_handler._get_wall_coordinates(5, 5, 'Right')) == {(5, 4), (5, 5), (5, 6)}

    wall_handler = WallHandler(5)
    assert set(wall_handler._get_wall_coordinates(5, 5, 'Right')) == {(5, 3), (5, 4), (5, 5), (5, 6), (5, 7)}


def test_get_walls_coordinates():
    wall_handler = WallHandler()
    wall_handler.add_wall((3, 3, 'Up'))
    wall_handler.add_wall((5, 5, 'Right'))
    assert set(wall_handler.get_walls_coordinates()) == {(2, 3), (3, 3), (4, 3), (5, 4), (5, 5), (5, 6)}

    wall_handler = WallHandler()
    wall_handler.add_wall((3, 3, 'Up'))
    wall_handler.add_wall((3, 2, 'Right'))
    assert set(wall_handler.get_walls_coordinates()) == {(2, 3), (3, 3), (4, 3), (3, 1), (3, 2)}