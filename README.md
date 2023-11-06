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
  - Then within the for loop I added 1 to the total_months for each row.
          
        #Set a variable to calculate total months 
        total_months = 0

        for row in csv_reader:
          # Adding 1 for each row since each row is its own month
          total_months += 1

  - Then we print the total_months variable to get our total months for the answer.

        #Print the desired results
        print("Total Months: " + str(total_months)

  **Code for this portion was taken from lessons in class. Particularly the Student Functions lesson for the +=**
    
#  3. The net total amount of "Profit/Losses" over the entire period

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

#  4. The changes in "Profit/Losses" over the entire period, and then the average of those changes

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

  **Outside Resources: I used chatGTP to check my code here when I ran into errors and it helped me clean things up and create a more efficient manner**

#  6. The greatest increase in profits (date and amount) over the entire period

  - Within my if statement I had already created I set the variables for greatest increase and greatest decrease by using max and min functions to search through my changes list
  - I also created another if statement that set the month of the greatest increase and greatest decrease when I found my max and min change.
  - I then referenced 

  8. The greatest decrease in profits (date and amount) over the entire period
