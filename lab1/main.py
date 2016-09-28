from lab1.dataset import Dataset
from lab1.drawer import Drawer
from lab1.coordinate import Coordinate

# 1 read
dataset = Dataset()
dataset.read('chips.txt')
dataset.print_info()

# 2 center & polar
center = Coordinate.get_center(dataset)
Coordinate.translate(dataset, center)
Coordinate.to_polar(dataset)

# 3 normalize
Coordinate.normalize_polar(dataset)
#
Drawer.draw_polar_grid()
Drawer.draw_dataset_polar(dataset, ['red', 'blue'])
Drawer.limits([[-1.5, 1.5], [-1.5, 1.5]])
Drawer.show_all()

# 4 shuffle
dataset.shuffle()
