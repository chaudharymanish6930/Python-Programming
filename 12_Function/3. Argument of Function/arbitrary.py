def average(*numbers): #convert into tuple forms
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average is: ",sum/len(numbers))

average(5,6)
    

# another atributes of functions
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")

greet_all("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

def name(**name):  #dictionary of name
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"])

name(mname="buchana",lname="barnes",fname="james")



