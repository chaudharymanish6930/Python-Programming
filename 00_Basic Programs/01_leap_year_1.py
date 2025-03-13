x=int(input("enter the year :"))
if (x%4==0 and x%100!=0) or (x%400==0):
    print("the given year is leap year")
else:
    print("it is not a leap year")