The process is composed in 3 steps, corresponding to 3 scripts:

All process should be run in the script directory : 

## First process 

Related script : Step1_RNA.py

This script performs several tasks related to analyzing RNA structures. 

**Functionalities of the script:**

**Parsing PDB files:** The script reads PDB files and extracts relevant atom coordinates for 'C3\'' atoms of nucleotides.

**Computing interatomic distances:** It calculates the distances between atoms in the RNA structure based on the extracted coordinates.

**Processing distances:** The distances are rounded to the nearest integer for further analysis.

**Computing reference frequencies:** Frequencies of distances between 1 and 20 are computed to establish a reference distribution.

**Calculating observed frequencies:** Frequencies of distances between nucleotide pairs (base pairs) are calculated.

**Computing log ratios:** Logarithmic ratios between observed and reference frequencies are computed.

**Writing scores to files:** The computed scores are written to files for each base pair interaction.

### Inputs
- PDB files: These are files containing the structure information of RNA molecules.
- Base pairs: A list of base pair interactions (e.g., 'AA', 'AU', etc.).

Notes: If you want to try to train it with a another file, you should change the line 141 :  pdb_files = ['1c2x.pdb'], and replace '1c2x.pdb' by the file of interest. 

### Outputs
- Score files: Each base pair interaction has a corresponding file ('AA_scores.txt', 'AU_scores.txt', etc.) containing computed scores.
  



## Second process 

Related script : Step2_RNA.py

**Inputs:**
- **Score files**: These are files containing score values for different base pair interactions (e.g., AA_scores.txt, AU_scores.txt, etc.).

**Outputs:**
- **Plots**: For each score file, an XY plot is generated showing the relationship between distance and score. The plot is saved as a PNG image file with a filename indicating the base pair interaction (e.g., 'AA_Scores_Plot.png').



### Functionalities of the script:

**Reading score files:** The script reads the score values from each file ending with "_scores.txt" in the current directory.

**Plotting XY scores:** For each score file, the script extracts the code (base pair interaction) from the filename and reads the Y-axis values from the file. It then plots the XY scores using matplotlib, with distances on the X-axis and scores on the Y-axis. 

**Saving plots:** Each plot is saved as a PNG image file with a filename indicating the base pair interaction.

**Displaying plots:** The script displays each plot in the console.

The script provides a visual representation of the scores associated with different base pair interactions, allowing for easy comparison and analysis.

## Third process

Related script : Step3_RNA.py

### Inputs

- **PDB files**: These are files containing the coordinates of atoms in a 3D structure of an RNA molecule.

- **Score files**: These are files containing scores associated with different base pair interactions (e.g., AA_scores.txt, AU_scores.txt, etc.).

### Output 

- **scores**: A dictionary where each key represents a base pair interaction (e.g., 'AA', 'AU', etc.), and the corresponding value is a list of interpolated scores based on the interatomic distances for that base pair.

- **total_sum**: The sum of all interpolated scores across all base pair interactions, which represents the estimated Gibbs free energy of the RNA conformation.



### Functionalities of the script

**Parsing PDB files:** 
The script reads the coordinates of atoms from a PDB file, focusing on atoms labeled as 'C3''.

**Computing interatomic distances:** 
It computes the distances between atoms in the RNA structure, considering only atoms from different residues separated by at least 4 positions.

**Reading score files:** 
The script reads score values from separate files corresponding to different base pair interactions.

**Interpolating scores:** 
Using linear interpolation, it assigns scores to the distances between atoms based on the provided score values.

**Summing scores:** 
Finally, it calculates the total sum of all interpolated scores, which represents the estimated Gibbs free energy of the RNA conformation.

The script then prints out the total sum of scores as the estimated Gibbs free energy.



Have  fun !! ;)