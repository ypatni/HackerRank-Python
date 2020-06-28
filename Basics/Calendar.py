import calendar 
month, day, year = map(int, input().split())

x = calendar.weekday(year,month,day)
if x == 0:
    print("MONDAY")
elif x ==1:
    print("TUESDAY")
elif x ==2:
    print("WEDNESDAY")
elif x ==3:
    print("THURSDAY")
elif x ==4:
    print("FRIDAY")
elif x ==5:
    print("SATURDAY")
elif x == 6:
    print("SUNDAY")