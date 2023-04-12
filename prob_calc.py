
import copy
import random

class Hat:

    def __init__(self, **kwargs) -> None:
        # for the __repr__ method
        self.kwargs: dict[str, int] = kwargs
        self.contents: list[str] = []

        # loop through the keyword arguments
        for color in kwargs.keys():
            # the index is not needed so `_` is sufficient
            # epeat the loop as often as the value in the keyword argument
            # and append the key as much
            for _ in range(kwargs[color]):
                self.contents.append(color)

    def draw(self, num_of_balls: int) -> list[str]:
       
        # safety or the pop() method
        # so that pop can't pop from an empty list
        # and raise an `IndexError`
        if num_of_balls >= len(self.contents):
            return self.contents

        balls: list[str] = []

        # repeat the loop for every ball wanted
        for _ in range(num_of_balls):
            # choose a random ball out of the list
            # to get a int value `random.randint` is the perfect function
            # ref:
            # https://github.com/timgrossmann/InstaPy/issues/2208#issuecomment-396048533
            choice: int = random.randint(0, abs(len(self.contents) - 1))

            # `pop()` removes the item from the list so it can not be drawn again
            balls.append(self.contents.pop(choice))

        return balls

    def __repr__(self) -> str:
       
        return __class__.__qualname__ + f"({self.kwargs})"


# ref:
# https://medium.com/i-math/can-you-solve-this-intro-probability-problem-807c59543c32
# https://en.wikipedia.org/wiki/Urn_problem
def experiment(
    hat: Hat,
    expected_balls: dict[str, int],
    num_balls_drawn: int,
    num_experiments: int,
) -> float:

    # variable to count successful draws
    num_successes: int = 0

    for _ in range(num_experiments):
        # grab a new, fresh copy of the hat everytime the loop is run through
        # https://docs.python.org/3/library/copy.html
        # using the `copy` method is not suffcient
        # so we use the `deepcopy` method instead
        hat_copy: Hat = copy.deepcopy(hat)

        # draw balls
        balls: list[str] = hat_copy.draw(num_balls_drawn)

        # variable to indicate a successful draw
        successful_draws: bool = True

        for color in expected_balls.keys():
            # ref:
            # https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count
            if balls.count(color) < expected_balls[color]:
                successful_draws = False
                continue

        if successful_draws:
            num_successes += 1

    return float(num_successes / num_experiments)
