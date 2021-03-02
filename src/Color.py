import numpy as np

GUASSIAN_COEFFICIENT = 1 / 159
GUASSIAN_MATRIX = np.array([[2, 4, 5, 4, 2],
                            [4, 9, 12, 9, 4],
                            [5, 12, 15, 12, 5],
                            [4, 9, 12, 9, 4],
                            [2, 4, 5, 4, 2]])

class RGB265:
    def __init__(self, raw):
        if isinstance(raw, np.ndarray):
            self.raw = raw

    def red_green_blue_split(self):
        if isinstance(self.raw, np.ndarray):
            r, g, b = self.raw[...,0], self.raw[...,1], self.raw[...,2]
            return r, g, b

    def color_mean(self):
        return (lambda x: x - np.mean(x, axis=0))(self.raw)

    def color_stdv(self):
        return (lambda x: x / np.std(x, axis=0))(self.raw)

    def obtain_value(self, i=None, j=None):
        try:
            return self.raw[i][j]
        except IndexError:
            return 0
