import numpy as np
from sklearn import preprocessing
#We imported a couple of packages. Let's create some sample data #and add the line to this file:
input_data = np.array([[3, -1.5, 3, -6.4], [0, 3, -1.3, 4.1], [1, 2.3, -2.9, -4.3]])

data_binarized = preprocessing.Binarizer(threshold=1.4).transform(input_data)
print ("\nBinarized data =", data_binarized)
