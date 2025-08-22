file=open("D:/python/01upload on github/17_File Handlings/read_files/03_read_line_by_line.txt",'r')
line=file.readlines()
print(line)

# print(line.strip())
line1=file.readline()
print(line1)

file.close()