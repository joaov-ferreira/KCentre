
import matplotlib.pyplot as plt

#Plot a visualization of the problem

def plot(P,C,maxdistance):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    plt.scatter(*zip(*P), color = ['blue'])
    plt.scatter(*zip(*C), color = ['red'])

    for i in C:
        circle = plt.Circle((i[0],i[1]),maxdistance,color='g', fill=False)
        ax.add_patch(circle)

	plt.axis('equal')
    plt.show()
