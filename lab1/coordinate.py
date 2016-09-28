import math


class Coordinate:
    @staticmethod
    def get_center(dataset):
        dots = dataset.get_dots()
        n = len(dots)
        x = sum([i[0] for i in dots]) / n
        y = sum([i[1] for i in dots]) / n
        return [x, y]

    @staticmethod
    def translate(dataset, new_center):
        for i in dataset:
            i[0][0] -= new_center[0]
            i[0][1] -= new_center[0]
        return dataset

    @staticmethod
    def to_polar(dataset):
        for i in dataset:
            x, y = i[0][0], i[0][1]
            p = math.sqrt(x**2 + y**2)
            f = 0
            if x != 0:
                f = math.atan(y / x)
            else:
                f = math.pi / 2 if y >= 0 else - math.pi / 2
            if x < 0:
                f += math.pi
            i[0][0] = p
            i[0][1] = f
        return dataset

    @staticmethod
    def from_polar(dataset):
        for i in dataset:
            x = i[0][0] * math.cos(i[0][1])
            y = i[0][0] * math.sin(i[0][1])
            i[0][0] = x
            i[0][1] = y
        return dataset

    @staticmethod
    def normalize_polar(dataset):
        c = max([i[0][0] for i in dataset])
        for i in dataset:
            i[0][0] /= c
        return c
