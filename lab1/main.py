from lab1.dataset import Dataset
from lab1.drawer import Drawer
from lab1.coordinate import Coordinate
from lab1.classifier import Classifier

# 1 read
dataset = Dataset()
dataset.read('chips.txt')
dataset.print_info()

# 2 center & polar
center = Coordinate.get_center(dataset)
Coordinate.translate(dataset.data, center)
Coordinate.to_polar(dataset.data)

# 3 normalize
Coordinate.normalize_polar(dataset.data)
#
"""
Drawer.draw_polar_grid()
Drawer.draw_dataset_polar(dataset, ['red', 'blue'])
Drawer.limits([[-1.5, 1.5], [-1.5, 1.5]])
Drawer.show_all()
"""
# 4 shuffle
dataset.shuffle()

labels, trains, tests = Classifier.cross_validation(dataset, 5, 4, 2)
for i in range(len(labels)):
    print(Classifier.accuracy(labels[i], tests[i]))

mesh_labels, mesh = Classifier.get_mesh(dataset, 5, 2)
Drawer.draw_color_mesh(mesh, mesh_labels, ['#FFAAAA', '#AAAAFF'])
Drawer.draw_dataset_polar(dataset, ['red', 'blue'])
Drawer.limits([[-1.5, 1.5], [-1.5, 1.5]])
Drawer.show_all()