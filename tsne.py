import numpy as np
from sklearn.manifold import TSNE

from import_csv import get_dsv_data

if __name__ == '__main__':
    file_name = 'results.csv'
    data_item_list = get_dsv_data(file_name)
    X = np.array(data_item_list)
    X_embedded = TSNE(n_components=2).fit_transform(X)
    reduction_shape = X_embedded.shape
    print(reduction_shape)
    # print(X_embedded)