
'''Процедура определяет, високосный год или нет
в соответствии с григорианским календарем, год является
високосным, если его номер кратен 4, но не кратен
100, а также если он кратен 400.
'''
def LessonTask04LeapYear():
    print("Выясняем, является год високосным или нет")
    year = int(input('Введите год: '))

    if (year%400 == 0) | ((year%4 == 0) & (year%100 != 0)):
        print(f'Год {year} - високосный')
    else:
        print(f'Год {year} - НЕ високосный')
    print("\n")

'''Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''
def SumOfDigits():
    print("Задача 2: Найдем сумму цифр трехзначного числа.")
    number = int(input("Введите 3-х значное (а можно и любое) число: "))
    temp_number = number
    sum = 0
    result_string=''
    while temp_number > 0:
        sum += temp_number % 10
        result_string = str(temp_number % 10) + ('' if result_string =='' else ' + ') + result_string
        temp_number = temp_number // 10
    print(f'{number} -> {sum} ({result_string})')
    print("\n")

'''
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
'''
def PaperCranes():
    print("Задача 4: Дети делают журавликов.")
    #пусть Петя и Сережа сделали по Х журавликов
    #тогда Катя сделала (Х+Х)*2
    #и общее количество будет Х + Х + (Х+Х)*2 = 6Х,
    #то есть количество журавликов должно делиться нацело на 6, иначе у задачи нет решения
    number = int(input("Введите общее количество журавликов: "))
    if number % 6 != 0:
        print("У задачи нет решения, но Катя все равно сделала больше всех мальчиков вместе взятых")
    else:
        x = number / 6
        print(f'Петя: {x:.0f},  Катя: {4*x:.0f}, Сережа: {x:.0f}')
    print("\n")

'''
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
'''
def LuckyTicket():
    print("Задача 6: Счастливый билетик.")
    ticket_number = int(input("Введите номер билета (6 цифр): "))
    temp_number = ticket_number
    sum1 = 0
    sum2 = 0

    count = 0
    while count < 3:
        sum1 += temp_number % 10
        temp_number = temp_number // 10
        count+=1

    count=0
    while count < 3:
        sum2 += temp_number % 10
        temp_number = temp_number // 10
        count+=1

    if sum1 == sum2:
        print(f'Билетик {ticket_number} можно скушать ({sum2} = {sum1})')
    else:
        print(f'Билетик {ticket_number} не стоит скушать ({sum2} не равно {sum1})')
    print("\n")

def LuckyTicket2():
    print("Задача 6: Счастливый билетик (2-й способ).")
    ticket_number = input("Введите номер билета(любое количество цифр; их количество должно быть четным) : ")
    number_of_digits = len(ticket_number)

    sum1 = 0
    sum2 = 0

    count = 0
    if len(ticket_number) %2 != 0:
        print("Введен неправильный номер билета.")
    else:
        for digit in ticket_number:
            if count < number_of_digits/2:
                sum1+=int(digit)
            else:
                sum2+=int(digit)
            count+=1
        if sum1 == sum2:
            print(f'Билетик {ticket_number} можно скушать: ({sum2} = {sum1})')
        else:
            print(f'Билетик {ticket_number} не стоит кушать: ({sum2} не равно {sum1})')
    print("\n")

'''
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no
'''
def Chocolate():
    print("Задача 8: Делим шоколадку.")
    chocolate_height = int(input("Введите высоту шоколадки в дольках: "))
    chocolate_width  = int(input("Введите ширину шоколадки в дольках: "))
    number_of_pieces = int(input("Введите количество долек: "))

    #от шоколадки по прямой линии можно отломить кратное любой из сторон количество долек
    #например, от шоколадки 5х3 можно отломить следующие куски: 5*1=5, 5*2=10 и 3*1=3, 3*2=6, 3*3=9 и 3*4=12
    #то есть, если количество отламываемых долек делится без остатка на любую из сторон, задача решаема.
    #причем, отламываемое количество должно быть меньше общего количества долек

    if chocolate_height*chocolate_width < number_of_pieces:
        print(f'Нельзя отломить так много!')
    else:
        can_be_divided = (number_of_pieces % chocolate_width == 0) | (number_of_pieces % chocolate_height == 0)
        if can_be_divided:
            print(f'От шоколадки размером {chocolate_height}*{chocolate_width} можно отломить {number_of_pieces} дольки ')
        else:
            print(f'От шоколадки размером {chocolate_height}*{chocolate_width} нельзя отломить {number_of_pieces} дольки ')
    print("\n")

if __name__ == '__main__':
    LessonTask04LeapYear()
    SumOfDigits()
    PaperCranes()
    LuckyTicket()
    LuckyTicket2()
    Chocolate()