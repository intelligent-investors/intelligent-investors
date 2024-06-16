import matplotlib.pyplot as plt

# Data from the image
intervals = ['−30% to −20%', '−20% to −10%', '−10% to 0%', '0% to 10%', '10% to 20%', '20% to 30%', '30% to 40%', '40% to 50%']
relative_frequencies = [0.05, 0.10, 0.15, 0.35, 0.15, 0.10, 0.05, 0.05]

# Calculate cumulative relative frequencies
cumulative_relative_frequencies = [sum(relative_frequencies[:i+1]) for i in range(len(relative_frequencies))]

# Create the cumulative relative frequency bar chart
plt.figure(figsize=(12, 8))
plt.bar(intervals, cumulative_relative_frequencies, color='dodgerblue', width=1.0)

# Add titles and labels
plt.xlabel('Intervals', color='dodgerblue', fontweight='bold')
plt.ylabel('Frequency', color='dodgerblue', fontweight='bold')

# Rotate the x-axis labels diagonally and ensure all text is visible
plt.xticks(rotation=90, ha='right')

# Convert y-axis labels to percentages
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

# Adjust layout to make sure everything fits
plt.tight_layout()


# Show the plot
plt.savefig('figure3.png')
plt.show()
