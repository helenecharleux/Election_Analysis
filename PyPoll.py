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

# Initialize a total_votes counter
total_votes = 0

# Declare a list to store candidates'name (create first an empty list)
candidate_options = []

# Declare a dictionary to store the votes for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# With statement analysis to open the "election_results"
with open(file_to_load) as election_data :

    # Read the file.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)

 # Print each row in the CSV file and print the candidates'name for each row
    for row in file_reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        
        # If candidate_name is not in the candidate_options list, add the name to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Count the votes for each candidate_name
        candidate_votes[candidate_name]+=1
        
# Print the candidates'option list
print(candidate_options)

# Determine the percentage of votes for each candidate by looping through the counts.
for candidate_name in candidate_votes :
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100

# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
     # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage

     # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)