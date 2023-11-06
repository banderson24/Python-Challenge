#Import os and csv modules
import os
import csv

# Navigate to location of csv
election_csv = os.path.join("..", "..", "Starter_Code 3", "PyPoll", "Resources", 
                          "election_data.csv")

# Set the output path
output_path = os.path.join("analysis", "Election Results.txt")

#Create a list to store the candidates later on in the code
candidates = {}

# Open and read the CSV
with open(election_csv, 'r') as csv_file:
    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header row
    header = next(csv_reader)

    #Set a variable to calculate total votes  
    total_votes = 0

    for row in csv_reader:
        # Adding 1 for each row since each row is its own vote
        total_votes += 1
        # Setting our candidate names so that we can add it to the list
        candidate_name = str(row[2])
        #Add the candidate to the list if it's not in the list
        if candidate_name not in candidates:
            #Add a vote for the first time a candidate is added
            candidates[candidate_name] = 1
        else:
            #Add vote counts for each candidates that is in the dictionary
            candidates[candidate_name] += 1 

#Calculate the winner from our candidates dictionary using the 
winner = max(candidates, key=candidates.get)         

print("Election Results")
print("------------------------------")
#Print the desired results
print("Total Votes: " + str(total_votes))
print("------------------------------")
for candidate, votes in candidates.items():
    print(f'{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})') 
print("------------------------------") 
print("Winner: " + winner)
print("------------------------------")


with open(output_path, 'w') as output_file:
    # Write the desired results to the text file
    print("Election Results", file=output_file)
    print("------------------------------", file=output_file)
    print("Total Votes: " + str(total_votes), file=output_file)
    print("------------------------------", file=output_file)
    for candidate, votes in candidates.items():
        print(f'{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})', file=output_file) 
    print("------------------------------", file=output_file) 
    print("Winner: " + winner, file=output_file)
    print("------------------------------", file=output_file)