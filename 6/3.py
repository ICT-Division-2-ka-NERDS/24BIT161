def leap(year):
    if year%4==0:
        return True

def month1(month, year):
    monthh=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(year):
        monthh[1]=29
    return monthh[month-1]

date1=[5,12,2025]
date2=[17,3,2024]

def days(date, month, year):
    day=0
    for y in range(0,year):
        if leap(y):
            day+=366
        else:
            day+=365
    for m in range(1,month):
        day+= month1(month, year)

    day+=date

    return day

print("Number of days= ", days(date1[0],date1[1],date1[2])-days(date2[0],date2[1],date2[2]))
