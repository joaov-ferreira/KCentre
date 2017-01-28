#######################################################################
####### Functions for Solving the K center problem  ################### 
#######################################################################

import random as pyrandom
from evalu import dist

# Two approx algorithm to place K centers in the plane of the
# list P of points, returns a list of the centers.

def twoapprox(P, k):

    aux = P[:]           # Makes a copy of the list whitout reference
    p = pyrandom.choice(P) # takes out a random element
    aux.remove(p)        # in the list

    C = []
    C.append(p)          # add this element in the list

    while len(C) < k:
        distance = []
        for i in aux:

            myDistances =[] # List with distance to each center

            for j in C:
                myDistances.append(dist(i,j))

            myDistances.sort()
            distance.append(myDistances)
            distance.sort()

            if myDistances == distance[-1]:
                reponse = i

        aux.remove(reponse)
        C.append(reponse)

    return C
    
    
def dominant (P,k):
	
	C = []
	
	
	
	return C



def genetic (P,k, maxgenerations = 20, populationSize = 10):
	
	population = []
	for i in range(populationSize):
		temp = P(:) 			# Makes a copy of the list of points
		pyrandom.shuffle(temp)  #Then shuffles it
		population.append(temp)
		
	print (population)
	
	for generation in range(maxgenerations): #Now does the genetic part
			
	
	
	return C
