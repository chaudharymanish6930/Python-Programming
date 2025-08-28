from tkinter import * 
root = Tk() 
root.title("Calculator") 
root.geometry ("240x340") 
root.configure(bg ="#333333") 
root. resizable(0,0) 
entry = None 
expression = "™" 
# Define functions for the buttons 
def press_0(): 
    entry.insert(END,"0") 
def press_1(): 
    entry.insert(END,"1") 
def press_2(): 
    entry.insert(END,"2") 
def press_3(): 
    entry.insert(END,"3") 
def press_4(): 
    entry.insert(END,"4") 
def press_5(): 
    entry.insert(END,"5") 
def press_6(): 
    entry.insert(END,"6") 
def press_7(): 
    entry.insert(END,"7") 
def press_8(): 
    entry.insert(END,"8") 
def press_9(): 
    entry.insert(END,"9") 
def press_plus(): 
    entry.insert(END,"+") 
def press_minus(): 
    entry.insert(END,"-") 
def press_multiply(): 
    entry.insert(END,"*") 
def press_divide(): 
    entry.insert(END,"/") 
def press_equal(): 
    global expression 
expression = entry.get() 
entry.delete(0,END) 
entry.insert(0,eval(expression)) 
def press_clear(): 
    entry.delete(0,END) 
#Entry box for displaying the values and results 
entry = Entry (root, font=("Times New Roman", 12)) 
#Labels from 0 to 2 
label_0 = Label(root, text="0",bg="#333333",fg="white" ,width=5,border=1, font=("Times New Roman", 12)) 
label_1= Label(root, text="1",bg="#333333",fg="white" ,width=5, font=("Times New Roman", 12)) 
label_2 = Label(root, text="2",bg="#333333",fg="white" ,width=5, font=("Times New Roman", 12)) 
#Buttons from 0 to 2, + 
button_0=Button(root,text="0",bg="#A73278", fg="white"  ,width=5,font=("Times New Roman", 12),command=press_0) 
button_1= Button(root,text="1",bg="#A73278", fg="white" ,width=5,font=("Times New Roman", 12),command=press_1) 
button_2 =Button(root, text="2",bg="#A73278", fg="white" ,width=5,font=("Times New Roman", 12),command=press_2) 
button_3=Button(root, text="3",bg="#A73278", Roman",12),command=press_3) fg="white" ,width=5,font=()
button_4 =Button(root, text="4",bg="#A73278", fg="white" ,width=5,font=("Times New Roman", 12),command=press_4) 
button_5=Button(root, text="5",bg="#A73278",  Roman",12),command=press_5) fg="white" ,width=5,font=("Times New")
button_6=Button(root,text="6",bg="#A73278", fg="white" ,width=5,font=("Times New Roman", 12),command=press_6) 
button_7=Button(root, text="7",bg="#A73278", fg="white" ,width=5,font=("Times New Roman" 
,12),command=press_7) 
button_8=Button(root, text="8", bg="#A73278", fg="white" ,width=5, font=("Times New 
Roman",12),command=press_8) 
button_9=Button(root, text="9",bg="#A73278", fg="white" ,width=5,font=("Times New Roman", 
12),command=press_9) 
button_plus=Button(root,text="+",bg="#A73278",fg="white"  ,width=5,font=("Times New Roman" 
,12),command=press_plus) 
button_minus=Button(root, 
text=" 
NewRoman",12),command=press_minus) -",bg="#A73278",fg="white" 
,width=5,font=("Times 
button_multiply=Button(root, text="*",bg="#A73278",fg="white" ,width=5,font=("Times New Roman" , 12 ) ,command=press_multiply) 
button_divide=Button(root, text="/",bg="#A73278", fg="white" ,width=5,font=("Times New 
Roman", 12),command=press_divide) 
button_equal =Button(root, text="=",bg="#A73278",fg="white"  
Roman",12),command=press_equal) 
,width=5,font=("Times New 
button_clear =Button(root,text="Clear",bg="#A73278",fg="white" ,width=5,font=("Times New 
Roman", 12),command=press_clear) 
#Placing widgets on the window 
entry.grid(row=0,column=0,columnspan=3,sticky="news",pady=40) 
button_1.grid(row=1,column=0) 
button_2.grid(row=1,column=1) 
button_3. grid(row=1,column=2) 
button_4.grid(row=2,column=0) 
button_5.grid(row=2,column=1) 
button_6.grid(row=2,column=2) 
button_7.grid(row=3,column=0) 
button_8.grid(row=3,column=1) 
button_9.grid(row=3,column=2) 
button_0.grid(row=4,column=0,columnspan=3) 
button_plus.grid(row=5,column=0) 
button_minus.grid(row=5,column=1) 
button_multiply.grid(row=5,column=2) 
button_divide.grid(row=6,column=0) 
button_equal.grid(row=6,column=1) 
button_clear.grid(row=6,column=2) 
root.mainloop()