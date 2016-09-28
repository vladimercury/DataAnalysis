def read_dataset(filename):
    raw_data = open('chips.txt').read().split()
    new_data = []
    for i in range(0, len(raw_data), 3):
        new_data.append(
            [(float(raw_data[i].replace(',', '.')), float(raw_data[i + 1].replace(',', '.'))),
              int(raw_data[i + 2])])
    return new_data


def print_dataset_info(dataset):
    print("Dataset length: " + str(len(dataset)))
