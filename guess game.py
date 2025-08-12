from random import shuffle
def shuffle_lists(lists):
    shuffle(lists)
    return(lists)
def guess():
    g=''
    while g not in['0','1','2']:
        g=input("enter choice from 0,1,2")
    return int(g)

def check(lsits,g):
    if( lsits[g]=='O'):
        print('correct')
    else:
        print(lsits)

lists = ['','O','']
slists = shuffle_lists(lists)
print(slists)
choice = guess()
check(slists,choice)