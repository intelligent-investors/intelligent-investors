import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Degrees of freedom
dfs = [1, 4, 15]

# x values
x = np.linspace(-5, 5, 1000)

# Plot t-distributions for different degrees of freedom
plt.figure(figsize=(10, 6))

for df in dfs:
    y = stats.t.pdf(x, df)
    plt.plot(x, y, label=f'df = {df}')

# Add labels and legend
# plt.xlabel('x')
# plt.ylabel('')
plt.title('t-Distributions for Different Degrees of Freedom (df)')
plt.axvline(0, color='gray', linestyle='--')
plt.legend()
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(True)
plt.xticks([0], ['0'])
plt.yticks([])
# Show plot
plt.grid(False)
plt.savefig('figureA.png', transparent=True)
plt.show()