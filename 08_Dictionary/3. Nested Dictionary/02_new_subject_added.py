student={
    "name":"Rahul",
    "class":"10th",
    "subject":{
        "sub1":"Maths",
        "sub2":"Science",
        "sub3":"English"
    }
}

student["subject"]["sub3"]="Hindi"
print(student)
# Output:
# {'name': 'Rahul', 'class': '10th', 'subject': {'sub1': 'Maths', 'sub2': 'Science', 'sub3': 'Hindi'}}