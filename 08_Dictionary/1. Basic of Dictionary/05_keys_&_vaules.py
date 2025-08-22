info={
    "sweety":"doggy","candy":"girl",
    "chiku":"boy","msdhoni":"cricketer",
    7:"thala","virat":18
}

print(info)
print(info.keys())
print(info.values())

for k in info.keys():
    print(info[k])

for k in info.keys():
    print(f"the corespondinng value to the key {k} is {info[k]}")

for l in info.values():
    print(info[l])