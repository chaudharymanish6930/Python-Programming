def average(a,b):
    print("the average is ",(a+b)/2)

average(4,5 )

#ingnore our arguments
def average(a=6,b=8):
    print("the average is ",(a+b)/2)

average(4,5 )

# only one value in fuction call
def average(a=6,b=8):
    print("the average is ",(a+b)/2)

average(5 )

#another one value
def average(a=6,b=8):
    print("the average is ",(a+b)/2)

average(b=5 )

#important   ------------------------------------|
# from harry |                                   |
#           --                                   |
def name(fname,mname="jhon",lname="watson"):  #  |
    print("hello",fname,mname,lname)          #  |
                                          #   #  |
name("amy") #-------------------------------------


