import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
	return 1000 - 298*x + 3*(x**(2/3))

def f_prime(x):
	return -298 + 2*(x**(-1/3))

def solve(x, eps):
	new_x = -1
	rows = {'Iteration no':[], 'estimate':[], 'error':[]}
	for i in range(10):
		rows['Iteration no'].append(i+1)
		new_x = x - (f(x) / f_prime(x))
		rows['estimate'].append(new_x)
		err = abs((new_x - x) / new_x) * 100
		rows['error'].append(err)
		x = new_x
		#if (err <= eps):
			#break
	pd.set_option("display.precision", 20)
	df = pd.DataFrame(rows)
	print(df)
	return x

def plot_curve():
	x = np.arange(3, 4, 0.005)
	y = f(x)

	plt.plot(x, y)
	plt.show()

if __name__ == '__main__':
	plot_curve()
	print(solve(1000000, 0.05))
  