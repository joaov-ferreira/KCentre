#######################################################################
####### Functions for Solving the K center problem  ################### 
#######################################################################

import random as pyrandom
from evalu import dist

from plot import *

# Two approx algorithm to place K centers in the plane of the
# list P of points, returns a list of the centers.

def twoapprox(P, k):

    aux = P[:]           	# Makes a copy of the list whitout reference
    p = pyrandom.choice(P) 	# takes out a random element
    aux.remove(p)        	# in the list

    C = []
    C.append(p)          	# add this element in the centers list

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
                reponse = i	# Select the fartest point to a center

        aux.remove(reponse)
        C.append(reponse)	

    return C
    
    
# Center selection algorithm
    
def centerselection (P,k, initialRadius = 20, step = 5):
	
	solved = False
	radius = initialRadius
	
	while (not solved):
		C = []
		selection = P[:]
		
		while (len(selection) > 0):
			center = pyrandom.choice(selection)    	#random selection of a center
			C.append(center)

			#plot(P,C,radius)
				
			selection.remove(center)			   	#then removes it from the list
			
			tmp = selection[:]  #solves a bug
			
			for i in tmp:
				if (dist(center,i) <= radius):		# Now removes points that are closer
					selection.remove(i)		
				
				
			#if (len(selection) > 0):
			#	plot(selection,C,radius)
			
			if (len(C) > k):						# prevents testing with more than k center
				break
			
		radius = radius + step
	
		if (len(C) <= k):
			solved = True
	
		
	return C

