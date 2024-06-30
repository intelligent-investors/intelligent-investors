import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Define the range for x values
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Normal Distribution')
plt.fill_between(x, -0.01, y, where=(x <= -1.96), color='skyblue')
plt.fill_between(x, -0.01, y, where=(x >= 1.96), color='skyblue')

# Annotate the regions
plt.text(-3, -0.1, 'Reject $H_0$', horizontalalignment='center', color='blue')
plt.text(3, -0.1, 'Reject $H_0$', horizontalalignment='center', color='blue')
plt.text(0, -0.1, 'Fail to Reject $H_0$', horizontalalignment='center')
plt.annotate(
    '2.5%',
    xy=(-2.2, 0.0001),
    xytext=(-3, 0.05),
    arrowprops=dict(arrowstyle='->',lw=1, color='black'),
    color='blue'
)
plt.annotate(
    '2.5%',
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
plt.xticks([-1.96, 1.96])

plt.hlines(xmin=-4, xmax=4, y=-0.05, color='black', linestyle='-', linewidth=1)
plt.vlines(x=-1.96, ymin=[-0.04], ymax=[-0.15], color='black', linestyle='-', linewidth=1)
plt.vlines(x=1.96, ymin=[-0.04], ymax=[-0.15], color='black', linestyle='-', linewidth=1)
plt.vlines(x=-1.96, ymin=[-0.01], ymax=[0.06], color='black', linestyle='-', linewidth=1)
plt.vlines(x=1.96, ymin=[-0.01], ymax=[0.06], color='black', linestyle='-', linewidth=1)

# Show the plot
plt.grid(False)
plt.savefig('figureA.png', transparent=True)
plt.show()