#######################################################################
####### Functions for Evaluating the performance of the  ##############
#######						Solution                     ############## 
#######################################################################

import math as pymath

# I think this doesn't work D:
def calcdists(Points):
    
    distances = []
    
    for i in range(len(Points)):
        for j in range(i+1,len(Points)):
            p = []
            p.append(dist(Points[i],Points[j]))
            p.append(Points[i])
            p.append(Points[j])
    
    distances.sort()

    return distances


# Euclidean distance between two points
def dist(a,b):
     return pymath.sqrt(sum( (a - b)**2 for a, b in zip(a, b)))

# Returns the worst distance from a point to the nearest center
def evaluate(P,C):
    distances = []
    for i in P:
        distanceToCenter = []
        for j in C:
            # get the individual distance to each center
            distanceToCenter.append(dist(i,j)) 
        distanceToCenter.sort()
        distances.append(distanceToCenter)

    distances.sort()
    return distances[-1][0]

# I totally forgot what this suposed to be

def performance_evaluation(a,b):
    distances = []
    for k in range(1,a+1):
        temp = []
        for n in range(3,b+1):
            P = generateUniform(n)
            C = twoapprox(P,k)
            maxdistance = evaluate(P,C)
            temp.append(maxdistance)
        distances.append(temp)
    return distances
