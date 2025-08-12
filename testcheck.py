limit = input()
lst = input()
lst1 = lst.split(" ")
newlst=[]
for i in range(0,int(limit)):
    for j in range(i+1,int(limit)):
        sum = int(lst1[j])+int(lst1[i])
        newlst.append(sum)
        print(sum)
print(max(newlst))