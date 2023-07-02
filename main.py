# Найдите сумму цифр трехзначного числа.

num1 = int(input("Vvedite chislo: "))
sum1 = 0
if num1 > 99 and num1 < 1000:
    while num1 > 0:
        ost = num1 % 10
        sum1 += ost
        num1 = num1 // 10
    
    print(sum1)
else:
    print("Error, vvedite pravilnoe chislo")
