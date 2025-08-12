lt = 3
lst = [-1,2,3]
maxlst=[]
print(lst[0:1])
for j in range(0,len(lst)):
    if(j==0):
        if(lst[0]>sum(lst)):
            maxlst.append(lst[0])
        else:
            maxlst.append(sum(lst))
    else:
        newlst1=lst[0:j+1]
        newlst2=lst[j:lt]
        print(j)
        print(newlst1)
        print(newlst2)
        if(sum(newlst1)>sum(newlst2)):
            maxlst.append(sum(newlst1))
        else:
            maxlst.append(sum(newlst2))
print(maxlst)
print(max(maxlst))