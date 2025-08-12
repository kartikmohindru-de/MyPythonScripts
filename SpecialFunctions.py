class sample():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self): #magic func helps in getting values of string when a string function is used on the object tp print
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
        #return len(self.title) a way to gt the length of a string
mysample = sample("python","kk",24)
print(mysample) #giving out put of string magic function
print(len(mysample)) #gives out numeric value returned bu __len__
#mysample = sample()
#len(mysample) # it will give error as this is a user defined object unlike length,set without using magic functions or dunder functions

