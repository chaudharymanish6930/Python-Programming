student={
    "name":"Rahul",
    "class":"10th",
    "subject":{
        "sub1":"Maths",
        "sub2":"Science",
        "sub3":"English"
    }
}
print(student.get("subject"))  # {'sub1': 'Maths', 'sub2': 'Science', 'sub3': 'English'}
print(student.get("subject").get("sub3"))  # English
print(student.get("subject").get("sub4"))  # None
print(student["name1"])  # KeyError: 'name1'
print(student.get("name1"))  # None