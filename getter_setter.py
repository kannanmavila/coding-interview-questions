import math

class Square(object):
    """A square with two properties: a writable area and a read-only perimeter.

    To use:
    >>> sq = Square(3)
    >>> sq.area
    9
    >>> sq.perimeter
    12
    >>> sq.area = 16
    >>> sq.side
    4
    >>> sq.perimeter
    16
    """

    def __init__(self, side):
        self.side = side

    def _get_area(self):
        """Calculates the 'area' property."""
        return self.side ** 2

    def _set_area(self, area):
        """Sets the 'area' property."""
        self.side = math.sqrt(area)

    area = property(_get_area, _set_area,
                    doc="""Gets or sets the area of the square.""")

    @property
    def perimeter(self):
        return self.side * 4

#################### DRIVERS ####################

sq = Square(3)
print sq.area
print sq.perimeter
sq.area = 16
print sq.side
print sq.perimeter
