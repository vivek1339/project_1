import math
import random
import numpy as np
def min_value(Fitness_array,sol):
	best=0
	for i in range(len(Fitness_array)):
		if(Fitness_array[i]<Fitness_array[best]):
			best=i
	return sol[i]
def fitness(a,sol,k):
	val = 0.0
	inter=999.0
	#print(sol)
	for j in sol:
		dist=np.sum(np.power(np.array(j)-np.array(a),2))
		if(dist!=0):	
			if(dist<inter ):
				inter=dist
	intra=0.0
	for j in range(len(k)):
		intra+=np.sum(np.power(np.array(a)-np.array(k[j]),2))
	#print(intra)
	intra/=len(k)
	return intra/inter
def bat(data):
	Bmax=50
	A=1
	Fmin=0
	Fmax=10
	Imax=10
	r=0.1
	gamma=0.9
	alpha=0.9
	K=[]
	dims=len(data[0])
	for i in data:
		if(i[8]==1):
			K.append(i)
	velocities=np.zeros((len(K),dims))
	sol=np.zeros((len(K),dims))
	v=np.zeros((len(K),dims))
	Fitness_array=np.zeros((len(K)))
	best=[0]*dims
	Q=[0]*len(K)
	for k in range(2,len(K)):
		print(k)
		for i in range(1,Bmax):
			Fi=Fmin+random.random()*(Fmax-Fmin)
			for j in range(dims):
				v[i][j]=v[i][j]+(sol[i][j]-best[j])*Q[i]
				sol[i][j]=sol[i][j]+v[i][j]
			Fitness_array[i]=fitness(sol[i],sol,K)
		best=min_value(Fitness_array,sol)
		Iter=1
		rnd= np.random.random_sample()
		while Iter<=Imax:
			for i in range(1,Bmax):
				if(rnd>r):
					for j in range(dims):
						sol[i][j]=sol[i][j]+A*np.random.random_sample()
				if(A>rnd and fitness(best,sol,K)>=fitness(sol[i],sol,K)):
					#print(r)
					
					r=r*(1-np.exp(gamma))
					A=A*alpha
			best=min_value(Fitness_array,sol)
			Iter+=1
		best=min_value(Fitness_array,sol)

	best=min_value(Fitness_array,sol)
	return best