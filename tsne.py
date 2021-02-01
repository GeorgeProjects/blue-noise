import numpy as np
from sklearn.manifold import TSNE

from import_csv import read_csv_data, save_csv_data

if __name__ == '__main__':
    file_name = 'embeddings-results.csv'
    file_name_2d = 'embeddings-results-2d.csv'
    data_item_list = read_csv_data(file_name)
    X = np.array(data_item_list)
    X_embedded = TSNE(n_components=2).fit_transform(X)
    reduction_shape = X_embedded.shape
    save_csv_data(file_name_2d, X_embedded)
    