from snake import Snake
import pytest

def test__position_after_movement():
    assert Snake._position_after_movement((10, 10)) == (10, 10)
    assert Snake._position_after_movement((10, 10), 'Up') == (10, 11)
    assert Snake._position_after_movement((10, 10), 'Down') == (10, 9)
    assert Snake._position_after_movement((10, 10), 'Left') == (9, 10)
    assert Snake._position_after_movement((10, 10), 'Right') == (11, 10)
    assert Snake._position_after_movement((10, 10), 'Up', 'Up') == (10, 12)
    assert Snake._position_after_movement((10, 10), 'Up', 'Right', 'Down','Down','Left') == (10, 9)

def test__same_axis_as_current_direction():
    snake = Snake((10,10))
    assert snake._same_axis_as_current_direction('Up')
    assert snake._same_axis_as_current_direction('Down')
    assert not snake._same_axis_as_current_direction('Left')
    assert not snake._same_axis_as_current_direction('Right')
    with pytest.raises(ValueError) as excinfo:
        snake._same_axis_as_current_direction('Flurgle')
        assert "Invalid move" in str(excinfo.value)

def test__turn():
    snake = Snake((10, 10))
    assert not snake._turn(None)
    with pytest.raises(ValueError) as excinfo:
        assert not snake._turn('Flurgle')
        assert "Invalid move" in str(excinfo.value)
    assert not snake._turn('Up')
    assert not snake._turn('Down')
    
    assert snake._turn('Left')
    assert snake._turn('Up')
    assert snake._turn('Right')
    assert not snake._turn('Left')
    assert snake._turn('Down')

def test_move():
    snake = Snake((10, 10))
    snake.move(None)
    assert snake.body_coordinates == [(10, 11), (10, 10), (10, 9)]
    snake.move('Flurgle')
    assert snake.body_coordinates == [(10, 12), (10, 11), (10, 10)]
    snake.move('Down')
    assert snake.body_coordinates == [(10, 13), (10, 12), (10, 11)]
    snake.move('Up')
    assert snake.body_coordinates == [(10, 14), (10, 13), (10, 12)]
    snake.move('Left')
    assert snake.body_coordinates == [(9, 14), (10, 14), (10, 13)]
    snake.move('Right')
    assert snake.body_coordinates == [(8, 14), (9, 14), (10, 14)]
    snake.move('Down')
    assert snake.body_coordinates == [(8, 13), (8, 14), (9, 14)]
    snake.move('Right')
    assert snake.body_coordinates == [(9, 13), (8, 13), (8, 14)]

