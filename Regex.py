import re # class required for regex
text = "The agent's phone number  is 508-555-1234 call on this phone"
a=re.search("phone",text) #re.search(pattern,text)
print(a)
print(a.group())
b=re.findall("phone",text) #finds all the occurences of a pattern in text
print(b)
for ab in re.finditer("phone",text):#iterates through each occurence
    print(ab.group())
c = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
d = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(c.group())
print(d.group())
e=re.compile(r'(\d{3})-(\d{3})-(\d{4})') #grouping like ()() grouping patterns together
f=re.search(e,text)
print(f.group(1))
test2 = "ABA"
print(re.compile(r'A'))
print(re.search)