# Author - Sandeep Dulam
# submission date : 15-11-2024
# python code for calculating day to day expenses which are present in CSV file
# pre-requisite: need to have a CSV file which has expenses and amount.
# output will be saved in ".txt" file and ".png" file.


#importing external libraries 
import csv
from collections import defaultdict
import os
import matplotlib.pyplot as plt


# Read expenses from a CSV file and return as a list of dictionaries
def read_expenses(file_path):
    
    expenses = []
    # checking the file exists or not
    if not os.path.isfile(file_path):  
        print(f"The file '{file_path}' does not exist.")
        return expenses

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # converting Amount to float for handling few errors
                try:
                    amount = float(row['Amount'])  
                    row['Amount'] = amount 
                    expenses.append(row)
                except ValueError:
                    print(f"Skipping invalid row: {row} (invalid Amount value)")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    return expenses


#function to calculate total expenses and categorize by category
def calculate_summary(expenses):
    total_expense = 0
    category_expenses = defaultdict(float)

    for expense in expenses:
        amount = expense['Amount']
        category = expense['Category']
        total_expense += amount
        category_expenses[category] += amount

    return total_expense, category_expenses


# function for saving output summary to text file
def print_summary_to_file(total_expense, category_expenses, file_path):
    with open(file_path, 'w') as file:
        file.write(f"Total Expenses: ${total_expense:.2f}\n")
        file.write("Expenses by Category:\n")
        for category, amount in category_expenses.items():
            file.write(f"{category}: ${amount:.2f}\n")
    print(f"Summary saved to {file_path}")

# function for plotting the expenses in category
def plot_expenses_to_file(category_expenses, image_path):
    categories = list(category_expenses.keys())
    amounts = list(category_expenses.values())

    # Creating a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, amounts, color='red')
    plt.xlabel('Category')
    plt.ylabel('Amount ($)')
    plt.title('Expenses by Category')
    # Rotate category labels for better readability
    plt.xticks(rotation=45, ha='right')  
    # Adjust layout to prevent clipping of labels
    plt.tight_layout()  

    # Save the plot as an image file
    plt.savefig(image_path)  
    #plt.close()  
    print(f"Graph saved to {image_path}")

# path to the CSV file
file_path = r'D:\Scripting\New folder\expenses.csv' 
expenses = read_expenses(file_path)


# condition to print summary if expenses are read successfully
if expenses: 
    total_expense, category_expenses = calculate_summary(expenses)
    
    # Saving the summary to a text file
    summary_file_path = r'D:\Scripting\New folder\expenses_summary.txt'
    print_summary_to_file(total_expense, category_expenses, summary_file_path)
    
    # Saving the chart to an image file
    graph_image_path = r'D:\Scripting\New folder\expenses_graph.png'
    plot_expenses_to_file(category_expenses, graph_image_path)
else:
    print("No valid expenses data found.")
