import math


class Classifier:
    @staticmethod
    def classify_knn(train_data, test_data, k, n_classes):
        def dist_pp(a, b):
            return math.fabs(a[0] - b[0])

        def dist_p(a, b):
            return math.sqrt(a[0]**2 + b[0]**2 - 2 * a[0] * b[0] * math.cos(b[1] - a[1]))

        def dist(a, b):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        test_labels = []
        for test_point in test_data:
            test_dist = [[dist_pp(test_point[0], train_data[i][0]), train_data[i][1]] for i in range(len(train_data))]
            stat = [0 for i in range(n_classes)]
            for d in sorted(test_dist)[0:k]:
                stat[d[1]] += 1
            test_labels.append( sorted(zip(stat, range(n_classes)), reverse=True)[0][1] )
        return test_labels

    @staticmethod
    def cross_validation(dataset, parts, k, n_classes):
        l = len(dataset.data)
        pl = l // parts if l % parts == 0 else l // parts + 1
        labels = []
        trains = []
        tests = []
        for i in range(parts):
            train_data = dataset.data[i * pl:(i+1) * pl]
            test_data = dataset.data[0:i*pl] + dataset.data[(i+1)*pl:]
            labels.append(Classifier.classify_knn(train_data, test_data, k, n_classes))
            trains.append(train_data)
            tests.append(test_data)
        return labels, trains, tests

    @staticmethod
    def accuracy(labels, tests):
        return sum([int(labels[i]==tests[i][1]) for i in range(len(tests))]) / float(len(tests))

    @staticmethod
    def generate_mesh(train):
        import numpy as np
        x_min = min([train[i][0][0] for i in range(len(train))]) - 1.0
        x_max = max([train[i][0][0] for i in range(len(train))]) + 1.0
        y_min = min([train[i][0][1] for i in range(len(train))]) - 1.0
        y_max = max([train[i][0][1] for i in range(len(train))]) + 1.0
        h = 0.05
        testX, testY = np.meshgrid(np.arange(x_min, x_max, h),
                                   np.arange(y_min, y_max, h))
        return [testX, testY]

    @staticmethod
    def get_mesh(train, k, n_classes):
        from lab1.coordinate import Coordinate
        test_mesh = Classifier.generate_mesh(train.data)
        mesh_labels = Classifier.classify_knn(train.data,
                                              Coordinate.to_polar([[[x[0], x[1]], 0] for x in zip(test_mesh[0].ravel(), test_mesh[1].ravel())]),
                                              k,
                                              n_classes)
        return mesh_labels, test_mesh

