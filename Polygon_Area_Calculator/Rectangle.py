class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, new_width: float) -> None:
        self.width = new_width

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
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for y_side in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self, shape: object) -> float:
        """Takes another shape (square or rectangle) as an argument.
        Returns the number of times the passed in shape could fit inside the shape (with no rotations).
        For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""
        return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
