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
 
 #BUILD A LIST OF UNIQUE CANDIDATE NAMES
 # iterate through "candidates" list and pull unique names into "unique_candidates_list" list and print results
    for name in candidates:
        if name not in unique_candidates_list:
            unique_candidates_list.append(name)

#BUILD A DICTIONARY FOR (UNIQUE CANDIDATE NAME: TOTAL VOTES)
    # iterate through "candidates" list and count each time a vota is cast for a candidate and put in dictionary called "total votes"
    for name in unique_candidates_list:
        total_votes[name] = candidates.count(name)

#BUILD A DICTIONARY FOR (UNIQUE CANDIDATE NAME: PERCENT VOTES)
#create a dictionary named "percent votes" to hold the percent of votes each candidate received
percent_votes = {}

#loop through total votes dictionary and take total votes for each candidate and divide by the total votes - round to 2 decimal points
for name in total_votes:
    percent_votes [name] = str(round((total_votes [name] / len(candidates) * 100),2)) + "%"

#MERGE TOTAL_VOTE DICTIONARY AND PERCENT VOTE DICTIONARY INTO FINAL RESULT DICTIONARY (UNIQUE CANDIDATE NAME: PERCENT VOTES, TOTAL VOTES)
#create a dictionary named "final result" to merge "total_votes" dictionary with "perect_votes" dictionary

final_result = {}


#loop through "total_votes" dictionary and "percent_votes" dictionary and merge based on candidate name
for name, value in total_votes.items() | percent_votes.items():
    final_result.setdefault(name, set()).add(value)

#
print (final_result)

print (
        "\n-------------------------"
        + "\nWinner "
        + max(total_votes, key=total_votes.get)
        + "\n-------------------------"
    )     
# Write results to text file
file = open('analysis/PyPoll Result.txt', 'w')
file.write ("Election Results"
            + "\n-------------------------" 
            + "\nTotal Votes: " + str(len(candidates))
            + "\n-------------------------"  
            + str(final_result)
            + "\n-------------------------"
            + "\nWinner "
            + str(max(total_votes, key=total_votes.get))
            + "\n-------------------------"
            )
file.close()