import matplotlib.pyplot as plt
import numpy as np
import math

# Data for normal distribution
mu = 0
sigma = 1
x_norm = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
y_norm = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_norm - mu)/sigma)**2)

# Data for lognormal distribution
mu_lognorm = 0
sigma_lognorm = 1
x_lognorm = np.linspace(0.01, 3, 100)
y_lognorm = (1 / (x_lognorm * sigma_lognorm * np.sqrt(2 * np.pi))) * np.exp(- (np.log(x_lognorm) - mu_lognorm)**2 / (2 * sigma_lognorm**2))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot normal distribution
ax1.plot(x_norm, y_norm)
ax1.set_title('Normal Distribution')
ax1.set_xlabel('$\mu$')
ax1.set_yticks([])
ax1.set_xticks([])
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(True)

# Plot lognormal distribution
ax2.plot(x_lognorm, y_lognorm)
ax2.set_title('Lognormal Distribution')
ax2.set_yticks([])
ax2.set_xticks([0])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(True)
ax2.set_ylim(bottom=0)
ax2.set_xlim(left=-0.2)
ax2.axvline(x=0, color='black', linestyle='-', linewidth=1)

plt.tight_layout()
plt.savefig('figureK.png', transparent=True)
plt.show()
