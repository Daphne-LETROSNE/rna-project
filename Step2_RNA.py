import os
import matplotlib.pyplot as plt

#we were supposed to do it without using libraries, but i had to use the plt function of matpplotlib


# Function to read values from a file and return them as a list of floats
def read_values_from_file(file_path):
    # Open the file and read each line, converting each line to a float and stripping whitespace
    with open(file_path, 'r') as file:
        return [float(line.strip()) for line in file]

# Function to plot XY scores from a file
def plot_xy_scores(file_name):
    # X-axis values from 0.5 to 19.5 with a step of 1
    x_values = [i + 0.5 for i in range(20)]

    # Extract the code from the file name as the is format: "NucNuc_scores.txt")    
    code = file_name.split('_')[0]
    
    # Read Y-axis values from the file
    file_path = os.path.join(file_name)  # Adjust the path to your file directory
    y_values = read_values_from_file(file_path)
    
    # Plot the data
    plt.plot(x_values, y_values)

    # Set labels and title
    plt.xlabel('distance')
    plt.ylabel('score')
    plt.title(f'{code} scores')

    # Save the plot as a PNG image with a file name containing the XY value
    plot_filename = f'{code}_Scores_Plot.png'
    plt.savefig(plot_filename)

    # Show the plot
    plt.show()


# Get a list of all files in the current directory
all_files = os.listdir()

# Filter the files to only include those ending with "_scores.txt"
score_files = [file for file in all_files if file.endswith("_scores.txt")]

# Print the names of the files ending with "_scores.txt"
for file in score_files:
    print(file)


# Iterate over each file and plot its XY scores
for file in score_files:
    plot_xy_scores(file)
