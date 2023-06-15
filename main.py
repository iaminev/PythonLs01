
# Процедура определяет, високосный год или нет
def LessonTask04LeapYear():
    year = int(input('Введите год: '))
    if year%4 == 0:
        print(f'Год {year} - високосный')
    else:
        print(f'Год {year} - НЕ високосный')

if __name__ == '__main__':
    LessonTask04LeapYear()