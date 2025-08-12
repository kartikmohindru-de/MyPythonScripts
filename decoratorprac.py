def newdeco(funcname):

    def inner():
        print("something before")
        funcname()
        print("something after")
    return inner

@newdeco
def needsdeco():
    print("need a deco")

needsdeco()