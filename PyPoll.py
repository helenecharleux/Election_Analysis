# The data we need to retreive 
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. Winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path. 
file_to_save = os.path.join("Analysis", "election_analysis.txt") 

# With statement analysis to open the "election_results"
with open(file_to_load) as election_data :

    # Read the file.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)