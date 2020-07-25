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

    #define "date" and "profit_loss" variables as lists
    date = []
    profit_loss = []
    change_profit_loss = []

    #iterate through rows of data and add Column A to "data" list and Column B to "profit_loss" list
    for row in csvreader:
       
        #load each row in date column to "date" list
        date.append(row[0])
        
        #load each row in "profit_loss" column to "profit_loss" list
        profit_loss.append(int(row[1]))

        #for each row add profit_loss value to total_profit_loss to determine sum of column
        total_profit_loss = total_profit_loss + int(row[1])

    #print "Total Months" and "Total Profit/loss" to terminal
    print (
            "Financial Analysis"
            + "\n----------------------------" 
            + "\nTotal Months: " + str(len(date))
            + "\nTotal: $" + str(total_profit_loss)
            )   
    
    # iterate through "profit/loss list" to calculate average change in profit/loss
    for value in range (1, len(profit_loss)):
        
        #store result in "change_profit_loss variable"
        change_profit_loss.append(int(profit_loss[value]) - int(profit_loss[value-1]))

    #calulate average "Change in Profit Loss"
    def average(change_profit_loss):
        averagechange_profit_loss = sum(change_profit_loss)/len(change_profit_loss)

        return round((averagechange_profit_loss),2)

    #remove first value from "Date" to align with "Change Profit/Loss list" list
    date.pop(0)

    #create a dictionary with "Date" and Average Change in Profit/loss" list   
    change_profitloss_dict = dict(zip(date,change_profit_loss))

    #print "Average Change, Greatest Change, and Greatest Decrease in Profit/Loss, " 
    print ("Average  Change: $" + str(average(change_profit_loss)))
    print (
            "Greatest Increase in Profits: " 
            #print key in dictionary that matches "Greatest Increase"
            + max(change_profitloss_dict, key=change_profitloss_dict.get)
            + " "
            + str(max(change_profit_loss))
            )
    print (
            "Greatest Decrease in Profits: " 
            #print key in dictionary that matches "Greatest Decrease"
            + min(change_profitloss_dict, key=change_profitloss_dict.get)
            + " "
            + str(min(change_profit_loss))
            )
# Write results to text file
file = open('analysis\PyBank Results.txt', 'w')
file.write ("Financial Analysis"
            + "\n----------------------------" 
            + "\nTotal Months: " + str(len(date))
            + "\nTotal: $" + str(total_profit_loss)
            + "\nAverage  Change: $" + str(average(change_profit_loss))
            + "\nGreatest Increase in Profits: " 
            + max(change_profitloss_dict, key=change_profitloss_dict.get)
            + " "
            + str(max(change_profit_loss))
            + "\nGreatest Decrease in Profits: " 
            + min(change_profitloss_dict, key=change_profitloss_dict.get)
            + " "
            + str(min(change_profit_loss)))
file.close()