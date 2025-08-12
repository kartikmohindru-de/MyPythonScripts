import csv
data = open('NewCustomer.csv',encoding='utf-8') # encoding required for special char parsing
csv_data = csv.reader(data)
data_lines = list(csv_data) #first element of list is column names
print(len(data_lines))
newlst = []
for i in range(2,len(data_lines)):
    newlst.append(data_lines[i][4])
    #print(data_lines[i][0])

setnewlst = set(newlst)
print(len(setnewlst))
newlst.sort()
print(newlst)