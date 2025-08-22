fruit ="mango"
mangolen=len(fruit)
print(mangolen)
# 1st
print("1st")
print(fruit[0:4]) #including 0 but not 4
print(fruit[1:4]) #including 1 but not 4
print(fruit[:])   #including 0 but not 0
print(fruit[:5]) 
# 2nd
print("2nd")
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])
# 3rd
print("3rd")
print(fruit[-1:len(fruit)-2])
print(fruit[-1:-3])
print(fruit[-3:-1]) # len(fruit)-1