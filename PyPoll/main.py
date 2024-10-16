# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = [] # List of candidates
candidatevotes = {} # Dictionary to track votes per candidate
winning_candidate = "" # Variable to track the winning candidate
winning_count = 0 # Track the highest vote count
winning_percentage = 0 # Track the highest vote percentage

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidatevotes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidatevotes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    electionresults = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes}\n"
        f"-------------------------\n"
    )

    print(electionresults, end="") # Print a loading indicator (for large datasets)
    txt_file.write(electionresults)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidatevotes:

        # Get the vote count and calculate the percentage
        votes = candidatevotes[candidate]
        vote_percentage = (votes/total_votes)*100

        # Update the winning candidate if this one has more votes
        if votes> winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        # Print and save each candidate's vote count and percentage

        candidateresults = f"{candidate}:{vote_percentage:.3f}% ({votes})\n"
        print (candidateresults, end="")
        txt_file.write(candidateresults)
        
    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n" 
    )
    print(winning_candidate_summary)
    # Save the winning candidate summary to the text file
    
    
    txt_file.write(winning_candidate_summary)








