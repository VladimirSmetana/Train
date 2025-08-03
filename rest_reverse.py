number = int(input("Введите число: "))
new_number = 0

started = False
while number>0:
    if started:
        new_number=new_number*10
    started = True
    digit=number%10
    new_digit = 9-digit
    new_number +=new_digit
    number=number//10

new_number = str(new_number)
new_number = new_number[::-1]
print(new_number)

