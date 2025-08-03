<<<<<<< HEAD
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'w') as file:
    file.write("Hi!, Everyone \n we are learning file handlings in python\n")
    file.write("using java\n")
    file.write("i Like java programminng!\n")
    file.write("java is a good programming language\n\n\n")

    # print data before replacing  
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'r') as file: 
    data=file.read()
    print(data)


# replace code is here

new_data=data.replace("java","python")
print(new_data)


# this change again in main file
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'w') as file:
    file.write(new_data)
=======
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'w') as file:
    file.write("Hi!, Everyone \n we are learning file handlings in python\n")
    file.write("using java\n")
    file.write("i Like java programminng!\n")
    file.write("java is a good programming language\n\n\n")

    # print data before replacing  
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'r') as file: 
    data=file.read()
    print(data)


# replace code is here

new_data=data.replace("java","python")
print(new_data)


# this change again in main file
with open("D:/python/01upload on github/17_file handlings/5. programs (important)/01_replace.txt",'w') as file:
    file.write(new_data)
>>>>>>> 85a1649 (first)
    # print data after replacing