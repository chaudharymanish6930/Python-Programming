file=open("D:/python/01upload on github/17_File Handlings/1. Read Files/01_read_file.txt",'r')
content=file.read()
print(content)
print(type(content))
print(content.strip())   #remove the new line character in program  
file.close()