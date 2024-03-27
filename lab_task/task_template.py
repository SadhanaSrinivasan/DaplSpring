import numpy as np

# Hint: To visualize the data, you can import matplotlib.pyplot as plt

# Step 1: Load the CSV file using numpy
# HINT: Use np.loadtxt, specifying the path to your CSV, delimiter, and skiprows to ignore the header

data = np.loadtxt('/Users/sadhanasrinivasan/Desktop/Dartmouth/spring 24/DAPL24/DaplSpring/lab_task/simulated_temperatures.csv', delimiter=',', skiprows=1)

# Extract the days and temperatures from the loaded data
days = data[:, 0]
temperatures = data[:, 1]

# Step 2: Calculate the mean and standard deviation of the temperatures
# HINT: Use np.mean and np.std functions

mean_temperature = np.mean(temperatures)
std_temperature = np.std(temperatures)

# Step 3: Identify the hottest and coldest days
# HINT: Use the mean and standard deviation to calculate thresholds for hot and cold days.
# Hot days could be defined as days with temperatures more than 2 standard deviations above the mean
# Cold days could be defined as days with temperatures more than 2 standard deviations below the mean

hot_threshold = mean_temperature + 2 * std_temperature
cold_threshold = mean_temperature - 2 * std_temperature

# Find the days that are hotter than the hot_threshold and colder than the cold_threshold
# HINT: Use boolean indexing with days and temperatures arrays

hot_days = days[temperatures > hot_threshold]
cold_days = days[temperatures < cold_threshold]

# Step 4 (Optional): Visualize the data using matplotlib
# Plot the temperatures across days and mark the hot and cold days using different colors or markers
# HINT: Use plt.plot for the temperatures, plt.scatter for marking hot and cold days

# YOUR CODE HERE for visualization
#plt.plot(temperatures)
#plt.scatter()
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Plot temperatures across days
plt.plot(days, temperatures, label='Temperatures', color='blue')

# Mark hot days
plt.scatter(hot_days, temperatures[temperatures > hot_threshold], color='red', label='Hot Days')

# Mark cold days
plt.scatter(cold_days, temperatures[temperatures < cold_threshold], color='cyan', label='Cold Days')

# Add labels and legend
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature Variation')
plt.legend()

# Show plot
plt.grid(True)
plt.show()

# Step 5: Write a summary of your findings
# Create a string variable `summary` that includes the mean temperature, standard deviation,
# and lists of hot and cold days.

summary = f"""
Mean Temperature: {mean_temperature:.2f}C
Standard Deviation: {std_temperature:.2f}C
Hottest Days: {hot_days}
Coldest Days: {cold_days}
"""

# Print the summary
print(summary)