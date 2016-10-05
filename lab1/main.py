from lab1.dataset import Dataset
from lab1.drawer import Drawer
from lab1.coordinate import Coordinate
from lab1.classifier import Classifier

# 1 read
dataset = Dataset()
dataset.read('chips.txt')
dataset.print_info()

# 2 center & polar
center = Coordinate.get_center(dataset.data)
Coordinate.translate(dataset.data, center)
Coordinate.to_polar(dataset.data)

# 3 normalize
Coordinate.normalize_polar(dataset.data)
#
'''
Drawer.draw_polar_grid()
Drawer.draw_dataset_polar(dataset, ['red', 'blue'])
Drawer.limits([[-1.0, 1.0], [-1.0, 1.0]])
Drawer.show_all()
'''

# 4 shuffle
dataset.shuffle()

folds = 5
k = 3
classes = 2

res_acc = [[0] * 10 for i in range(10)]
res_f1 = [[0] * 10 for i in range(10)]
res_sum = [[0] * 10 for i in range(10)]
res_recall = [[0] * 10 for i in range(10)]
res_precision = [[0] * 10 for i in range(10)]

for folds in range(2, 10):
    for k in range(1, 10):
        #print()
        #print("Folds: " + str(folds))
        #print("K: " + str(k))
        labels, trains, tests = Classifier.cross_validation(dataset, folds, k, classes)
        acc = sum([Classifier.accuracy(labels[i], tests[i]) * 100 for i in range(len(labels))]) / len(labels)
        f1_r_p = [Classifier.recall_precision(labels[i], tests[i], 0) for i in range(len(labels))]
        f1 = sum([f1_r_p[i][0] for i in range(len(labels))]) / len(labels) * 100
        rec = sum([f1_r_p[i][1] for i in range(len(labels))]) / len(labels) * 100
        prec = sum([f1_r_p[i][2] for i in range(len(labels))]) / len(labels) * 100
        #print("Accuracy: " + str(acc) + " %")
        #print("F1: " + str(f1) + "%")
        #print("Recall: " + str(rec) + "%")
        #print("Precision: " + str(prec) + "%")
        res_acc[folds][k] = acc
        res_f1[folds][k] = f1
        res_recall[folds][k] = rec
        res_precision[folds][k] = prec
        res_sum[folds][k] = acc + f1

for i in res_acc:
    print(' '.join(["%5.2f" % x for x in i]))
print()
for i in res_f1:
    print(' '.join(["%5.2f" % x for x in i]))
print()
for i in res_sum:
    print(' '.join(["%6.2f" % x for x in i]))
print()


def get_max(matrix):
    maxi, maxj, maxval = 0, 0, matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > maxval:
                maxval = matrix[i][j]
                maxi = i
                maxj = j
    return maxval, maxi, maxj

max_sum, i, j = get_max(res_sum)
print("Accuracy: " + str(res_acc[i][j]) + " %")
print("F1: " + str(res_f1[i][j]) + "%")
print("Recall: " + str(res_recall[i][j]) + "%")
print("Precision: " + str(res_precision[i][j]) + "%")