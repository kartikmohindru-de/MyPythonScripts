#pandas very important
#openpyxl specifically for excel files
#python-excel.org
#googlesheets python API
import csv
data = open('TestFile.csv',encoding='utf-8') # encoding required for special char parsing
csv_data = csv.reader(data)
data_lines = list(csv_data) #first element of list is column names
print(data_lines)
for line in data_lines[:5]:
    print(line)
len(data_lines) #record count of file
all_emails = []
for lines in data_lines:
    all_emails.append(lines[1])
print(all_emails)
full_details = []
for line in data_lines[1:]:
    full_details.append(line[0]+' '+line[1]+' '+line[2])
print(full_details)

file_out = open('fileout.csv', mode = 'w',newline='') #append mode can write mpre lines
csv_writer = csv.writer(file_out,delimiter=',')
csv_writer.writerow(['col1','col2','col3']) #writes one line
csv_writer.writerows([['val1','vsl2',3],['val4',5,'val6']]) #many line
#PYpdf2 LIBRARY FOR PDFS
#ALL PDF FILES ARE NOT READABLE BECAUSE OF ITS CONTENTS AND FORMATTING

