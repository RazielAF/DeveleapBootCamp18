import sys
import os.path
import re

ISNUM = "-?\d+" #Regex to find numbers

def sum_column(filename, column_number, length):
    with open(filename,'r') as file:
        column_name = file.readline().split(",")[column_number]
        not_number_counter = 0
        amount = 0
        for line in file:
            field = line.split(",")[column_number]
            if field:
                try:
                    if re.findall(ISNUM,field):
                        amount += float(field)
                    else:
                        not_number_counter += 1
                except ValueError:
                    print("ERROR: Invalid")
                    exit()
            else:
                not_number_counter += 1
                continue
    print(f'\nIn your column is \'{column_name}\' there are {not_number_counter} field(s) which either not numeric or empty')
    return amount

if __name__ == '__main__':
    filename = sys.argv[1]
    column_number = int(sys.argv[2])
    if os.path.isfile(filename):
        with open(filename,'r') as file:
            arr = file.readline().split(",")
            length = len(arr)
            
            if length -1 < column_number: #check valid colum number
                print("ERROR: the file given has less colums then the argument given")
            else:
                total = sum_column(filename, column_number, length)
                print(f'The total sum of your column is - {total:,.1f}\n')
    else:
        print("ERROR: Invalid file given as an argument")









