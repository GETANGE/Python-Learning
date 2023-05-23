import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Apples', 'Oranges', 'Bananas', 'Grapes']
sizes = [30, 25, 15, 10]
colors = ['red', 'orange', 'yellow', 'purple']
explode = (0.1, 0, 0, 0)  # explode the first slice

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Aspect ratio to make the pie circular
plt.axis('equal')

# Add a title
plt.title('Fruit Distribution')

# Display the chart
plt.show()
