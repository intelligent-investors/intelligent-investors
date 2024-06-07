import matplotlib.pyplot as plt
import numpy as np

# Data for plots
np.random.seed(0)
N = 60
x = np.random.rand(N) * 10
y1 = np.random.rand(N) * 10
y2 = 1.5 * x + np.random.normal(0, 1, N)
y3 = np.sin(x)

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Scatterplot 1: No relationship
axs[0, 0].scatter(x, y1)
axs[0, 0].scatter(9.2, 8.5, color='red')
axs[0, 0].set_title('a) No relationship')
axs[0, 0].set_xlim(0, 10)
axs[0, 0].set_ylim(0, 10)
axs[0, 0].grid(True)

# Scatterplot 2: Strong linear relationship
axs[0, 1].scatter(x, y2)
axs[0, 1].set_title('b) Strong linear relationship')
axs[0, 1].set_xlim(0, 10)
axs[0, 1].set_ylim(0, 12)
axs[0, 1].grid(True)

# Scatterplot 3: Non-linear relationship
axs[1, 0].scatter(x, y3)
axs[1, 0].set_title('c) Non-linear relationship')
axs[1, 0].set_xlim(0, 10)
axs[1, 0].set_ylim(-1.5, 1.5)
axs[1, 0].grid(True)

# Hide empty subplot
fig.delaxes(axs[1, 1])

# Adjust layout
fig.suptitle('Figure: Scatterplots')
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Manually set position for axs[1, 0] to center it
pos1 = axs[1, 0].get_position()
l, b, w, h = pos1.bounds
axs[1, 0].set_position([l+0.25, b, w, h])

plt.savefig('figureA.png', transparent=True)
plt.show()
