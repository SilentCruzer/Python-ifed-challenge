import time
import numpy as np

def usingNumpy(all_elem, subset):
	"""
	It gives the length of an array containing the common
	values of two arrays using the numpy module

	Parameters:
	-----------
	all_elem: array
	subset: array

	Returns:
	-----------
	Length of array containing the common elements of arrays passed in through the 
	arguments

	"""
	verified_elements = np.intersect1d(subset,all_elem)
	return len(verified_elements)

def usingNormal(all_elem,subset):
	"""
	It gives the length of an array containing the common
	values of two arrays using the inbuilt fuctions of python

	Parameters:
	-----------
	all_elem: array
	subset: array

	Returns:
	-----------
	Length of array containing the common elements of arrays passed in through the 
	arguments

	"""
	verified_elements = set(all_elem) & set(subset)
	return len(verified_elements)

if __name__ == "__main__":

	with open('subset_elemets.txt') as f:
	    subset_elements = f.read().split('\n')
	    
	with open('all_elements.txt') as f:
	    all_elements = f.read().split('\n')

	start = time.time()
	all_elements = np.array(all_elements)

	print(usingNumpy(all_elements, subset_elements))
	print(usingNormal(all_elements, subset_elements))
	print('Duration: {} seconds'.format(time.time() - start))