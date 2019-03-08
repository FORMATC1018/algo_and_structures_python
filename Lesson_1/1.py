# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
number = int(input("Введите трехзначное число "))
sum_digit = number%10 + number//100 + (number//10%10)
mult_digit = number%10 * number//100 * (number//10%10)
print ("Сумма цифр равна {}".format(sum_digit))
print ("Произведение цифр равно {}".format(mult_digit))