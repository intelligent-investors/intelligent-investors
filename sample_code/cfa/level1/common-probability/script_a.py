import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define the range for the x-axis
x = np.linspace(-4, 4, 1000)

# Create the figure and the subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Plot the Probability Density Function (PDF)
ax1.plot(x, norm.pdf(x))
ax1.fill_between(x, -0.02, norm.pdf(x), where=(x <= -1), alpha=0.5)
ax1.annotate(
    'F(-1.0) = 0.1587',
    xytext=(-4, 0.1),
    xy=(-1.05, 0.02),
    arrowprops=dict(arrowstyle='->')
)
ax1.set_title('(a) Probability density function')
ax1.vlines(x=0, ymin=-0.05, ymax=norm.pdf([0])[0], color='black', linestyle='-')
ax1.set_xticks([-1, 0, 1])
ax1.set_yticks([])
ax1.xaxis.set_visible(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.set_ylim(-0.02, 0.45)

# Plot the Cumulative Distribution Function (CDF)
ax2.plot(x, norm.cdf(x))
ax2.axhline(y=0.1587, xmin=-3, xmax=-1, color='black', linestyle='--')
ax2.vlines(x=-1, ymin=-0.05, ymax=0.1587, color='black', linestyle='--')
ax2.hlines(y=0.1587, xmin=-5, xmax=-1, color='black', linestyle='--')
ax2.text(-1, 0.1587, '0.1587', verticalalignment='bottom', horizontalalignment='right')
ax2.set_title('(b) Cumulative distribution function')
ax2.set_xticks([-1, 0])
ax2.set_yticks([0, 0.1587, 1])
ax2.set_yticklabels(['0', '0.1587', '1'])
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['bottom'].set_visible(True)
ax2.set_ylim(-0.05, 1)
ax2.set_xlim(-4.1, 4.1)

# Adjust the layout and display the plot
plt.tight_layout()
plt.savefig('figureA.png', transparent=True)
plt.show()