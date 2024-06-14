import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mu = 6.0
sigma = 2.0

# Values for the EPS and corresponding z-values
eps = [6.0, 9.7]
z_values = [0, 1.85]

# x values for the plot
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

# Plot the normal distribution curve
plt.plot(x, y, label='Normal Distribution')

# Fill the area under the curve
x_fill = np.linspace(z_values[1] * sigma + mu, mu + 4*sigma, 1000)
y_fill = norm.pdf(x_fill, mu, sigma)

plt.fill_between(x_fill, y_fill, y2=-0.003, alpha=0.3)
plt.axvline(x=mu, ymin=-0.003, ymax=0.95, color='black', linewidth=1)

# Annotations
plt.annotate('0.0322',
    xy=(11, 0.02), xytext=(12, 0.06),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

# X-axis labels for EPS and z-values
eps = [2.3, 6.0, 9.7]
plt.xticks(eps, ['EPS:\nz-values', '$6.00\n0', '$9.70\n1.85'])
plt.yticks([])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['bottom'].set_position(('data', -0.003))

# Y-axis and X-axis labels
plt.xlabel('')
plt.ylabel('')

# Show the plot
plt.savefig('figureG.png', transparent=True)
plt.show()
