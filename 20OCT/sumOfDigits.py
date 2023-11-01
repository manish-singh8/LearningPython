num = int(input('Enter number: '))
sum1 = 0

while (num != 0):
    sum1 = sum1+(num % 10)
    num = num//10
print(f'The sum of digits is : {sum1}')