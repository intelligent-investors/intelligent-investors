import matplotlib.pyplot as plt
import numpy as np

# Generate data for the normal distribution
x = np.linspace(-3, 3, 1000)
y = (1 / (np.sqrt(2 * np.pi))) * np.exp(-0.5 * x**2)

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y)

# Add lines for mean, median, and mode
mean = median = mode = 0
plt.axvline(mean, color='black', linestyle='--')

# Add text for mean, median, and mode
plt.text(mean, -0.07, 'Mean\nMedian\nMode', horizontalalignment='center')

# Remove the axes
plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# Remove the x-axis label
plt.gca().axes.get_xaxis().set_visible(False)

# Display the plot
plt.savefig('figure6_1.png', transparent=True)
plt.show()