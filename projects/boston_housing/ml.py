# Import libraries necessary for this project
import numpy as np
import pandas as pd
from sklearn.cross_validation import ShuffleSplit

# Import supplementary visualizations code visuals.py
import visuals as vs



def load_data(file_path):
	# Load the Boston housing dataset
	data = pd.read_csv(file_path)
	y = data['MEDV']
	x = data.drop('MEDV', axis = 1)
	# Success
	print("Boston housing dataset has {} data points with {} variables each.".format(*data.shape))
	return(x,y)



