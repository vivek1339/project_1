import numpy as np
class rbfnn():
	def __init__(self,hidden_size,sigma=1.0):
		self.hidden_size=hidden_size
		self.sigma=sigma
		self.centres=[]
		self.weights=[]
		self.beta=1/(np.power(self.sigma,2)*2)
	def kernel_function(self,centre,data_point):
		return np.exp(-1*self.sigma*np.power(np.linalg.norm(centre-data_point),2))
	def calculate_interpolation_matrix(self,x):
		G=np.zeros((len(x),self.hidden_size))
		for data_point_arg,data_point in enumerate(x):
			for centre_arg,centre in enumerate(self.centres):
				G[data_point_arg,centre_arg]=self.kernel_function(centre,data_point)
		return G
	def calculate_centres(self,x):
		return x[np.random.choice(len(x),self.hidden_size)]
	def fit(self,x,y):
		self.centres=self.calculate_centres(x)
		self.weights=np.dot(np.linalg.pinv(self.calculate_interpolation_matrix(x)),y)
	def predict(self,x):
		return np.dot(self.calculate_interpolation_matrix(x),self.weights)



