"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

number = int(input("Введите число - "))
rotate_number = 0 
while number>0:
    rotate_number = rotate_number*10 + number%10
    number //=10
print("Перевернутое число {}".format(rotate_number))