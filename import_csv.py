import csv

def get_dsv_data(file_name):
    data_item_list = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
            data_item_list.append(row)
    return data_item_list

# if __name__ == '__main__':
#     get_dsv_data()