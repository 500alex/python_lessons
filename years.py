age = input("Введите колличество лет: ")

while True:
    if age.isdigit():
        age = int(age)
        break
    else:
        age = input("Введите колличество лет: ")


if (age % 10 == 1) and (age % 100 != 11):
    print(age, "год")
elif (age % 10 > 1) and (age % 10 < 5) and (age % 100 != 12) and (age % 100 != 13) and (age % 100 != 14):
    print(age, "года")
else:
    print(age, "лет")
