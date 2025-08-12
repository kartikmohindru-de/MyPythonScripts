loc = 'Bank'
if loc == 'Auto Shop':
    print("cars are present")
elif loc == 'Bank':
    print("Money is cool")
else:
    print("I do not know much")

#--------------------------for loops
#Iterable object- we can iterate over every element in the object
#like character in a string
#key in dictionary
#element in a list.

list1 = [1,2,3,4]
for i in list1:
    print(i)
for i in range(10,20):
    print(i)
string1 = "HEY HELLO LISTEN"
for a in string1:
    print(a)
list2 = [(1,2),(3,4),(5,6)]

for item in list2:
    print(item)
    for items in item:
        print(items)
#tupple unpacking duplicate the structure of objects in sequence
for (a,b) in list2:
    print(b)
for a, b in list2:
        print(a)
dict = {'k1':1, 'k2':2, 'k3':3}
for i in dict:
    print(i) #by default dict have iteratable keys
for k,v in dict.items(): #this gives tupple expressions so we can use tupple unpcking here
    print(v)
for v in dict.values(): #this gives tupple expressions so we can use tupple unpcking here
    print(v)
#----------------------------while loop--------------------------------------
x=0
while x<5:
    print(x)
    x = x+1
#break breaks out of the surrent closest loop
#continue goes to the top of current closest loop
#pass do nothing at all acts as a placeholder so if nothing follows while keyword it helps in avoiding syntax error
while x<5:
    pass #do nothing acts as a placeholder so if nothing follows while keyword it helps in avoiding syntax error
print("continue")
for x in range(0,5):
    if(x==2):
        continue
    print(x)
    x = x+
    A4xb950W * 9$6Js2FLqy  # xGI7