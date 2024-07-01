import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Define the range for x values
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normal Distribution')
plt.fill_between(x, -0.01, y, where=(x >= 1.645), color='skyblue')

# Annotate the regions
plt.text(2.6, -0.12, 'Reject $H_0$', horizontalalignment='center', color='blue')
plt.text(0, -0.12, 'Fail to Reject $H_0$', horizontalalignment='center')
plt.annotate(
    '5%',
    xy=(2.2, 0.0001),
    xytext=(2.8, 0.05),
    arrowprops=dict(arrowstyle='->',lw=1, color='black'),
    color='blue'
)
plt.text(0, 0.15, '95%', horizontalalignment='center')

# Remove ticks from y-axis
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['bottom'].set_position(('data', -0.01))
plt.yticks([])
plt.xticks([1.645])

plt.hlines(xmin=-4, xmax=4, y=-0.08, color='black', linestyle='-', linewidth=1)
plt.vlines(x=1.645, ymin=[-0.01], ymax=[0.1], color='black', linestyle='-', linewidth=1)
plt.vlines(x=1.645, ymin=-0.06, ymax=-0.14, color='black', linestyle='-', linewidth=1)
# Show the plot
plt.grid(False)
plt.savefig('figureB.png', transparent=True)
plt.show()