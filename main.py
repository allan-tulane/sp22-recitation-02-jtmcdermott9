"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	
	# TODO
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    return a * simple_work_calc(n//b, a, b) + n

def test_simple_work():
	""" done. """
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 65
	assert simple_work_calc(9, 2, 3) == 19
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(10, 3, 3) == 28
	assert simple_work_calc(15, 2, 3) == 29

def work_calc(n, a, b, f):

	if n == 0:
		return 0
	if n == 1:
		return 1

	else:
		return a * work_calc(n//2, a, b, f) + f(n)
	

def span_calc(n, a, b, f):
	"""Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	# TODO
	return math.log(n, b)

def test_work():
	""" done. """
	assert work_calc(8, 2, 2,lambda n: n) == 32 
	assert work_calc(8, 1, 2, lambda n: n*n) == 85 
	assert work_calc(8, 3, 2, lambda n: 1) == 40   
	assert work_calc(10, 2, 2, lambda n: n*n*n) == 1290
	assert work_calc(10, 3, 3, lambda n: n*n*n*n) == 12046
	assert work_calc(15, 2, 3, lambda n: 3) == 3


def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	
	"""
	result = []
	for n in sizes:
		# compute W(n) using current a, b, f
		result.append((
			n,
			work_fn1(n),
			work_fn2(n)
			))
	return result

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_work():
	# curry work_calc to create multiple work
	# functions that can be passed to compare_work
    
	# create work_fn1
	# create work_fn2
	work_fn1 = work_calc(n, 2, 2,lambda n: n)
	work_fn2 = work_calc(n, 3, 2,lambda n: n) 
	#work_fn
	

	res = compare_work(work_fn1, work_fn2)
	#res2 = compare_work(work_fn3, work_fn4)
	print(res)
	#print(res2)
  

def test_compare_span():
	# TODO
  pass

def printSttuff():

	print(work_calc(10, 2, 2, lambda n: n*n*n)) 
	print(work_calc(10, 3, 3, lambda n: n*n*n*n)) 
	print(work_calc(15, 2, 3, lambda n: 3)) 

test_compare_work()