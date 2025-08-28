list=[1,2,3,4,5,6,7]
list1=[list[2],list[4]]
list.append(list1)
list.remove(list[4])
list.remove(list[2])
list[2]=list1
print(list)