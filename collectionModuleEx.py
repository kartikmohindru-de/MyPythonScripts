from collections import Counter
from collections import defaultdict # if a wrong key is asked for in default dict it will give a default val to it
from collections import namedtuple
mylist = [1,1,1,2,2,2,3,3,3,4]
print(Counter(mylist))# tells the count of a unique records in dictionary format
sentence = "Lets count number of words in this group of words"
print(Counter(sentence.split()))
print(Counter(sentence.split()).most_common()) #if we provide  number argument so it will give out that number of most common
print(Counter(sentence.split()).most_common(1))
d = {'a':10}
d = defaultdict(lambda:0)
d['correct'] = 100
print(d['correct'])
print(d['wrong'])

dog = namedtuple('Dog',['age','breed','name'])
sammy = dog(age=5,breed='huske',name = 'sam')
print(sammy)
print(sammy.age)
print(sammy[0])
'''
A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. 
If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.
>>> baseline = {'music': 'bach', 'art': 'rembrandt'}
>>> adjustments = {'art': 'van gogh', 'opera': 'carmen'}
>>> list(ChainMap(adjustments, baseline))
['music', 'art', 'opera']
class collections.deque([iterable[, maxlen]])
Returns a new deque object initialized left-to-right (using append()) with data from iterable. If iterable is not specified, the new deque is empty.
from collections import deque
>>> d = deque('ghi')                 # make a new deque with three items
>>> for elem in d:                   # iterate over the deque's elements
...     print(elem.upper())
https://docs.python.org/3/library/collections.html
'''