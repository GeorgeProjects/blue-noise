import numpy as np
from sklearn.manifold import TSNE

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_components=2).fit_transform(X)
reduction_shape = X_embedded.shape
print(reduction_shape)
print(X_embedded)