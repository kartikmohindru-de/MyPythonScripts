#list is mutable that is any of teh elements can be changed
list1=[1,'abc',1.3]
list2 =[1,2,3]
print(len(list1))

print(list1[0])
#slicing and indexing works just like strings
listconc=list1+list2 #concatenating the 2 lists
print(listconc)

list1[0]=3
print(list1)
list1.append(1.4) #places any item in the list towards the end
print(list1)
list1.pop()
print(list1)#takes out any item in the list towards the end
pop_item= list1.pop()
print(pop_item)
list1.pop(1)#takes out any item in the list from a specified index
#list1=[1,'abc',1.3]
#list1.sort()
#print(list1)#sorting will be done if datatypes are same
list2.sort()
print(list2)
#None datatype for no value that is default value for functions that do not return anything.
list2.reverse()
print(list2)

list3=[0]*3
print(list3)

sorted(list2) #sorts the list

for num in range(0,10):
    print(num)
list4=list(range(0,10,2))

if('x' in list1):
    print(False)
else:
    print(True)


min(list2) #minimum in a list
max(list2) #max in a list
# list comprehension- used to avoid append function with for loop
strings = 'hellopython'
mylist = [x for x in strings] #the outer x comes from inner x so the outer one should be same to iner
print(mylist)
mylist = [x**2 for x in range(0,5)]
print(mylist)
mylist = [x for x in range(0,5) if x%2==0]
print(mylist)
mylist = [x if x%2==0 else 'ODD' for x in range(0,5) ]
print(mylist)
mylist = [x*y for x in range(0,5) for y in range(0,3) ] #y is nested under x
print(mylist)

l = [1,2,3]
l.append(5)
l.count(3) #counts how many time number is present in teh list
l.extend([1,2]) #adds the element indivisually by appending it as list in list whie append will do it as 1 element
l.index(1) #finds at what index the value is
l.insert(3,'inserted') #index first and then the string it do not overwrite any value on that index
l.pop() #takes out the last element by default from list permannetly, we can pass an index to delete it
l.remove() #removes the first insatnce of the value from lst
l.reverse() #reverses the list
l.sort() #sorts list
