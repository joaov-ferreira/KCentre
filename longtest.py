import sys
import argparse
import matplotlib.pyplot as plt

#import functions from files
from generate import *
from solve import *
from plot import *
from evalu import *



def main():
	
	parser = argparse.ArgumentParser(description='Realise many solutions of the problem')
	parser.add_argument('-c','--cluster',help = 'Generate in cluster mode instead of uniform', action="store_true")
	parser.add_argument('--nc', help='Number of clusters for cluster generation, default = 5', type=int, nargs='?', const=5, default=5)
	parser.add_argument('-n','--npoints',help = 'Number of points, default = 100', type=int, const = 100, default = 100, nargs='?')
	parser.add_argument('-k','--ncenters', help='Number of centers in the first test, default = 3', type=int, nargs='?', const=3, default=3)
	parser.add_argument('-s','--sol',help = 'Solution method 2approx or select')
	parser.add_argument('-t',type=int,help = 'Number of tests, default = 15',const = 15, default = 15, nargs='?')
	parser.add_argument('-g','--gen',help='Method of generation of points in 2D plane')
	
	args = parser.parse_args()
	
	res = []
	x = []
	
	k = args.ncenters

	for i in range(args.t):
		part = [] # Partial results
		for j in range(50):
			if (args.cluster):
				P = clusterGenerate(args.npoints,args.nc,20,20)
	
			else:
				P = generateUniform(args.npoints)
	
			if (args.sol == '2approx'):
				C = twoapprox(P,k)
	
			if (args.sol == 'select'):
				C = centerselection(P,k,100,50)
    
			part.append(evaluate(P,C))
	
		res.append(sum(part)/len(part))
		x.append(k)
		k = k+1
		
		
	print res
	
	fig = plt.figure()
	
	plt.plot(x,res)
	plt.show()
	
	return 0

if __name__ == '__main__':
    main()
