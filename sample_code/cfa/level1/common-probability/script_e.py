import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.linspace(-5, 5, 1000)
y = (1/np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# Plot the normal distribution
plt.plot(x, y, color='steelblue')

# Annotations
plt.annotate(
    'The normal curve is symmetrical.\nThe two halves are identical.',
    xy=(0, 0.2), xytext=(0, 0.42), horizontalalignment='center')

plt.annotate('',
    xy=(0.65, 0.35), xytext=(1.4, 0.4),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

plt.annotate('',
    xy=(-0.66, 0.35), xytext=(-1.4, 0.4),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

plt.annotate('Theoretically, the curve\nextends to - ∞.',
             xy=(-3.55, 0.013), xytext=(-3.2, 0.1),
             arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
             horizontalalignment='center')

plt.annotate(
    'Theoretically, the curve\nextends to + ∞.',
    xy=(3.5, 0.013), xytext=(3.2, 0.1),
    arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
    horizontalalignment='center')

plt.annotate('The mean, median,\nand mode are equal.',
             xy=(0, -0.05), xytext=(0, -0.2),
             arrowprops=dict(facecolor='black', lw=1, arrowstyle='->'),
             horizontalalignment='center')

# Axes labels
plt.hlines(y=-0.05, xmin=-4.9, xmax=5.1, color='black', lw=1, linestyle='-')
plt.vlines(x=0, ymin=-0.05, ymax=0.4, color='black', lw=1, linestyle='-')


# Remove x-axis, y-axis ticks
plt.xticks([])
plt.yticks([])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Set limits
plt.xlim(-4.9, 4.8)
plt.ylim(-0.15, 0.55)

# Show plot
plt.savefig('figureE.png', transparent=True)
plt.show()