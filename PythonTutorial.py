#lists are mutable
#tupples are imutable
#escape characte "\" great usage
#\ can also symbolises next line
# is is not are heyword equal to = !=
# 2 things when processed with comma separated comes in a s tupple as it is a default sequence
# wage(8),wage_bonus(8) = (200,250)
# order of precedence not>and>or
# if function return multiple values this will be returned as tupples
#strings are immutable that is cannot be muted or changed
#It’s easy to forget that the stored value is an approximation to the original decimal fraction,
#because of the way that floats are displayed at the interpreter prompt.
#Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine.
#If Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display*/
#https://docs.python.org/2/tutorial/floatingpoint.html
#meaning that the exact number stored in the computer is approximately equal to the decimal value
#0.100000000000000005551115123125. In versions prior to Python 2.7 and Python 3.1,
#Python rounded this value to 17 significant digits, giving ‘0.10000000000000001’.
#In current versions, Python displays a value based on the shortest decimal fraction that roundsF_
#correctly back to the true binary value, resulting simply in ‘0.1’.
#Dynamic typing is done here in assignment means same variable can be reused with different datatypes
#strings are immutable that is cannot be muted or changed
#list is mutable that is any of teh elements can be changed
# list = []
#dictionary cannot be sorted,indexed and sliced because of key value relationship
#tupples are immutable rest behave like ists
# tupple = ()
#sets have unique elements in them
#Booleans are True False indicators
#for the conditional statements just remember the identations
#Iterable object- we can iterate over every element in the object
#like character in a string
#key in dictionary
#element in a list.
#tupple unpacking duplicate the structure of objects in sequence
#break breaks out of the current closest loop
#continue goes to the top of current closest loop
#pass do nothing at all acts as a placeholder so if nothing follows while keyword it helps in avoiding syntax error
#from random import library used for making some random combinations of a object
#input('Message to display)
#we need to typecast the inputs into non string data types as  inputs are genrally of type string
'''
int()
float()
str()

'''
# module 'numbers' has no attribute 'Number' this error comes if you name a code of yours as numbers.py avoid it
#def name_of_function():
#def say_hello(name='default'): #if no parameter is passed it wil return default on call
#when we give *args as parameter in  the function we can pass unlimited arguments.
#kwargs key value pair comes as dictionary # we can use **with any variable name key word argument
#min(),max() functions can be used for only 2 numbers comparison if greater we will use them in list
#split function by default returns list
#' '.join(list) it will join the contents of list with space in between
#sum([a,b,c]) sum of a+b+c
#tip for finding prime numbers a list can be started from 2 counter from 3 as it gives an edge of using a step size of 2 as after 2 all else evens are non prime so 3+2 = 5 5+2=7
##map function maps every single item in an object to a function
'''
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
https://book.pythontips.com/en/latest/map_filter.html
'''
#filter function returns only values if they satisfy a condition or make it true. Always use functions that aregoing to have a true or false as output
'''
LEGB RULE FOR VARiABLES:
LOCAL - NAMES ASIGNED IN ANY WAY WITHI A FUNTION  AND NOT DECLARED GLOBAL IN THE FUNCTION
ENCLOSING FUNCTION LOCALS NAMES IN LOCAL SCOPE OF FUNCTION
x=
GLOBAL - NAMES ASSIGNED AT THE TOP LEVEL OF A MODUE FILE OR DECLARED GLOBAL IN DEF WITHIN THE FILE
BUILT IN - NAMES PRE ASSIGNED IN THE RANGE
#global
name = value
def printer():
enclosing
name = value2
def hello():
local
name = value3
we can make chnges to global variable in a function by declaring it global in the function
'''
# punctuationmakr.islower()=false punctuationmakr.isupper()=false
#isdigit() detects whether an input is digit or not
#magic/special functions a must one for oops
#__init.py__ helps compiler in finding that a particular directory is not a normal directory but a package
#all the code at identation level 0 gets run once a program is called so all the function get by default define
#when we run the prog directly __name__ = "__main__"
#when we run indirecty i.e inheritance or import __name__ != "__main__"
#pylint reports back possible issues pylint programname.py in cmd
#unittest built in library for testing
#var = func_name var will start pointing on func_name forever
#a function can return another function defined in it
#a function can be passed as an argument
#print(func_name) address of the func
#print(func_name()) return value of the func
#decorators
#generators a type of function that do not execute all the iterations in a single go like  range
# next() generator's yield object is using it to print the value
# iter() allows us to iterate through normal object iter(object)
#generator comprehension
#extend  takes a list and extends the other one
#use to add more elements into a list
'''
import pdb imports debugger

pdb.set_trace() sets teh checkpoint on th eline following this
'''
'''
#to time the code
import time
start_time - time.time()
#run_code
end_time = time.time()
elapsed = end_time-start_time
import timeit
timeit.timeit
stmt = '''code to run '''
setup = '''setup to be done once like var defining fjnc defining '''
tmeit.timeit(stmt,setup,number=1000000) number = how many times it needs to be executed
'''
#NoneType is the type of the None object which represents a lack of value, for example,
# a function that does not explicitly return a value will return None
#decoratorprac.py
#method vs function function is independent , method is attached to a object or class
#module = pre written code containing definitions of funcs and classes
#package = a collection or directory of related python modules
#standard library = collection of modules avaialble as soon as you install python
##for keys in dictionary never use mutable objects like list but immutable objects like tuples should be used
#https://www.geeksforgeeks.org/filter-pandas-dataframe-with-multiple-conditions/
--List
#range function have starting point inclusive ending as exclusive
#Slicing have first incusive last exclusive
#playersdict.setdefault("Player",[]).append(str(pl4[j+1])[str(pl4[j+1]).find(">")+1:str(pl4[j+1]).find("</")])
#to append dictionary elements

'''
Syntax: defaultdict(default_factory)
Parameters:  

default_factory: A function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.
'''

'''
Default arguments
'''
#casefold case insensitive string comparison
#%timeit to check performance of statement 