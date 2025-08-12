

a=2+1
print(a)
print(2/2)
print(2**3)
print(0.1+0.2) #not resulted in exact .3
#It’s easy to forget that the stored value is an approximation to the original decimal fraction,
#because of the way that floats are displayed at the interpreter prompt.
#Python only prints a decimal approximation to the true decimal value of the binary approximation stored by the machine.
#If Python were to print the true decimal value of the binary approximation stored for 0.1, it would have to display*/
#https://docs.python.org/2/tutorial/floatingpoint.html
#meaning that the exact number stored in the computer is approximately equal to the decimal value
#0.100000000000000005551115123125. In versions prior to Python 2.7 and Python 3.1,
#Python rounded this value to 17 significant digits, giving ‘0.10000000000000001’.
#In current versions, Python displays a value based on the shortest decimal fraction that rounds
#correctly back to the true binary value, resulting simply in ‘0.1’.
#Dynamic typing is done here in assignment means same variable can be reused with different datatypes
t=type(a)
print(t)
round(5.3222,2) rounds to 2 decimal places