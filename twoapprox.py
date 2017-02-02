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



    for k in range (1,50):



        l = []
        for i in range (50):
            P = generateUniform(50)
            C = twoapprox(P,k)
            l.append(evaluate(P,C))

        print ("Average distance for ", k," centers : ",sum(l) / float(len(l)))

    print ("Max distance : ", maxdistance)

    plot (P,C,maxdistance)

    return
