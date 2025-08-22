# intersection of sets
s1={11,2,57,8,4,}
s2={23,8,5,4,12,57}
print(s1.intersection(s2))
# s3=s1.intersection(s2)
# print(s3)

# updte intersecctions of sets
s1.update(s2)
print(s1,s2)

#s1 same sa the uppdated
s2.update(s1)
print(s1,s2)