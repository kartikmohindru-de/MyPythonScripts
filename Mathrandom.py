import math
import random
#print(help(math))
print(math.floor(4.5))
math.log(100,10) #10 is base and 100 is number
random.seed(21) #it makes randint to get same number for a range, returns only for first call for randint
random.randint(0,100)
mylist = [10,20,30,40,50,60]
random.choices(population=mylist,k=10) #sample with replacement\
random.sample(population=mylist,k=10) #sample without replacement no repetion