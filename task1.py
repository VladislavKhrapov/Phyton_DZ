seconds = int(input("Введите количество секунд:  "))
days = seconds // (60 * 60 * 24)
hours = (seconds - days * (60 * 60 * 24)) // (60 * 60)
minutes = (seconds - days * (60 * 60 * 24) - hours * (60 * 60)) // 60
remainder = seconds - days * (60 * 60 * 24) - hours * (60 * 60) - minutes * 60
print("Дней: ", days, "часов: ", hours, "минут: ", minutes, "секунд: ", remainder)