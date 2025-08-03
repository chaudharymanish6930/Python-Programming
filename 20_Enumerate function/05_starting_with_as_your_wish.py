x=("apple","banana","cherry","dates","elderberry","fig","grape","honeydew","jackfruit")
for v in enumerate(x, start=1):
    index, value = v
    print(index, value)
    print(f"index={index}, value={value}")
