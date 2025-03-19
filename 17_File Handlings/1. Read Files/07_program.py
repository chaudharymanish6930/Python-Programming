file=open("D:/python/01upload on github/17_File Handlings/1. Read Files/07_program.txt",'r')
i=0
while True:
    i +=1
    line=file.readline()
    if not file:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]

    print(f"mark of student {i} is {m1}")
    print(f"mark of student {i} is {m2}")  
    print(f"mark of student {i} is {m3}")