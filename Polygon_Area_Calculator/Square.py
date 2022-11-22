from Rectangle import Rectangle


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

