ep1={
    122:45,
    123:89,
    345:69,
    670:69,
    453:97
}
ep2={
    22:34,
    566:90
}

ep1.update(ep2)
print(ep1) 

ep1.pop(123)
print(ep1)

# remove last item from the dictionary
ep1.popitem()
print(ep1)