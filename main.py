import sys

#import functions from files
from generate import *
from solve import *
from plot import *
from evalu import *

def main():

    #P = clusterGenerate(20,5,2,20)
    
    P = generateUniform(20)
    
    C = centerselection(P,5,10)
    
    m = evaluate(P,C)
    plot(P,C, m)
      
    return
    
    
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


if __name__ == '__main__':
    main()
