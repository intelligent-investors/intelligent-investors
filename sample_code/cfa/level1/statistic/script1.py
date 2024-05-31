import matplotlib.pyplot as plt

# Data from the image
intervals = ['−30% to −20%', '−20% to −10%', '−10% to 0%', '0% to 10%', '10% to 20%', '20% to 30%', '30% to 40%', '40% to 50%']
relative_frequencies = [0.05, 0.10, 0.15, 0.35, 0.15, 0.10, 0.05, 0.05]

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(intervals, relative_frequencies, color='dodgerblue', width=1.0)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0%}'.format(y)))

# Add titles and labels
plt.title('(a) Relative Frequencies')
plt.xlabel('Intervals')
plt.ylabel('Relative Frequency')

plt.xticks(rotation=20, ha='right')

# Show the plot
plt.savefig('figure1.png')
plt.show()