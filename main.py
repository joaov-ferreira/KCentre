import sys
import argparse

#import functions from files
from generate import *
from solve import *
from plot import *
from evalu import *


def main():
	
	parser = argparse.ArgumentParser(description='Example of the K center problem')
	parser.add_argument('-c','--cluster',help = 'Generate', action="store_true")
	parser.add_argument('--nc', help='Number of clusters for cluster generation, default = 5', type=int, nargs='?', const=5, default=5)
	parser.add_argument('-s','--sol',help = 'Solution method 2approx or select')
	parser.add_argument('-k',type=int,help = 'Number of centers')
	parser.add_argument('-p',type=int,help = 'Number of points')
	parser.add_argument('--plot',help='Enables plot of the solution',action="store_true")
	
	
	
	args = parser.parse_args()
	
	
	if (args.cluster):
		P = clusterGenerate(args.p,args.nc,20,20)
	
	else:
		P = generateUniform(args.p)
		
  
	if (args.sol == '2approx'):
		C = twoapprox(P,args.k)
	
	if (args.sol == 'select'):
		C = centerselection(P,5,100,50)
    
	m = evaluate(P,C)
	
	print(m)
	
	if (args.plot):
		plot(P,C, m)
     
	return
		
    

if __name__ == '__main__':
    main()
