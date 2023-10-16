side1=int(input('Enter side 1 of Triangle: '))
side2=int(input('Enter side 2 of Triangle: '))
side3=int(input('Enter side 3 of Triangle: '))
if side1==side2 and side2==side3:
    print('EQUILATERAL TRIANGLE')
elif side1!=side2 and side2!=side3:
    print('SCALENE TRIANGLE')
else:
    print('ISOSCELES TRIANGLE')