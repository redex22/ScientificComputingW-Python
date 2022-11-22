# This entrypoint file to be used in development. Start by reading README.md
from Rectangle import Rectangle
from Square import Square
from unittest import main


rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)


if __name__ == "__main__":
    # Run unit tests automatically
    main(module='test_module', exit=False)