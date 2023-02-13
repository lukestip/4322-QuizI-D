'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

open1 = open('employee_data.csv', 'r')
infile = csv.reader(open1, delimiter=',')

# create an empty dictionary

empIncrease = {}

# use a loop to iterate through the csv file
for i in infile:
    # check if the employee fits the search criteria
    if i[3] == 'Marketing' and i[4] == 'CSR':
        print(
            f'Manager Name: {i[1]} {i[2]} Current Salary: ${float(i[5]):,.2f}')
        empName = i[1]+' '+i[2]
        empIncrease[empName] = float(i[5])*1.1


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
for k, v in empIncrease.items():
    print(f'Manager Name: {k} New Salary: ${v:,.2f}')
