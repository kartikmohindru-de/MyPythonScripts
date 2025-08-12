#dictionary cannot be sorted,indexed and sliced because of key value relationship
dict1={'key1':'val1' ,'key2': 'val2'}
print(dict1['key1'])
dict1={'k1':245958 ,'k2': [1,2,3], 'k3':{'insidekey':100}}
print(dict1['k2'])
print(dict1['k2'][1])
print(dict1['k3']['insidekey'])
dict1['k4'] = 'New record' #appends new key
print(dict1['k4'])
dict1['k4'] = 'New records' #changes value
print(dict1['k4'])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

if('x' in dict1.keys()):
    print(False)
else:
    print(True)
if('x' in dict1.values()):
    print(False)
else:
    print(True)
dict1={'key1':'val1' ,'key2': 'val2'}

for k in dict1: #prints all the keys
    print(k)
for k in dict1.values():
    print(k)

#for keys in dictionary never use mutable objects like list but immutable objects like tuples should be used
#playersdict.setdefault("Player",[]).append(str(pl4[j+1])[str(pl4[j+1]).find(">")+1:str(pl4[j+1]).find("</")])
#to append dictionary elements