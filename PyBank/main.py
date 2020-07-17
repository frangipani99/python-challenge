import os
import csv

#store filepath of budget data source data
budgetdata_csv = r"/Users/carawilliams/Repository/python-challenge/PyBank/Resources/budget_data.csv"

with open(budgetdata_csv) as budgetdata_file:
    csvreader=csv.reader(budgetdata_file)

    #skip first row which is data header
    csvheader=next(csvreader)

    #set initial value of the total_profit_loss variable to 0. this will hold the total sum of profit/loss in the for loop below.
    total_profit_loss = 0
    total_profit_loss = 0

    #define "date" and "profit_loss" variables as lists
    date = []
    profit_loss = []
    change_profit_loss = []

    #iterate through rows of data and add Column A to "data" list and Column B to "profit_loss" list
    for row in csvreader:
       
        #add each row in date column to "date" list
        date.append(row[0])
        
        #add each row in "profit_loss" column to "profit_loss" list
        profit_loss.append(int(row[1]))
 
        #in each loop subtract prior "profit_loss" value from current "profit_loss" value and add result to "change_profit_loss" list
        change_profit_loss.append(int(row[1]) - int(profit_loss[-1]))
        

        #for each row add profit_loss value to total_profit_loss to determine sum of column
        total_profit_loss = total_profit_loss + int(row[1])

    print (str(change_profit_loss))

    def average(change_profit_loss):
        averagechange_profit_loss = sum(change_profit_loss)/len(change_profit_loss)

        return averagechange_profit_loss

#print analysis to terminal
print (
        "Financial Analysis"
        + "\n----------------------------" 
        + "\nTotal Months: " + str(len(date))
        + "\nTotal: $" + str(total_profit_loss)
        + "\nAverage  Change: $" + str(average(change_profit_loss))
        )