import numpy as np
from scipy.stats import skewnorm
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
a = 4
mean, var, skew, kurt = skewnorm.stats(a, moments='mvsk')
x = np.linspace(skewnorm.ppf(0.01, a), skewnorm.ppf(0.99, a), 100)
rv = skewnorm(a)
pdf_values = rv.pdf(x)
ax.plot(x, pdf_values)

mean_value = skewnorm.mean(a)
median_value = skewnorm.median(a)
mode_value = x[np.argmax(rv.pdf(x))]

# Plot mean, median, and mode lines
ymax_mean = rv.pdf([mean_value])
ymax_median = rv.pdf(median_value)
ymax_mode = rv.pdf(mode_value)
ax.vlines(mean_value, color='black', linestyle='--', linewidth=1, label='mean', ymin=-0.05, ymax=ymax_mean)
ax.vlines(median_value, color='black', linestyle='--', linewidth=1, label='Median', ymin=-0.1, ymax=ymax_median)
ax.vlines(mode_value, color='black', linestyle='--', linewidth=1, label='Mode', ymin=-0.15, ymax=ymax_mode)

# Add text labels
ax.text(mean_value + 0.15, -0.09, 'Mean', verticalalignment='bottom', horizontalalignment='right')
ax.text(median_value + 0.11, -0.14, 'Median', verticalalignment='bottom', horizontalalignment='right')
ax.text(mode_value + 0.11, -0.19, 'Mode', verticalalignment='bottom', horizontalalignment='right')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.axhline(0, color='black', linestyle='-', linewidth=1)

ax.set_ylim(-0.15, max(rv.pdf(x)) + 0.01)
plt.savefig('figure6_2.png', transparent=True)
plt.show()