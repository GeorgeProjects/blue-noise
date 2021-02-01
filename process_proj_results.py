from process_csv import save_csv_data
import json

def load_json_obj(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def add_item_index(proj_point_list):
    '''
        add the index of project point item
    '''
    for i in range(len(proj_point_list)):
        proj_point_item = proj_point_list[i]
        proj_point_item.insert(0, i)
    return proj_point_list

if __name__ == '__main__':
    proj_results = load_json_obj('proj_results.json')
    proj_point_list = proj_results['Y']
    proj_point_list = add_item_index(proj_point_list)
    attr_names = ['index', 'x', 'y']
    proj_point_list.insert(0, attr_names)
    file_name = 'proj_point_list.csv'
    save_csv_data(file_name, proj_point_list)
