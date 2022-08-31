# function 
from traceback import print_tb


print("======================\n")
def myName():
    print("irmansyah")
    
myName()
# a function with parameters
print("========================\n")

def segitiga(a,t):
    return 1/2*a*t

b = segitiga(10,10)

print(b)

print("=====================\n")
# a function with tuple

def hello(*names):
    print("welcome to jungle "+names[2])
    
hello('irmansyah','bagus','umi')

print("=====================\n")
# a function with key and value

def member(name1,name2,name3):
    print('hello i just learn python language ' + name2)
    
member(name1 = "wkwk" , name2 ='umi', name3="wakanda")

print("=====================\n")
# a function with parameter default

def myCity(name = 'bogor'):
    print('my city is '+name)
    
myCity()

print("=====================\n")
# fuction can empaty statatment

def kosong():
    pass

kosong()