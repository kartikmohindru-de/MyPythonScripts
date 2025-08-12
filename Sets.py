#sets have unique elements in them

set1 = set("ABC")
print(set1)

set2 = set()
set2.add("ABC")
print(set2)
list1 = [1,1,1,2,2,2,3,3,3]
set3 = set(list1)
print(set3)
sc = set3.copy()
print(sc.difference(set2))
sa = {1,2,3}
sb= {1,4,5}
sa.difference_update(sb) #common elements from sa will be removed
print( sa)
sa = {1,2,3}
sa.discard(2) #removes element from the set
print(sa)
sa ={1,2,3}
sb = {1,4,5}
print(sa.intersection(sb)) #common elements in both
sa.intersection_update(sb) # only common elements will be left in sa
sa= {1,2}
sb = {5}
print(sa.isdisjoint(sb)) # returns true if no element is common
sa= {1,2}
sb = {1,2,3}
print(sa.issubset(sb)) # check if sa is subset of set sb issupperset is inverse
print(sa.symmetric_difference(sb)) # returns elements only in one set _update updates sa to have only the values
sa.union(sb) #return union of 2 sets
sa.update(sb) #updates with union of both the sets
print(sa)
