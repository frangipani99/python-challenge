import os
import csv

#store filepath of budget data source data
electiondata_csv = r"/Users/carawilliams/Repository/python-challenge/PyPoll/Resources/election_data.csv"

with open(electiondata_csv) as electiondata_file:
    csvreader=csv.reader(electiondata_file)

    #skip first row which is data header
    csvheader=next(csvreader)

    
    #define "date" and "profit_loss" variables as lists
    candidates = []

    #iterate through rows of data and add Column C to "candidate" list
    for row in csvreader:
       
        #load each row in date column to "date" list
        candidate.append(row[2])
        
    #print total number of votes
    print (
            "Election Results"
            + "\n-------------------------" 
            + "\nTotal Votes: " + str(len(candidate))
            # + "\n-------------------------" 
            # + "\nTotal: $" + str(total_profit_loss)
            )   
    
#     # iterate through "profit/loss list" to calculate average change in profit/loss
#     for value in range (1, len(profit_loss)):
        
#         #store result in "change_profit_loss variable"
#         change_profit_loss.append(int(profit_loss[value]) - int(profit_loss[value-1]))

#     #calulate average "Change in Profit Loss"
#     def average(change_profit_loss):
#         averagechange_profit_loss = sum(change_profit_loss)/len(change_profit_loss)

#         return round((averagechange_profit_loss),2)

#     #remove first value from "Date" to align with "Change Profit/Loss list" list
#     date.pop(0)

#     #create a dictionary with "Date" and Average Change in Profit/loss" list   
#     change_profitloss_dict = dict(zip(date,change_profit_loss))

#     #print "Average Change, Greatest Change, and Greatest Decrease in Profit/Loss, " 
#     print ("Average  Change: $" + str(average(change_profit_loss)))
#     print (
#             "Greatest Increase in Profits: " 
#             #print key in dictionary that matches "Greatest Increase"
#             + max(change_profitloss_dict, key=change_profitloss_dict.get)
#             + " "
#             + str(max(change_profit_loss))
#             )
#     print (
#             "Greatest Decrease in Profits: " 
#             #print key in dictionary that matches "Greatest Decrease"
#             + min(change_profitloss_dict, key=change_profitloss_dict.get)
#             + " "
#             + str(min(change_profit_loss))
#             )
# # Write results to text file
# file = open('analysis/PyBank Results.txt', 'w')
# file.write ("Financial Analysis"
#             + "\n----------------------------" 
#             + "\nTotal Months: " + str(len(date))
#             + "\nTotal: $" + str(total_profit_loss)
#             + "\nAverage  Change: $" + str(average(change_profit_loss))
#             + "\nGreatest Increase in Profits: " 
#             + max(change_profitloss_dict, key=change_profitloss_dict.get)
#             + " "
#             + str(max(change_profit_loss))
#             + "\nGreatest Decrease in Profits: " 
#             + min(change_profitloss_dict, key=change_profitloss_dict.get)
#             + " "
#             + str(min(change_profit_loss)))
# file.close()