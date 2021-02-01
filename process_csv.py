import csv

def read_csv_data(file_name):
    data_item_list = []
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_item_list.append(row)
    return data_item_list

def save_csv_data(file_name, data_item_list):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data_item_list)

# if __name__ == '__main__':
#     # read_csv_data()
#     data_item_list = [[1,2], [3, 4]]
#     file_name = 'results.csv'
#     save_csv_data(file_name, data_item_list)
