if __name__ == "__main__":
    # This is for testing purposes
    from Rectangle import Rectangle
    from Square import Square
    t1 = Rectangle(15, 10)
    t2 = Square(5)
    print(t1.get_amount_inside(t2))
    print(t2.get_amount_inside(t1))
    print(f"Before: {t1}")
    print(f"{'Rectangle'.center(21, '-')}")
    print(f"Width: {t1.width}")
    print(f"Height: {t1.height}")
    print(f"Area: {t1.get_area()}")
    print(f"Perimeter: {t1.get_perimeter()}")
    print(f"Diagonal: {t1.get_diagonal()}", end="\n\n")
    print(t1.get_picture())
    print(f"Before: {t2}")
    print(f"{'Square'.center(21, '-')}")
    print(f"Width: {t2.width}")
    print(f"Height: {t2.height}")
    print(f"Side Length: {t2.side}")
    print(f"Area: {t2.get_area()}")
    print(f"Perimeter: {t2.get_perimeter()}")
    print(f"Diagonal: {t2.get_diagonal()}", end="\n\n")
    print(t2.get_picture())
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
