# Python-Challenge

# Module 3 Objectives 

# PyBank Objectives

# Your task is to create a Python script that analyzes the records to calculate each of the following values:
      
I started both of these tasks by adding the code we learned in class to import the modules and designate our file path. Then I added the script to read the CSV and skip the header row for our caclulations. Code differs slightly for each challenge because the CSVs were pulled from different locations.

      #Import os and csv modules      
      import os
      import csv

      # Navigate to location of csv      
      budget_csv = os.path.join("..", "..", "Starter_Code 3", "PyBank", "Resources", 
                          "budget_data.csv")

      # Open and read the CSV
      with open(budget_csv, 'r') as csv_file:
          # Split the data on commas
          csv_reader = csv.reader(csv_file, delimiter=",")
          # Skip the header row
          header = next(csv_reader)

#  1. The total number of months included in the dataset

  - The easiest way to calculate this number is to add one for each row using a for loop to iterate through the rows. Since we are skipping the header and every row has a unique month this gives the total number of months in the CSV. 
  - First I had to create the total_months variable and then add 1 to it for row it iterates. 
  - Then within the for loop I added 1 to the total_months.
          
        #Set a variable to calculate total months 
        total_months = 0

        for row in csv_reader:
          # Adding 1 for each row since each row is its own month
          total_months += 1

  - Then we print the total_months variable to get our total months for the answer.

        #Print the desired results
        print("Total Months: " + str(total_months)

  **Code for this portion was taken from lessons in class. Particularly the Student Functions lesson for the +=**
    
#  2. The net total amount of "Profit/Losses" over the entire period

  - This answer was found by using similar functionality as the earlier question and I found this by adding up the profit/loss from each row.
  - First I created created the total variable to calculate the total profilt/loss and set it = to 0
  - Then within the for loop I added the value for each row making sure to specify the proper column to collect the data from
  - Finally, I printed the total results in the correct format.

        #Set a variable to calculatetotal profit/loss
        total = 0

        # Adding up the value for each row within the 2nd column
        total += int(row[1])

        #Print total results in the proper format
        print("Total: $" + str(total))

  **Code for this portion was taken from lessons in class. Again particularly the Student Functions lession for +=**

#  3. The changes in "Profit/Losses" over the entire period, and then the average of those changes

  - The next set of quesions were more difficult. And there are a few different steps to setting this up
  - First I had to create a list to store the changes in profilt/loss for each row
  - Then I had to create a variable to store the previous month's profit/loss and set it = to 0
  - Then I used an if statement to calculate the change by subtracting the row contents from the previous row. The if statement I used was to calculate if there was a change from the previous month.
  - I also used append to add the change to the list I had created
  - I set the previous month's profit/loss before iterating to the next row
  - Finally, outside the loop I calculated the average change and rounded it to 2 decimals
  - Then I printed the results in the desired format

        #Create a list to store the changes for the average change calculation
        changes = []

        # Set a variable to store the previous month's profit/loss
        prev_month_profit_loss = 0

        # Assuming there is a change each month this performs the calculation to get the change
        if prev_month_profit_loss != 0:
            # Calculate the change and add it to the changes list
            change = int(row[1]) - prev_month_profit_loss
            changes.append(change)

        # Update the previous month's profit/loss for the next iteration
        prev_month_profit_loss = int(row[1])

        # Calculate the average outside the loop so it can go through the entire loop
        average_change = round(sum(changes) / len(changes), 2

        print("Average Change: $" + str(average_change))

  **Code for this came from our lessons on lists and how you can add back to lists as well the Student Functions lesson where we performed an average calculation**

  **Outside Resources: I used ChatGPT to check my code here when I ran into errors and it helped me clean things up and create a more efficient manner**

#  4. The greatest increase in profits (date and amount) over the entire period

  - Within my if statement I had already created I set the variables for greatest increase and greatest decrease by using max and min functions to search through my changes list
  - I also created another if statement that set the month of the greatest increase and greatest decrease when I found my max and min change. I would then use this to pull the month into my print statement
  - I then printed the results of the greatest increase and decrease

          #Calculate the greatest increase in profits
          greatest_increase = max(changes)

          # Calculate the greatest decrease in profits
          greatest_decrease = min(changes) 

          if change == greatest_increase:
                greatest_increase_month = row[0]
          elif change == greatest_decrease:
                greatest_decrease_month = row[0]

          print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
          print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")

    **Code for this was mostly taken from lessons we had it in class regarding how to use if statements and how to reference certains columns in the CSV**

    **Outside Resources: I did use ChatGPT to correct some syntax errrors I had made the few times I tried to run this.**


#  5. The greatest decrease in profits (date and amount) over the entire period

      - Code was provided in the previous question above. Should include both greatest increase and greatest decrease explanations


#PyPoll Objectives

# Your task is to create a Python script that analyzes the votes and calculates each of the following values:

# 1. The total number of votes cast

- This is very similar to the first part of the previous activity.
- First I created a variable for the total_votes
- Then within the for loop I added 1 the totals votes
- Then I printed the results

              #Set a variable to calculate total votes  
              total_votes = 0

              for row in csv_reader:
              # Adding 1 for each row since each row is its own vote
              total_votes += 1

              print("Total Votes: " + str(total_votes))

# 2. A complete list of candidates who received votes

- To start this off I created a dictionary to hold each candidates but didn't add anything to it
- Within the for loop I set the candidate_name to be column 2 in the row
- Then I used an if statement to add the candidate_name to the list if the name is not already in the list
- Then I used a for loop to pull the name of each candidate within my dictionary and reference it in the print statement

              #Create a list to store the candidates later on in the code
              candidates = {}

              # Setting our candidate names so that we can add it to the list
              candidate_name = str(row[2])
              #Add the candidate to the list if it's not in the list
              if candidate_name not in candidates:
                    #Add a vote for the first time a candidate is added
                    candidates[candidate_name] = 1
              else:
                    #Add vote counts for each candidates that is in the dictionary
                    candidates[candidate_name] += 1

              for candidate, votes in candidates.items():
                    print(f'{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})') 

**Idea for this was taken from our class session on dictionaries. Struggled a little bit to make this code work so I used ChatGPT to help me get there. ChatGPT helped me come up with the for loop statement to search through the dictionary and pull out the results I needed**

# 3. The percentage of votes each candidate won

- The code I outlined in my answer above gave me most of what I needed to calculate the percentages of each vote per candidate
- In my for loop I rounded the average of the (candidate votes/total votes) and multiple by 100 to get my percentage
- I've listed the unique code for this part of the homework below.

              for candidate, votes in candidates.items():
                      print(f'{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})'

**Idea for this was taken from our class session on dictionaries. Struggled a little bit to make this code work so I used ChatGPT to help me get there. ChatGPT helped me come up with the for loop statement to search through the dictionary and pull out the results I needed**

# 4. The total number of votes each candidate won

- The code I outlined in question #2 provides the code I used to get this calculation
- One other thing to call out here is that in my if statement I added the vote count for the candidates if they were already in the dictionary
- For this one I had to reference my candidate in the for loop and ask for the votes for that candidate

              else:
                    #Add vote counts for each candidates that is in the dictionary
                    candidates[candidate_name] += 1

              for candidate, votes in candidates.items():
                      print(f'{candidate}: {round((votes/total_votes)*100, 3)}% ({votes})'

**Idea for this was taken from our class session on dictionaries. Struggled a little bit to make this code work so I used ChatGPT to help me get there. ChatGPT helped me come up with the for loop statement to search through the dictionary and pull out the results I needed**

# 5. The winner of the election based on popular vote

- I calculated the winner by using the max function to pull the greatest number of votes from the candidates dictionary using
- I then referenced the winner in my print to pull the results

              #Calculate the winner from our candidates dictionary using the 
              winner = max(candidates, key=candidates.get)

**Code for this was taken from Stack Overflow (https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary)**

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

- This was the final part of the exercise to push the results to a new txt file in the analysis folder
- I first needed to set my output path which is what we had learned in class.
- Then I needed to create a 'w' (write) statement to write the ouput to the output path.

              # Set the output path
              output_path = os.path.join("analysis", "Election Results.txt")

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

**Code Resources: I started with the code we learned in class, but that was for CSV files not txt files so I had to do some searching. Found an article on Stack Overflow that gave me some ideas, but I wasn't able to make it work until I threw my code in ChatGPT to get some ideas. ChatGPT gave me the code needed to write to my output path.**
