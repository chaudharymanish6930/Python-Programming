file=open("D:/python/01upload on github/17_File Handlings/3. Stream/03_a.txt","a+")
print(file.read())
file.write("hello world!\n")
print(file.read())
file.close()