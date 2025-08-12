word = 'abcdef'
for item in enumerate(word):
    print(item)
for index,value in enumerate(word):
    print(value)
    print(index)


#enumrators are use to iterate the iteratable objects like list, output is of the type list with (index,value)
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = [100,200,300]
for item in zip(list1,list2,list3):
    print(item)
#the zip function takes into consideration number of elements present in shortest list ignoring the rest, no errors are given