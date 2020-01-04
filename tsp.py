import sys
import cplex
import math


if len(sys.argv) < 2:
	print ("Usage: python3.4 tsp.py inputFile")
	sys.exit(1)

def read_data(filename):
	with open(filename) as f:
		data = f.read().split()
		floats = []
		for elem in data:
			try:
	        		floats.append(float(elem))
			except ValueError:
				pass
	return(floats)
	

file_it = read_data(sys.argv[1])


n = int(file_it[0]) # number of cities
del file_it[0]

c = []  #travelling cost vector
for i in range(n):
	c.append([])
	for j in range(n):
		if len(file_it) ==0:
			print("Data is not consistent")
			exit()
		c[i].append(int(file_it[0]))
		del file_it[0]

print(c)

def define_problem(prob):
		
	prob.set_problem_name ("tsp")
	prob.objective.set_sense(prob.objective.sense.minimize)

	for i in range(n): # variable denoting if the city i is travelled before j
		prob.variables.add(obj=c[i],lb = [0]*(n),
				ub = [1]*(n),
				types = ["B"]*(n))

	for i in range(n):
		cons = [ [ [i*(n) + j for j in range(n)], [1 for j in range(n)] ] ]  # constraint saying that there are two edges connected on each node: one incoming one outgoing
		prob.linear_constraints.add(lin_expr=cons, senses = ["E"], rhs = [1])
	for i in range(n):
		cons = [ [ [j*(n) + i for j in range(n)], [1 for j in range(n)] ] ]
		prob.linear_constraints.add(lin_expr=cons, senses = ["E"], rhs = [1])

	

def tsp():
	prob = cplex.Cplex()

	define_problem(prob)
	prob.solve()
	sol = prob.solution
	print("The IP is:", sol.status[sol.get_status()])
	#print("Cost = ", int(sol.get_objective_value()))

	for j in range(n):   # to check if there are subtours or not
		if sol.get_values(j) != 0:
			m = j
	s = 0
	S = []
	S.append(m)
	while m != 0:
		s += 1
		for j in range(n):
			if sol.get_values(m*n + j) != 0:
				m1 = j
				continue
		m = m1
		del m1
		S.append(m)

	
	while s < n-1:   # Until all the subtours are not eliminated keep on addign the constraints
		#print("subtour detected")
		print(S)
		cons = [ [ [],[]  ]  ]
		for i in S:
			for j in range(n):
				if j not in S:
					cons[0][0].append(i*n+j)
					cons[0][1].append(1)

		prob.linear_constraints.add(lin_expr=cons, senses = ["G"], rhs = [1])
		prob.solve()
		
		sol = prob.solution
		print(sol.status[sol.get_status()])
		#print("Number of cities =",n)
		#print("Cost = ", int(sol.get_objective_value()))

		
		for j in range(n):    # Repeat the process of eliminating subtours
			if sol.get_values(j) != 0:
				m = j
				continue
		s = 0
		S = []
		S.append(m)
		while m != 0:
			s += 1
			for j in range(n):
				if sol.get_values(m*n + j) != 0:
					m1 = j
					continue
			m = m1
			del m1
			S.append(m)

	numcols = prob.variables.get_num()
	print("Tour:")
	for j in range(0,numcols):
		if sol.get_values(j) != 0:
			print(" (%d,%d) " % (math.floor(j/n),j%n ))

	prob.write("tsp.lp")

tsp()
