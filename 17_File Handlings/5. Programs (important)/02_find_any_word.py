with  open("D:/python/01upload on github/17_File Handlings/5. Programs (important)/01_replace.txt",'r') as file:
    content=file.read()
    if "python" in content:
        print("Yes, the word is present")
    else:
        print("No, the word is not present")