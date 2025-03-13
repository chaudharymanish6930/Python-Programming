name_set={"Arpit","Manish","Amit","Bohit","Bharat","joney"}
setA=set()
setB=set()
setC=set()
for i in name_set:
    if i[0]=="A":
        setA.add(i)
    elif i[0]=="B":
        setB.add(i)
    else:
        setC.add(i)
    # print("first letter ""A"":",{setA},"first letter "B":",{setB})
print(f"first letter A:{setA},\n first letter B:{setB},\nother first letter:{setC}")
