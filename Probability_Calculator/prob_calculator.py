from copy import deepcopy
from Hat import Hat


def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    """
    hat: A hat object containing balls that should be copied inside the function.
    expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
                    For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat,
                    set expected_balls to {"blue":2, "red":1}.
    num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    num_experiments: The number of experiments to perform. (The more experiments performed,
                     the more accurate the approximate probability will be.)
    :return: The experiment function should return a probability.
    """
    m = 0
    for _ in range(num_experiments):
        hat_copy = deepcopy(hat)
        hat_balls_drawn = hat_copy.draw(num_balls_drawn)
        matched_balls = sum([1 for k, v in expected_balls.items() if hat_balls_drawn.count(k) >= v])
        m += 1 if matched_balls == len(expected_balls) else 0
    return m / num_experiments


if __name__ == "__main__":
    # This is for testing purposes
    hat = Hat(blue=3, red=2, green=6)
    hat2 = Hat(red=5,blue=2)
    print(hat2.draw(2))
    probability = experiment(hat=hat, expected_balls={"blue": 2, "green": 1}, num_balls_drawn=4,
                                             num_experiments=1000)
    print(probability, probability == 0.272)
