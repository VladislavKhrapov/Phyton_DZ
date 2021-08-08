percent = int(input('Введите число процента: '))
if percent % 100 in (11, 12, 13, 14):
    print(percent, "Процентов")
elif percent % 10 in (0, 5, 6, 7, 8, 9):
    print(percent, "Процентов")
elif percent % 10 in (2, 3, 4):
    print(percent, "Процента")
else:
    print(percent, "Процент")
