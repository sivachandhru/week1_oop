import pytest
from shapes import Circle, Rectangle, Square

def test_circle_area():
    assert round(Circle(2).area(), 2) == 12.57

@pytest.mark.parametrize(("w", "h", "expected"), [(1, 1, 1), (3, 5, 15)])
def test_rectangle_area(w: float, h: float, expected: float):
    assert Rectangle(w, h).area() == expected

def test_square_area():
    assert Square(4).area() == 16
