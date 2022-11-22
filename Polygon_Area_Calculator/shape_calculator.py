class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, new_width: float) -> None:
        self.width = new_width

    def height(self):
        return self.height

    def set_height(self, new_height: float) -> None:
        self.height = new_height

    def get_area(self) -> float:
        """Returns area (width * height)"""
        return self.width * self.height

    def get_perimeter(self) -> float:
        """Returns perimeter (2 * width + 2 * height)"""
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self) -> float:
        """Returns diagonal ((width ** 2 + height ** 2) ** .5)"""
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self) -> str:
        """
        Returns a string that represents the shape using lines of "*".
        The number of lines should be equal to the height and the number of "*"
        in each line should be equal to the width.
        There should be a new line (\n) at the end of each line.
        If the width or height is larger than 50, this should return the string: "Too big for picture."."""
        pass

    def get_amount_inside(self, shape: object) -> float:
        """Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""
        pass

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side_length: float):
        super().__init__(side_length, side_length)

    @property
    def side(self) -> float:
        return self.width

    def set_side(self, new_length: float) -> None:
        super().set_height(new_length)
        super().set_width(new_length)

    def set_width(self, new_width: float) -> None:
        super().set_height(new_width)
        super().set_width(new_width)

    def set_height(self, new_height: float) -> None:
        super().set_height(new_height)
        super().set_width(new_height)

    def __repr__(self):
        return f"Square(side={self.side})"


if __name__ == "__main__":
    # This is for testing purposes
    t1 = Rectangle(10, 5)
    t2 = Square(5)
    print(f"Before: {t1}")
    print(f"{'Rectangle'.center(21, '-')}")
    print(f"Width: {t1.width}")
    print(f"Height: {t1.height}")
    print(f"Area: {t1.get_area()}")
    print(f"Perimeter: {t1.get_perimeter()}")
    print(f"Diagonal: {t1.get_diagonal()}", end="\n\n")
    print(f"Before: {t2}")
    print(f"{'Square'.center(21, '-')}")
    print(f"Width: {t2.width}")
    print(f"Height: {t2.height}")
    print(f"Side Length: {t2.side}")
    print(f"Area: {t2.get_area()}")
    print(f"Perimeter: {t2.get_perimeter()}")
    print(f"Diagonal: {t2.get_diagonal()}", end="\n\n")
    t1.set_width(20)
    t1.set_height(10)
    print(f"After: {t1}")
    print(f"{'Rectangle'.center(21, '-')}")
    print(f"Width: {t1.width}")
    print(f"Height: {t1.height}")
    print(f"Area: {t1.get_area()}")
    print(f"Perimeter: {t1.get_perimeter()}")
    print(f"Diagonal: {t1.get_diagonal()}", end="\n\n")
    t2.set_side(10)
    print(f"""After set side: {t2}
Width: {t2.width}
Height: {t2.height}
Side: {t2.side}""")
    t2.set_height(10)
    print(f"""After set height: {t2}
Width: {t2.width}
Height: {t2.height}
Side: {t2.side}""", end="\n\n")
    t2.set_width(10)
    print(f"""After set width: {t2}""")
    print(f"{'Square'.center(21, '-')}")
    print(f"Width: {t2.width}")
    print(f"Height: {t2.height}")
    print(f"Side Length: {t2.side}")
    print(f"Area: {t2.get_area()}")
    print(f"Perimeter: {t2.get_perimeter()}")
    print(f"Diagonal: {t2.get_diagonal()}")
