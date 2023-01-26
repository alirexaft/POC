# import csv
#
# # def myFunc():
# #     with open('C:\\Users\\Alireza\Desktop\\employee_birthday.csv', mode='r') as csv_file:
# #         csv_reader = csv.DictReader(csv_file)
# #         line_count = 0
# #         for row in csv_reader:
# #             if line_count == 0:
# #                 line_count += 1
# #                 print(row)
# #             print(row)
# #
# #             line_count += 1
# #     return line_count
#
# # print(line_count)
#
# # file = open("C:\\Users\\Alireza\Desktop\\employee_birthday.csv")
# #
# # print(file)
#
# with open('C:\\Users\\Alireza\Desktop\\employee_birthday.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     line_count = 0
#     for row in spamreader:
#         if line_count == 0:
#             line_count += 1
#             print(row)
#
#         line_count += 1
#
#
# print(line_count)

# importing csv module
import csv

# csv file name
# filename = "C:\\Users\\Alireza\Desktop\\employee_birthday.csv"
#
# # initializing the titles and rows list
# fields = []
# rows = []
#
# # reading csv file
# with open(filename, 'r') as csvfile:
#     # creating a csv reader object
#     csvreader = csv.reader(csvfile)
#
#     # extracting field names through first row


#     # extracting each data row one by one
#     for row in csvreader:
#         rows.append(row)
#
# #     # get total number of rows
# #     print("Total no. of rows: %d" % (csvreader.line_num))
# #
# # # printing the field names
# # print('Field names are:' + ', '.join(field for field in fields))
#
# # printing first 5 rows
# # import module
# import pandas as pd
#
# # read CSV file
# results = pd.read_csv('C:\\Users\\Alireza\Desktop\\myCSV.csv')
#
# # count no. of lines
# print("Number of lines present:-",
# 	len(results))
# Setting initial value of the counter to zero

def myFunction():

    rowcount = 0
    # iterating through the whole file
    for row in open("C:\\Users\\Alireza\Desktop\\myCSV.csv"):
        rowcount += 1
    # printing the result
    return rowcount
