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
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

num2 = int(input("Vvedite chislo zhyravlikov: "))
flag = True
for i in range(num2//2):
    if i + i + i * 4 ==num2:
        print("Pite - ",i ,"Serg - ", i , "Kate - ", 4*i)
    else:
        flag = False 

if flag == False:
    print("Oni ne mogli sdelat takoe kollichestvo zhyravlei")

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#  Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
num3 = int(input("Vvedite nomer bileta: "))
sumed=0
sumother = 0
if num3 < 1000000:
    razr = 3
    while razr > 0:
        sumed += num3 %10
        num3 = num3 // 10
        razr-=1
    while num3 > 0:
        sumother += num3 %10
        num3 = num3 // 10
    if sumed == sumother:
        print("Schaslivii bilet! Urra")
    else:
        print("Ne povezlo")
else:
    print("Ne nomer bileta")
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Vvedite visoty shokolada: "))
m = int(input("Vvedite dliny shokolada: "))
k = int(input("Vvedite kolichest dolek dly delenia: "))
if ((k >= n or k >= m) and k < n*m) and (k % n == 0 or k % m == 0):
    print("mozhno")
else:
    print("nelzy")
    