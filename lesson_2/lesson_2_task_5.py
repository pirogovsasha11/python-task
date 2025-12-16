def month_to_season(m):
    if m in (1,2,12):
        return "ЗИМА"
    elif m in (3,4,5):
        return "ВЕСНА"
    elif m in (6,7,8):
        return "ЛЕТО"
    elif m in (9,10,11):
        return "ОСЕНЬ"
    else:
        return "Некорректный номер месяца"

m = int(input("Введите номер месяца: "))
print(month_to_season(m))