from random import randrange


class Hat:
    """
    The class should take a variable number of arguments that specify the number of balls
    of each color that are in the hat.
    """
    def __init__(self, **balls):
        self.contents = [ht for ht, v in balls.items() for _ in range(v)]

    def draw(self, num_to_retrieve: int) -> list:
        """
        Accepts an argument indicating the number of balls to draw from the hat.
        This method should remove balls at random from contents and return those balls as a list of strings.
        The balls should not go back into the hat during the draw, similar to an urn experiment without replacement.
        If the number of balls to draw exceeds the available quantity, return all the balls.
        """
        if len(self.contents) < num_to_retrieve:
            return self.contents
        return [self.contents.pop(randrange(len(self.contents))) for _ in range(num_to_retrieve)]

