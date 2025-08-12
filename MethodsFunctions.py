#use help function to get actual documentation
#or docs.python.org
#methods-Objects have a variety of built in methods to use
'''
def say_hello():
    print("hello world")

say_hello()

def say_hello(name):
    print("Hello", name)

say_hello('Kartik')

def say_hello(name='default'): #if no parameter is passed it wil return default on call
    print("Hello", name)
def add_num(a,b):
    return a+b
c=add_num(5,10)
print(c)
'''
k = input("Enter column names")
kl = list(k.split())
print(k)
print(kl)

def even_check(a):
    return a%2
n = int(input("input the number")) #we need to typecast inputs
print(even_check(n))
if(even_check(n)):
    print(n,"is odd")

def check_any_even(numlist):
    for nums in numlist:
        if (nums%2 == 0):
            return True
        else:
            pass

numlist = [3,5,7,9,8,10]
print(check_any_even(numlist))

def check_any_even(numlist):
    numlists = []
    for nums in numlist:
        if (nums%2 == 0):
            numlists.append(nums)
        else:
            pass
    return numlists

numlist = [3,5,7,9,8,10]
print(check_any_even(numlist))

#-----using tupple unpacking with functions
def emp_check(work_hrs):
    cur_max = 0
    eom = ''
    for emp,hrs in work_hrs:
        if hrs>cur_max:
            cur_max = hrs
            eom = emp
        else:
            pass
    return(eom,cur_max)

work_hrs = [('ab',30),('cd',50),('ef',200)]
emp,hr = emp_check(work_hrs)
print(emp)
print(hr)
#---args kwargs
#when we give *args as parameter in  the function we can pass unlimited arguments.
def myfunc(*args): #comes as tupple we can use *with any variable name
    print(args)
myfunc(1,2,3)
myfunc(1,2,3,4)
myfunc(1)
def myfunc(**kwargs): #comes as dictionaryq # we can use **with any variable name key word arguments
    print(kwargs)
    for n in kwargs:
        print(kwargs[n])
    for n1 in kwargs:
        print(kwargs['n1'])
    if 'n1' in kwargs:
        print(kwargs['n1'])
    if 'n' in kwargs:
        print(kwargs['n'])
myfunc(n1=1,n2=2)
#myfunc(1,2,3,4)
#myfunc(1)

def myfunc(*args,**kwargs):
    print(args[0], kwargs['n1'])
myfunc(10,2,3,n1=1,n2=2)