year=int(input("enter year:"))
if year%4==0:
    if year%100!=0:
        print("the year is leap year:",year)
    else:
        print("this year is not a leap year:",year)
elif year%400==0:
    print("the year is leap year ",year)