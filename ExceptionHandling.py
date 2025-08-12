#try tries the code
#except executed if tehre is an error
# else gets executed if tehre is no error
#finally executes any how

def add(n1,n2):
    print(n1+n2)


try:
    add(10,"abc")

except: #except Type Error you can always put a built in error type 
    print("not adding correctly")
else:
    print("done well")
finally:
    print("execution completed")