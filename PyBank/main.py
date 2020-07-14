import os
import csv

#store filepath of budget data source data
budgetdata_csv = r"/Users/carawilliams/Repository/python-challenge/PyBank/Resources/budget_data.csv"

with open(budgetdata_csv) as csvfile:
    csvreader=csv.reader(csvfile)

    csvheader=next(csvreader)

    print(csvheader)