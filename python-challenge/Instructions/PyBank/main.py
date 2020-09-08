# main.py

import os
import csv

# Initializing file paths.
csv_file_path = os.path.join("Resources", "budget_data.csv")
analysis_file_path = os.path.join("analysis", "analysis.txt")

# Open and read csv.
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header.
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Extract data.
    total_num_of_months = 0
    months = list()
    profits_and_loses = list()

    for row in csv_reader:
      total_num_of_months += 1
      profits_and_loses.append(float(row[1]))
      months.append(row[0])

    # Calculations.
    total_profits_and_loses = sum(profits_and_loses)
    average = total_profits_and_loses / total_num_of_months
    greatest_increase = max(profits_and_loses)
    greatest_decrease = abs(min(profits_and_loses))

    # Formatted output string.
    output = f'''
Financial Analysis
----------------------------
Total Months: {total_num_of_months}
Total: ${total_profits_and_loses}
Average Change: ${average}
Greatest Increase in Profits: {months[profits_and_loses.index(greatest_increase)]} (${greatest_increase})
Greatest Decrease in Profits: {months[profits_and_loses.index(-greatest_decrease)]} (${greatest_decrease})
'''
    # Open, write and close output file.
    analysis_file = open(analysis_file_path, "a")
    analysis_file.write(output)
    analysis_file.close()
