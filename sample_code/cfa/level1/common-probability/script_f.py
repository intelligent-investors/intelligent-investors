import matplotlib.pyplot as plt
import numpy as np

# Generate data for a standard normal distribution
x = np.linspace(-3, 3, 1000)
y = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * x**2)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normal Distribution')
plt.hlines(y=-0.01, xmin=-3.5, xmax=3.5, linestyle='-', color='gray')
plt.vlines(x=-3.2, ymin=-0.01, ymax=0.5, linestyle='-', color='gray')

# Adding annotations for the mean and standard deviations
plt.text(0, -0.03, 'E(x)', horizontalalignment='center', fontsize=12)
plt.text(-1, -0.03, '-σ', horizontalalignment='center', fontsize=12)
plt.text(1, -0.03, '+σ', horizontalalignment='center', fontsize=12)
plt.text(-2, -0.03, '-2σ', horizontalalignment='center', fontsize=12)
plt.text(2, -0.03, '+2σ', horizontalalignment='center', fontsize=12)

# Adding the percentage annotations
plt.text(
    0, -0.06, '68%',
    fontsize=12,
    horizontalalignment='center',
    bbox=dict(facecolor='white', alpha=1, edgecolor='none')
)
plt.text(
    0, -0.08, '≈95%',
    fontsize=12,
    horizontalalignment='center', verticalalignment='center',
    bbox=dict(facecolor='white', alpha=1, edgecolor='none'),
    
)

x = np.array([-2, -1, 0, 1, 2])
ymin = [-0.01] * len(x)
ymax = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * x**2)
plt.vlines(
    x = x,
    ymin=ymin,
    ymax=ymax,
    linestyles="--", color="black", alpha=0.5
)

# Adding brackets
plt.vlines(
    x=[-1, 1, -2, 2],
    ymin=[-0.06, -0.06, -0.08, -0.08],
    ymax=[-0.04, -0.04, -0.04, -0.04],
    linestyles='-', color='black'
)
plt.hlines(
    y=[-0.06, -0.08],
    xmin=[-1, -2],
    xmax=[1, 2],
    linestyles='-', color='black'
)

plt.xticks([])
plt.yticks([])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Setting labels
plt.xlabel('')
plt.ylabel('Probability')
plt.title('')
plt.ylim(-0.1, 0.4)
plt.xlim(-3.2, 3.2)

# Show the plot
plt.savefig('figureF.png', transparent=True)
plt.show()
