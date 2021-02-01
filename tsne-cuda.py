# -*- coding: utf-8 -*-
import os
import numpy as np
np.set_printoptions(precision=3)
import pandas as pd
import json

from sklearn.preprocessing import MinMaxScaler, StandardScaler
# from sklearn.manifold import TSNE
# from scipy.spatial import procrustes
from tsnecuda import TSNE

def standardize(raw_values):
    # raw_values = df.to_numpy()
    scaler = StandardScaler()
    values = scaler.fit_transform(raw_values)
    return values
    # return pd.DataFrame(values, columns=dims)

def proj(X):
    Y = TSNE(n_components=2).fit_transform(X)
    # scaler = MinMaxScaler()
    # Y = scaler.fit_transform(Y)
    # Y = Y.tolist()
    # Y = np.round(Y, decimals=3).tolist()
    return Y

def main():
    # csv_name = 'lamost_sample.csv'
    csv_name = 'test.csv'

    df = pd.read_csv(csv_name, header=None)

    arr = df.loc[:].to_numpy()
    standardize_arr = standardize(arr)

    proj_res = proj(standardize_arr)

    # json_dir = 'lamost_sample.json'
    json_dir = 'proj_results.json'
    with open(json_dir, 'w') as fp:
        json.dump(proj_res, fp)

if __name__ == "__main__":
    main()