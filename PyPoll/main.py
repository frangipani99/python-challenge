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


    # iterate through "candidates" list and count each time a vota is cast for a candidate
    for name in unique_candidates_list:
        total_votes[name] = candidates.count(name)

print (total_votes)