import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(2, 12, 100)
y = np.ones_like(x) * 0.5

# Create the plot
plt.plot(x, y, label='CDF = 0.5')

# Fill the area between x=4 and x=8
plt.fill_between(x, 0, y, where=(x >= 4) & (x <= 8), alpha=0.5)

# Add labels and title
plt.ylabel('Probability')
plt.xlabel('')
plt.xlim(0, 14)
plt.ylim(0, 0.8)
plt.xticks([2, 4, 6, 8, 10, 12])
plt.yticks([])
plt.vlines(x=2, ymin=0, ymax=0.5, linestyle='-')
plt.vlines(x=12, ymin=0, ymax=0.5, linestyle='-')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(True)
plt.gca().spines['bottom'].set_visible(True)

# Display the plot
plt.savefig('figureC.png', transparent=True)
plt.show()