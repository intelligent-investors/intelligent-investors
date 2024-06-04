import numpy as np
from scipy.stats import norm, kurtosis
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(-5, 5, 1000)
normal_dist = norm.pdf(x, 0, 1)  # Normal distribution with mean 0 and standard deviation 1
leptokurtic_dist = norm.pdf(x, 0, 0.75)  # Leptokurtic distribution with mean 0 and standard deviation 0.75

# Calculate kurtosis
kurtosis_normal = kurtosis(normal_dist)  # Kurtosis of the normal distribution
kurtosis_leptokurtic = kurtosis(leptokurtic_dist)  # Kurtosis of the leptokurtic distribution

# Plotting the distributions
plt.figure(figsize=(8, 6))
plt.plot(x, leptokurtic_dist, linestyle='--', color='black')
plt.plot(x, normal_dist)

# Show x-axis
plt.axhline(0, color='gray', linewidth=0.5)

# Remove spines and tickers
plt.gca().spines.values()
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.xticks([])
plt.yticks([])

# Add text labels
plt.annotate(
    'Normal Distribution',
    xytext=(-5, 0.15),
    xy=(-1.65, 0.1),
    arrowprops=dict(arrowstyle='->')
)
plt.annotate(
    'Leptokurtic',
    xytext=(2, 0.4),
    xy=(0.5, 0.45), 
    arrowprops=dict(arrowstyle='->')
)

# Display the plot
plt.ylim(-0.01, 0.54)
plt.legend()
plt.savefig('figure7.png', transparent=True)
plt.show()