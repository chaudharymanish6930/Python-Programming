# symmetric differnce of sets
# A-B
s1={11,2,57,8,4,}
s2={23,8,5,4,12,57}
print(s1.symmetric_difference(s2))
# print(s1.symmetric_difference_update(s2))
s1.update(s2)
print(s1,s2)
print("s2 then s1")
s2.update(s1)
print(s1,s2)