str1 = 'Hello'
str2 = "Great"
str3 = "It's an example"
print(str1[0]) #index starts at 0
print(str1[-1]) #gets the last letter
print(str1[0:3]) #str[start:stop:step] start=position from which the slice needs to begin it is included, stop till wha position you want
#the slicing not included, step how many will be skipped
print("Hello \\n World")
print("Hello \n World")
print(len(str1))
print(str1[1:])
print(str3[:5])
print(str3[::-1])#reverse
#strings are immutable that is cannot be muted or changed
print('P'+str1[1:]) #to change first letter of string str1
print(10 *'z')
print(str1.upper()) #need to reassign to change the string
print(str3.split(" "))
print('this is a string {}'.format('inserted'))
print('this is a string {1} {0} {2}'.format('inserted','i have','in')) #take the variables from the index positions
print('this is a string {b} {a} {c}'.format(a='inserted',b='i have',c='in'))
print('this is a string {}'.format(str1))
res = 100/777
print('result is {r:1.3f}'.format(r=res))
username="John"
print(f'hello welcome {username}')

if('x' in "uvwxyz"):
    print(False)
else:
    print(True)

inputs = input('enter a string')
print("the third character is", inputs[2] )

str = "aaaaaaaaaaaaabbbbbbbbddddddddddeeeemmmmmmmm"
str.count("a")

str3 = "It's an example"
n = 3
l = len(str3)
print(str3[0:n])