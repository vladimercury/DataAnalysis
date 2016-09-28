import pylab as pl
from matplotlib.colors import ListedColormap


def draw_dots(dataset):
    color_map = ListedColormap(['#FF0000', '#0000FF'])
    pl.scatter([x[0][0] for x in dataset],
               [x[0][1] for x in dataset],
               c=[x[1] for x in dataset],
               cmap=color_map)
    pl.show()
