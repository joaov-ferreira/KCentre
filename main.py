import math
import random
import matplotlib.pyplot as plt
#import pylab

__author__ = 'ferreiraduar_joa'


def twoapprox(P, k):

    aux = P[:]           # Makes a copy of the list whitout reference
    p = random.choice(P) # takes out a random element
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


#def knapsack

#def dominant


#def generatePerlinNoise

#

def generateUniform(numberPoints):
    P = []
    dimension = 2

    for n in range(numberPoints):
        point = []
        for j in range(dimension):
            point.append(random.randint(0,100))

        P.append(point)

    return P



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




def dist(a,b):
     return math.sqrt(sum( (a - b)**2 for a, b in zip(a, b)))




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


def plot(P,C,maxdistance):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(*zip(*P), color = ['blue'])
    plt.scatter(*zip(*C), color = ['red'])

    for i in C:
        circle = plt.Circle((i[0],i[1]),maxdistance,color='g', fill=False)
        ax.add_patch(circle)

    plt.show()


def clusterGenerate(N_Points,N_Clusters, offset,mindistance = 5):
    clusters = []
    points = []
    threshold = mindistance

    i = 0
    while (i < N_Clusters):
        p = []
        for j in range(2):
            p.append(random.randint(0+offset*2,100-offset*2))
    
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
        xcoord = cluster[0] + random.randint(-offset,offset)
        ycoord = cluster[1] + random.randint(-offset,offset)
        p = [xcoord,ycoord]
        points.append(p)

    return points



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


def main():

    P = generateUniform(4)
    
    a = calcdists(P) 
    
    print(P)
    print(a)    
    return
    
    
    for k in range (1,50):



        l = []
        for i in range (50):
            P = generateUniform(50)
            C = twoapprox(P,k)
            l.append(evaluate(P,C))

        print ("Average distance for ", k," centers : ",sum(l) / float(len(l)))

    #print ("Max distance : ", maxdistance)

    #plot (P,C,maxdistance)

    #return


if __name__ == '__main__':
    main()
