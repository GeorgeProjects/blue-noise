import csv

def get_dsv_data(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
        print(reader)

# if __name__ == '__main__':
#     get_dsv_data()