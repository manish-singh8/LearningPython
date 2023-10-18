#Leap Year checker
year=int(input('Enter the year: '))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print('Given Year IS Leap Year')
        else:
            print('Given Year IS NOT Leap Year')
    else:
        print('Given Year IS Leap Year')
else:
    print('Given Year IS Leap Year')

#2 Solution

if ((year%4==0 and year%100!=0) or (year%400==0)):
    print(f'Given Year {year} IS Leap Year')
else:
    print(f'Given Year {year} IS NOT Leap Year')