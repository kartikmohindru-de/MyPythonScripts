#__INIT__() HELPS IN INSTANTIATING A CLASS AND AN OBJECT.
#methods are functions in a class
class dog():
    #class object attribute to remain constant for any isntance
    species = 'mammal'

    def __init__(self, breed,ages): #always gets called whenever a class is initiated, it is like constructor
        self.breed = breed
        self.age = ages #by convention they all should ahve the same name but changing name do not make a differnece
        print(breed)
        #print(age) #whenever we need to print a variable we need to use self because it connects object with variable
    def bark(self):
        print("Woof my name is ",self.breed)
    def bark2(self,number):
        print("Woof my name is ", self.breed, number)

#my_sample = dog('lab',3) #if we pass no parameter now it will show error because it requires one in init
my_sample = dog(breed='lab', ages=3)
print(my_sample.breed)
print(my_sample.age)
print(my_sample.species) #species is not required to be defined because it is a class object attribute for any instance
my_sample.bark() #calling a method
my_sample.bark2(3)
print(dir(my_sample)) #list of all attributes associated with a class
