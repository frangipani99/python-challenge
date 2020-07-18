import os
import csv

#store filepath of budget data source data
electiondata_csv = r"/Users/carawilliams/Repository/python-challenge/PyPoll/Resources/election_data.csv"

with open(electiondata_csv) as electiondata_file:
    csvreader=csv.reader(electiondata_file)

    #skip first row which is data header
    csvheader=next(csvreader)

    
    #define "candidates" variable as list
    candidates = []

    #iterate through rows of data and add Column C to "candidates" list
    for row in csvreader:
       
        #load each row in date column to "date" list
        candidates.append(row[2])
    
    #print total number of votes
    print (
            "Election Results"
            + "\n-------------------------" 
            + "\nTotal Votes: " + str(len(candidates))
            + "\n-------------------------" 
            )   
# define "unique candidates" variable as list
    unique_candidates_list = []
    total_votes = {}
 
 # iterate through "candidates" list and pull unique names into "unique_candidates_list" list and print results
    for name in candidates:
        if name not in unique_candidates_list:
            unique_candidates_list.append(name)


    # iterate through "candidates" list and count each time a vota is cast for a candidate and put in dictionary called "total votes"
    for name in unique_candidates_list:
        total_votes[name] = candidates.count(name)

#create a dictionary named "percent votes" to hold the percent of votes each candidate received
percent_votes = {}

#loop through total votes dictionary and take total votes for each candidate and divide by the total votes - round to 2 decimal points
for name in total_votes:
    percent_votes [name] = round((total_votes [name] / len(candidates) * 100),2)


#create a dictionary named "final result" to hold the percent of votes each candidate received
total_votes[name].update(percent_votes[name])

print (total_votes)