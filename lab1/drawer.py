import pylab as pl
import math
from matplotlib.colors import ListedColormap

pl.figure(figsize=(8, 8))


class Drawer:
    @staticmethod
    def change_plot():
        pl.figure(figsize=(8, 8))

    @staticmethod
    def draw_dataset(dataset, colors=None):
        data = dataset.data
        if colors is not None:
            colors = ListedColormap(colors)
        pl.scatter([x[0][0] for x in data],
                   [x[0][1] for x in data],
                   c=[x[1] for x in data],
                   cmap=colors)

    @staticmethod
    def draw_dataset_polar(dataset, colors=None):
        data = dataset.data
        if colors is not None:
            colors = ListedColormap(colors)
        pl.scatter([x[0][0] * math.cos(x[0][1]) for x in data],
                   [x[0][0] * math.sin(x[0][1]) for x in data],
                   c=[x[1] for x in data],
                   cmap=colors)

    @staticmethod
    def draw_dot(dot, color=None):
        if color is not None:
            color = ListedColormap([color])
        pl.scatter([dot[0]], [dot[1]], c=[0], cmap=color)

    @staticmethod
    def draw_polar_grid():
        lim = 1.5
        pl.gca().add_patch(pl.Circle((0, 0), 1, color='black', fill=None))
        pl.gca().add_patch(pl.Circle((0, 0), 0.5, color='black', fill=None))
        pl.plot([-lim, lim], [-lim, lim], color='black')
        pl.plot([-lim, lim], [lim, -lim], color='black')
        pl.plot([0, 0], [-lim, lim], color='black')
        pl.plot([-lim, lim], [0, 0], color='black')

    @staticmethod
    def limits(lim):
        pl.xlim(lim[0])
        pl.ylim(lim[1])

    @staticmethod
    def show_all():
        pl.show()
        pl.figure(figsize=(8, 8))