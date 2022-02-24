from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(8, 2, 2) == 32
	assert simple_work_calc(8, 3, 2) == 65  #TODO: fix
	assert simple_work_calc(9, 2, 3) == 19  #TODO: fix
def test_work():
	""" done. """
	assert work_calc(8, 2, 2,lambda n: n) == 32 
	assert work_calc(8, 1, 2, lambda n: n*n) == 85 # TODO: fix
	assert work_calc(8, 3, 2, lambda n: 1) == 40   # TODO: fix
