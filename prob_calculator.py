import random
import copy


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents.extend([color] * quantity)

    def draw(self, num_balls):
        drawn_balls = []
        for _ in range(min(num_balls, len(self.contents))):
            ball_index = random.randint(0, len(self.contents) - 1)
            drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = []
        for _ in range(num_balls_drawn):
            if len(hat_copy.contents) == 0:
                break
            ball_index = random.randint(0, len(hat_copy.contents) - 1)
            drawn_balls.append(hat_copy.contents.pop(ball_index))
        drawn_counts = {color: drawn_balls.count(color) for color in expected_balls}
        if all(
            drawn_counts.get(color, 0) >= count
            for color, count in expected_balls.items()
        ):
            successful_experiments += 1
    probability = successful_experiments / num_experiments
    return probability
