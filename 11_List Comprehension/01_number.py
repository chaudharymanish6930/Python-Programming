list=[2,4,6,8,10]
new_list=[i*2 for i in list if i%2==0]
new_list1=[i+2 for i in list]
new_list2=[i**2 for i in list]
# condition is not mendentory for this 
print(list)
print(new_list)
print(new_list1)
print(new_list2)