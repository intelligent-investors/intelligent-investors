import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([0, 2, 4, 7, 12])
y = np.array([0, 0, 0.2, 0.5, 1.0])

# Plot
plt.plot(x, y, marker='o', linewidth=2)
default_color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0]
plt.annotate(
    '',
    xy=(2, 0), xytext=(0, 0),
    arrowprops=dict(arrowstyle='-', lw=2, color=default_color),
)
plt.hlines(y=1.0, xmin=0, xmax=12, color='black', linestyle='--')
plt.hlines(y=0.5, xmin=0, xmax=7, color='black', linestyle='--')
plt.hlines(y=0.2, xmin=0, xmax=4, color='black', linestyle='--')
plt.vlines(x=4, ymin=0, ymax=0.2, color='black', linestyle='--')
plt.vlines(x=7, ymin=0, ymax=0.5, color='black', linestyle='--')
plt.vlines(x=12, ymin=0, ymax=1, color='black', linestyle='--')

plt.xticks([2, 4, 6, 8, 10, 12])
plt.yticks([0.2, 0.5, 1.0])
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(True)
plt.gca().spines['bottom'].set_visible(True)


# Arrows
plt.arrow(12, 1.0, 1, 0, head_width=0.03, head_length=0.5)

# Axes
plt.xlim(0, 14)
plt.ylim(0, 1.1)

# Labels
plt.xlabel('')
plt.ylabel('')

# Show plot
plt.savefig('figureD.png', transparent=True)
plt.show()
