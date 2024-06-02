import numpy as np
import matplotlib.pyplot as plt

# Given data
data = [8, 10, 12, 13, 15, 17, 17, 18, 19, 23]

# Calculate the third quartile
Q3 = 18.25

# Calculate the median
median = np.median(data)

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(range(1, len(data) + 1), data, color='blue', label='Data Points')
plt.axvline(8.25, color='r', linestyle='--', label=f'Position of Q3')
plt.title('Data Points of Returns Distribution')
plt.xlabel('Index')
plt.ylabel('Returns (%)')
plt.xticks(range(1, len(data) + 1))
plt.legend()
plt.grid(True)
plt.savefig('figure5.png')
plt.show()
