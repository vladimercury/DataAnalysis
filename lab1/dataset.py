class Dataset:
    def __init__(self, new_data=[]):
        self.data = new_data

    def read(self, filename):
        self.data = []
        raw_data = open(filename).read().split()
        for i in range(0, len(raw_data), 3):
            self.data.append(
                [[float(raw_data[i].replace(',', '.')), float(raw_data[i + 1].replace(',', '.'))],
                 int(raw_data[i + 2])])

    def get_info(self):
        return {"length": len(self.data)}

    def get_data(self):
        return self.data

    def get_dots(self):
        return [x[0] for x in self.data]

    def print_data(self):
        [print(str(x[1]) + ": " + str(x[0])) for x in self.data]

    def print_info(self):
        info = self.get_info()
        [print(str(x) + ": " + str(info[x])) for x in info]

    def shuffle(self):
        import random
        random.shuffle(self.data)