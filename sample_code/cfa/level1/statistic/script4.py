import matplotlib.pyplot as plt

# Data from the image
intervals = ['−30% to −20%', '−20% to −10%', '−10% to 0%', '0% to 10%', '10% to 20%', '20% to 30%', '30% to 40%', '40% to 50%']
relative_frequencies = [0.05, 0.10, 0.15, 0.35, 0.15, 0.10, 0.05, 0.05]

# Midpoints of each interval
midpoints = [-25, -15, -5, 5, 15, 25, 35, 45]

# Add zero points to the start and end of midpoints and frequencies
extended_midpoints = [-35] + midpoints + [55]
extended_frequencies = [0] + relative_frequencies + [0]

# Create the frequency polygon with the extended points
plt.figure(figsize=(12, 8))
plt.plot(extended_midpoints, extended_frequencies, marker='', linestyle='-', color='dodgerblue')

# Add titles and labels
plt.xlabel('Interval Midpoints', color='dodgerblue', fontweight='bold')
plt.ylabel('Frequency', color='dodgerblue', fontweight='bold')

# Set x-ticks without the last point (55)
plt.xticks(extended_midpoints[1:-1], labels=['−25', '−15', '−5', '5', '15', '25', '35', '45'])

# Convert y-axis labels to percentages
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

# Set y-axis limit to start at 0
plt.ylim(0, max(extended_frequencies) * 1.1)
plt.xlim(-35, 55)

# Adjust layout to make sure everything fits
plt.tight_layout()

# Save and display the plot
plt.savefig('figure4.png')
plt.show()