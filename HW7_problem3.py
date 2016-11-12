import numpy as np 

def Gaussian_cdf(gaus_num, unif_num):
	gaus_samples = []
	var = np.sqrt(1/(12*unif_num))
	for i in range(gaus_num):
		unif_samples = np.random.uniform(0, 1, unif_num)
		gaus_samples.append(np.true_divide(np.mean(unif_sample)-0.5,var))
	gaus_samples = np.array(gaus_samples)
	value = len(gaus_samples[gaus_samples<=0.7])/gaus_num
	return (value)
Gaussian_cdf(1000000, 1000)

