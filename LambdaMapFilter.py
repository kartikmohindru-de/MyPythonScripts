#map function maps every single item in an object to a function
def squares(n):
    return n**2
mynum=[1,2,3,4,5,6]
print(map(squares,mynum))#gives memory location
print(list(map(squares,mynum)))
#filter function returns only values if they satisfy a condition or make it true. Always use functions that aregoing to have a true or false as output
def check_evens(num):
    return num%2==0
print(list(filter(check_evens,mynum)))
#lambda done for something that is not to be used mor ethan once replace def with lambda i.e and return is ommitted def squares(n): return n**2
y=lambda x:x**2 #assigning to y i.e. y() will be called as function call
print(y(5))

print(list(map(lambda x:x**2,mynum)))
print(list(filter(lambda x:x%2==0,mynum)))