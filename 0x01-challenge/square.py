#!/usr/bin/env python3
"""Class Square that defines a square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize a new Square instance with a specified size.

        Args:
            size (int): The length of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def perimeter(self):
        """Calculate and return the perimeter of the square."""
        return self.__size * 4

    def __str__(self):
        """Return a string representation of the square."""
        return f"{self.__size}/{self.__size}"

if __name__ == "__main__":
    s = Square(12)
    print(s)
    print(s.area())
    print(s.perimeter())
