import numpy as np
import matplotlib.pyplot as plt
from sklearn.Naive_bayes import GaussianNB
from sklearn import cross_validation

from utilities import visualize_classifier

# input file containing data
input_file = 'data_multivar_nb.txt'

# Load data from input file
data = np.loadtxt(input_file, delimiter=',')
X, y = data[:, :-1], data[:, -1]

# Create Naive Bayes classifier