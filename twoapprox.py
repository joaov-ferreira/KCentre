import sys

#import functions from files
from generate import *
from solve import *
from plot import *
from evalu import *

def main(args):
	P = generateUniform(20)
	C = twoapprox(P,4)
	
	maxdistance = evaluate(P,C)
	print 'The maximun distance was : ', maxdistance
	
	plot(P,C,maxdistance)
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
