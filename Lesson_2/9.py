"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def sum_digit(number):
    sum=0
    while number!=0:
        last_digit = number%10
        sum+=last_digit
        number//=10
    return sum


n = int(input("Введите количество чисел - "))
maximum=0
for i in range(n):
    number = int(input("Введите число - "))
    sum = sum_digit(number)
    if sum>maximum:
        maximum=sum
        find_numb = number
print("Наибольшее по сумме цифр число - {} Сумма цифр этого числа {} ".format(find_numb, maximum))