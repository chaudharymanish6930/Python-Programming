with open("D:/python/01upload on github/17_File Handlings/read_files/03_read_line_by_line.txt") as file:
    print(file.read())
    print("next line....")
    print(file.read(10))
    print(file.read(20))