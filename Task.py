import re
class AlphanumericException(Exception):
    pass
class StringException(Exception):
    pass

def isvalid(v,i):
    if(i==0):
        if (isinstance(v, int)):
            return "Valid"
    else:
        if (re.fullmatch('[A-z]+',v)):
           return "String"
        if (re.fullmatch('[0-9]+',v)):
           return "Number"
        else:
            return "Valid"
l=True
i=0
n=input()
try:
    while l:
        if(i==0):
            if(re.fullmatch('[0-9]+',n)):
                n=int(n)
            else:
                if(re.match('[0-9]+',n)):
                    raise AlphanumericException
                else:
                    raise StringException
        val = isvalid(n,i)
        if(val!="Valid"):
            raise Exception("String Error")
        else:
            print("Valid")
        n=input()
        if(n==''):
            l=False
        else:
            l=True
            i=i+1
except AlphanumericException:
    print("This is Alphanumeric")
except StringException:
    print("This is StringException")


