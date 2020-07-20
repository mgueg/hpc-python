import numpy as np
import matplotlib.pyplot as plt

arr = np.random.random(size=1000)
print("Uniform distribution")
print("Mean: ", np.mean(arr), "Std. dev.: ", np.std(arr))
plt.hist(arr, 50)
plt.title('Uniform distribution')

arr = np.random.normal(size=1000)
print("Normal distribution")
print("Mean: ", np.mean(arr), "Std. dev.: ", np.std(arr))
plt.figure()
plt.hist(arr, 50)
plt.title('Normal distribution')

arr = np.random.gamma(1000,size=1000)
print("Gamma distribution")
print("Mean: ", np.mean(arr), "Std. dev.: ", np.std(arr))
plt.figure()
plt.hist(arr, 50)
plt.title('gamma distribution')

b = np.random.exponential(size=1000)
print("exp distribution")
print("Mean: ", np.mean(b), "Std. dev.: ", np.std(b))
plt.figure()
plt.hist(b, 50)
plt.title('exp distribution')

plt.show()
