import numpy as np
from sklearn.manifold import TSNE

from import_csv import get_dsv_data

if __name__ == '__main__':
    file_name = 'results.csv'
    data_item_list = get_dsv_data(file_name)
    print(data_item_list)
    # X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    # X_embedded = TSNE(n_components=2).fit_transform(X)
    # reduction_shape = X_embedded.shape
    # print(reduction_shape)
    # print(X_embedded)