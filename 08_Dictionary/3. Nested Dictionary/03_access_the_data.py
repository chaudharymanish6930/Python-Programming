student={
    "name":"Rahul",
    "class":"10th",
    "subject":{
        "sub1":"Maths",
        "sub2":"Science",
        "sub3":"English"
    },
    "marks":{
        "sub1":90,
        "sub2":80,
        "sub3":70
    }
}
student["subject"]["sub3"]="Hindi"
print(student)

print(student["marks"]["sub3"])  #70