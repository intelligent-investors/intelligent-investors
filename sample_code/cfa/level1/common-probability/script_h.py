import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 6  # mean
sigma = 2  # standard deviation
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 1000)

# Z value
z = (4.10 - mu) / sigma
p_value = norm.cdf(z)

# Plotting the distribution
plt.figure(figsize=(10, 6))
plt.plot(x, norm.pdf(x, mu, sigma), label='Normal Distribution')

# Filling the area under the curve for P(EPS < $4.10)
YMIN = -0.01
x_fill = np.linspace(mu - 3*sigma, 4.10, 1000)
plt.axvline(x=mu, ymin=0, ymax=0.95, color='black', linewidth=1)
plt.fill_between(
    x_fill, norm.pdf(x_fill, mu, sigma), y2=YMIN,
    color='skyblue', alpha=0.4, label=f'P(EPS < $4.10) = {p_value:.4f}')

x_fill = np.linspace(7.9, 7.9 + 2*sigma, 1000)
plt.fill_between(
    x_fill, norm.pdf(x_fill, mu, sigma), y2=YMIN,
    color='skyblue', alpha=0.4, label=f'P(EPS < $4.10) = {p_value:.4f}')

plt.annotate('0.171',
    xy=(3, 0.05), xytext=(2, 0.1),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

plt.annotate('0.171',
    xy=(9, 0.05), xytext=(10, 0.1),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

plt.title('')
plt.xlabel('')
plt.ylabel('')
plt.xticks([2, 4.10, 6, 7.9], ['EPS:\nz-values', '$4.10\n-0.95', '$6.00\n0', '\n+0.95'])
plt.yticks([])

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['bottom'].set_position(('data', YMIN))


# Display the plot
plt.savefig('figureH.png', transparent=True)
plt.show()
