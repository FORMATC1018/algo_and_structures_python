"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""
number = int(input("Введите натуральное число - "))
count_even = 0
count_odd = 0
while number!=0:
    digit = number%10
    number//=10
    if digit%2==0:
        count_even+=1
    else:
        count_odd+=1
print("У числа {} четных цифры и {} нечетных".format(count_even, count_odd))