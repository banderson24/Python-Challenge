#Import os and csv modules
import os
import csv

# Navigate to location of csv
budget_csv = os.path.join("..", "..", "Starter_Code 3", "PyBank", "Resources", 
                          "budget_data.csv")

# Set the output path
output_path = os.path.join("analysis", "Financial Analysis.txt")

#Create a list to store the changes for the average change calculation
changes = []

# Open and read the CSV
with open(budget_csv, 'r') as csv_file:
    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header row
    header = next(csv_reader)

    #Set a variable to calculate total months  
    total_months = 0
    #Set a variable to calculatetotal profit/loss
    total = 0
    # Set a variable to store the previous month's profit/loss
    prev_month_profit_loss = 0

   

    for row in csv_reader:
        # Adding 1 for each row since each row is its own month
        total_months += 1
        # Adding up the value for each row within the 2nd column
        total += int(row[1])

        # Assuming there is a change each month this performs the calculation to get the change
        if prev_month_profit_loss != 0:
            # Calculate the change and add it to the changes list
            change = int(row[1]) - prev_month_profit_loss
            changes.append(change)  

            #Calculate the greatest increase in profits
            greatest_increase = max(changes)

            # Calculate the greatest decrease in profits
            greatest_decrease = min(changes) 

            if change == greatest_increase:
                    greatest_increase_month = row[0]
            elif change == greatest_decrease:
                    greatest_decrease_month = row[0]

        # Update the previous month's profit/loss for the next iteration
        prev_month_profit_loss = int(row[1])


# Calculate the average outside the loop so it can go through the entire loop
average_change = round(sum(changes) / len(changes), 2)

#Calculate the greatest increase in profits
greatest_increase = max(changes)

# Calculate the greatest decrease in profits
greatest_decrease = min(changes)

print("Financial Analysis")

print("------------------------------")

#Print the desired results
print("Total Months: " + str(total_months))
print("Total: $" + str(total))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")


# Create and open a text file in write mode
with open(output_path, 'w') as output_file:
    # Write the desired results to the text file
    print("Financial Analysis", file=output_file)
    print("------------------------------", file=output_file)
    print("Total Months: " + str(total_months), file=output_file)
    print("Total: $" + str(total), file=output_file)
    print("Average Change: $" + str(average_change), file=output_file)
    print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")", file=output_file)
    print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")", file=output_file)