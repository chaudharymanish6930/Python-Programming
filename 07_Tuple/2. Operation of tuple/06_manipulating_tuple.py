countries =("spain","italy","india","england","germany")
temp=list(countries)
temp.append("russia")   #add item
temp.pop(3)             #remove item
temp[2]="finland"       #change item
countries=tuple(temp)
print(countries)