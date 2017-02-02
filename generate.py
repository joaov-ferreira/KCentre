#######################################################################
####### Functions for generating the points in a 2D plane ############# 
#######################################################################

import random as pyrandom
from evalu import dist

# Generates random points with uniform distribution

def generateUniform(numberPoints):
    P = []
    dimension = 2

    for n in range(numberPoints):
        point = []
        for j in range(dimension):
            point.append(pyrandom.randint(0,1000))

        P.append(point)

    return P

# Generate random points with a cluster distribution
#
#	N_Points 			- Number os points
#	N_Clusters 			- Number of Clusters
#	offset				- Defines a circle arround the center of the cluster
#						  The points will be randomly placed inside this circle
#	mindistance			- Minimun distance between two clusters, default = 5
#

def clusterGenerate(N_Points,N_Clusters, offset,mindistance = 50):
    clusters = []
    points = []
    threshold = mindistance

    i = 0
    while (i < N_Clusters):
        p = []
        for j in range(2):
            p.append(pyrandom.randint(0+offset*2,1000-offset*2))
    
        if (i!=0):
            add = True
            for j in clusters:                
                if (dist(p,j) < threshold):
                    add = False
            
            if (add):
                clusters.append(p)
                i+=1
        else:
            clusters.append(p)
            i+=1
    
    for i in range(N_Points):
        cluster = clusters[i % len(clusters)]
        p = []
        xcoord = cluster[0] + pyrandom.randint(-offset,offset)
        ycoord = cluster[1] + pyrandom.randint(-offset,offset)
        p = [xcoord,ycoord]
        points.append(p)

    return points
