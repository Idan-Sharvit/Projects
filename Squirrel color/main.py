import pandas as pd


# Get a hold in the data csv file.
file = pd.read_csv('Squirrel_Data.csv')

# Get the required column.
# fur_color is now a Series.
fur_color = file['Primary Fur Color']

# Initialize a new list and a dictionary.
colors = []
color_dict = {}

# Traverse through the lines of the Series.
for row in fur_color:
    # Add each color to the color list.
    # Now you should have the next colors in your list: nan, cinnamon, black and gray.
    # They repeat themselves along the list.
    colors.append(row)
# Cast the color list to a set, so you will remove duplicated colors from the list.
colors = set(colors)
# Cast the set back to a list. Now you should have a list without duplicated colors.
colors = list(colors)
# Add a key to the dictionary named 'Fur Color'.
# The value of the key will be the list of colors you found earlier, but without the 'nan' value.
color_dict['Fur Color'] = colors[1:]
# Create a new list to save the counter of each color.
color_counter = []
# Traverse through the colors list while skipping 'nan'.
for color in colors[1:]:
    counter = 0
    # Traverse through the lines of the Series
    for row in fur_color:
        # Count the number of times each color appears in the Series.
        if row == color:
            counter += 1
    # Add the number of times each color appeared in the Series to a list.
    color_counter.append(counter)
# Create new key in the dictionary called 'Counter'.
# The value of the key should be the list of counters for each color.
color_dict['Counter'] = color_counter
# Create new Dataframe using the dictionary we created.
data = pd.DataFrame(color_dict)
# Create new csv file with the Dataframe we created.
data.to_csv('squirrel_count.csv')