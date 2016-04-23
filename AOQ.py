import numpy as np
import random

# size of the data set to test
sz = 1000000
data_set = np.random.rand(sz)

k = 30 #* j
#global m
m = 250 #* k
c = 2


print "m:",m, "\t", "k:",k, "\t", "c:",c

for j in range(1, 99):
	# set the value of p
	p = float(j/100.3)
	# converts the np array to binary based on p value
	p_data_set = []

	for t in np.nditer(data_set):
		if(t > p): 
			p_data_set.append(1)
		else: 
			p_data_set.append(0)

	defects = sz - np.count_nonzero(p_data_set)
	#print "The number of defects: ", defects, " out of a total of: ", sz

	#for j in range(1, 10):
		#for k in range(1, 10):
			# set values for eqn
	
	q = 1 - p
	# set up AOQ equation
	'''
	AOQ_num = float(p*(q**k)*(c+1)*(1 - (1/m)))
	AOQ_denom = float(1/m + q**k*(c+1-1/m))
	AOQ = float(AOQ_num / AOQ_denom)
	#print "AOQ: ", AOQ
	'''
	# Test the data_set
	# Sequentially test each item in the data set
	# define the global variables for the recursive program

	def sample_tester(sample):
		global good_count
		global bad_count 
		global k_count 
		global c_count
		global next_sample

		if (sample > 0):
			good_count += 1
			k_count += 1
			if (k_count > k):
				next_sample += random.randint(1, m)
			else:
				next_sample += 1
		elif (sample > 0 and c_count < c):
			c_count += 1
			next_sample += random.randint(1, m)
		else:
			bad_count += 1
			next_sample += 1
			k_count = 0
			next_sample += 1
		return next_sample

	good_count = 0 
	bad_count = 0 
	k_count  = 0 
	c_count = 0
	next_sample = 0

	while (next_sample < sz):
		test_sample = p_data_set[next_sample]
		next_sample = sample_tester(test_sample)

	#print "GOOD found: ", good_count
	#print "BAD found: ", bad_count
	#print "Total tested: ", good_count + bad_count
	missed = defects - bad_count
	#print "Number of defects not detected: ", missed
	missed_r = 1-(missed / float(defects))

	print round(p, 6), "\t", round(missed_r, 6)*100
	#print "_____________________________________________________________________________________\n\n"

print "END"
