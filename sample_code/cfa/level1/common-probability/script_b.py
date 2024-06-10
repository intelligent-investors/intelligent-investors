import matplotlib.pyplot as plt
import numpy as np

# Data for the step function
x = [0, 2, 4, 6, 8, 10, 12]
y = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.0]

# Create the step plot
plt.step(x, y, where='post')

# Add labels and title
plt.xlabel('x')
plt.ylabel('Prob(X ≤ x)')
plt.ylim(0, 1.03)
plt.xlim(0, 13)
plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
default_color = plt.rcParams['axes.prop_cycle'].by_key()['color'][0]
print(default_color)
plt.annotate(
    '',
    xy=(12.1, 1), xytext=(10, 1),
    arrowprops=dict(arrowstyle='->', lw=1, color=default_color),
)

plt.annotate(
    '',
    xy=(2, 0), xytext=(0, 0),
    arrowprops=dict(arrowstyle='-', lw=1.5, color=default_color),
)


plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(True)
plt.gca().spines['bottom'].set_visible(True)

# Show the plot
plt.tight_layout()
plt.savefig('figureB.png', transparent=True)
plt.show()