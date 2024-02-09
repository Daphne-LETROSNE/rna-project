import os

base_pairs = ['AA', 'AU', 'AC', 'AG', 'UU', 'UC', 'UG', 'CC', 'CG', 'GG']
x_values = [i + 0.5 for i in range(20)]

def parse_pdb_file(file_path):
    coordinates = []
    with open(file_path, 'r') as pdb_file:
        for line in pdb_file:
            if line.startswith('ATOM') and 'C3\'' in line:
                columns = line.split()
                atome = columns[3]

                x = float(line[30:38].strip())
                y = float(line[38:46].strip())
                z = float(line[46:54].strip())
                coordinates.append((atome,(x, y, z)))
    return coordinates

def compute_euclidian_distance(atom1, atom2):
    # Calculate the Euclidean distance using the formula: sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
    return ((atom1[0] - atom2[0])**2 + (atom1[1] - atom2[1])**2 + (atom1[2] - atom2[2])**2)**0.5


def compute_interatomic_distances(coordinates, base_pairs):
    distances = []
    for i in range(len(coordinates)):
        for j in range(i + 4, len(coordinates), 1):
            distance = compute_euclidian_distance(coordinates[i][1], coordinates[j][1])
            if coordinates[i][0] + coordinates[j][0] in base_pairs:
                code = coordinates[i][0] + coordinates[j][0]
            else:
                code = coordinates[j][0] + coordinates[i][0]
            distances.append((code, distance))
    return distances

# Function to read values from a file and return them as a list of floats
def read_values_from_file(file_path):
    # Open the file and read each line, converting each line to a float and stripping whitespace
    with open(file_path, 'r') as file:
        values = []
        for line in file:
            values.append(float(line.strip()))
        return values


def create_values_dic(files_list, base_pairs):
    # Initialize an empty dictionary to store values for each base pair
    values_dic = {}
    # Iterate over each base pair and corresponding file
    for base_pair, file_name in zip(base_pairs, files_list):
        # Construct the file path by appending the base pair to "_scores.txt"
        file_path = f"{base_pair}_scores.txt"
        # Read Y-axis values from the file using the read_values_from_file function
        y_values = read_values_from_file(file_name)
        # Update the dictionary with the base pair as the key and corresponding Y-axis values
        values_dic[base_pair] = y_values
    # Return the populated values dictionary
    return values_dic

# Function to interpolate scores based on distances
def interpolate(distances, values_dic, x_values):
    # Initialize dictionary to store scores for each key
    scores = {}
    # Group distances by key
    distances_dict = {}
    for key, value in distances:
        distances_dict.setdefault(key, []).append(value)

    # Interpolate scores based on distances
    for key, value in distances_dict.items():
        try:
            scores[key] = [interpolate_single(d, values_dic[key], x_values) for d in value]
        except KeyError:
            # Handle the case where a key is not found in the values dictionary
            print("this is a key")

    return scores


# Function to interpolate a single score based on distances
def interpolate_single(distance, y_values, x_values):
    if distance < 0.5 or distance > 19.5:
        return 0
    idx = int(distance - 0.5)
    frac = distance - int(distance)
    return (1 - frac) * y_values[idx] + frac * y_values[idx + 1]

pdb_files = ['1c2x.pdb']  # replace with the PDB files of interest
    
files_list=[file for file in os.listdir() if file.endswith("_scores.txt")]
values_dic=create_values_dic(files_list, base_pairs)
    
for pdb_file in pdb_files:
    coordinates = parse_pdb_file(pdb_file)
    distances=compute_interatomic_distances(coordinates,base_pairs)
    scores=interpolate(distances,values_dic,x_values)
       

scores

total_sum = 0
for arr in scores.values():
    total_sum += sum(arr)

print(f"The sum of all these score is: {total_sum}")
