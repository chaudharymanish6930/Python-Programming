# y=[expression for item in iterable if conditional]
y=[x for x in 'items'  ] # [x for x in 'items' if y]
print(y)

new_li=[]
for x in range(1,51):
    if x%2==0 and x%3==0:
        new_li.append(x)
print(new_li)