import random, time

koloda = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 10
random.shuffle(koloda)

vibor1 = ["СТОП", "Стоп" , "стоп"]
vibor2 = ["ЕЩЕ", "Еще" , "еще"]
soglasie = "Да"

while True:
    name_player = input("Добро пожаловать в блекджек, введите своё имя: ")
    print()
    if name_player.isalpha():
        break
    print("Неправильное имя, попробуйте снова")
    print()
print("Здравствуйте, " + name_player)

time.sleep(1)

while True:
    try:
        vozrast = int(input("Введите свой возраст: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова. ")
        print()

if vozrast < 18:
    print("Братан, тебе сюда нельзя")
    exit()
elif vozrast > 100:
    print()
    print("Твой возраст слишком большой, но мы поверим)")
    print()
else:
    print()
    print("Ищем столы...")
time.sleep(3)

stol = int(random.randint(1,100))
print("Свободно столов: " , stol)
time.sleep(1)
print("Перенаправляю...")
time.sleep(5)
print()
print("Добро пожаловать в комнату №" , random.randint(1,stol))
print()

#ПРОВЕРКА ПЛАТЕЖА
while True:
    try:
        balance = float(input("Введите депозит: "))
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова. ")

while soglasie != "ВЫХОД":
    while True:
        try:
            stavka = float(input("Введи свою ставку: "))
            if balance >= stavka and stavka > 0:
                print()
                print("Ваша ставка составила: ", stavka)
                print("Баланс: ", balance - stavka)
                break
            elif stavka <= 0:
                print("Неправильная запись")
            else:
                print("Недостаточно средств")
                continue
        except ValueError:
            print("Вы ввели не число. Попробуйте снова. ")
    print()
    print("Подготовка к игре...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Раздача карт...")
    print()

    ruka_dealer = 0
    ruka_igrok = 0

    ruka_igrok = ruka_igrok + list.pop(koloda)
    print("Твоя первая карта равна: ", ruka_igrok)
    print()

    #ПРАВИЛА ДЛЯ ИГРОКА
    while ruka_igrok < 21:
        vibor = input("Еще или Стоп? ")
        if vibor in vibor1:
            print("Твоя рука: " , ruka_igrok)
            print()
            break
        elif vibor in vibor2:
            ruka_igrok = ruka_igrok + list.pop(koloda)
            if ruka_igrok != 21:
                print("Твоя рука равна: " , ruka_igrok)
                print()
                continue
            else:
                print("У вас 21")
                print()
                break
        elif vibor != "СТОП":
            print("Неправильный ввод")
    else:
            print("Перебор, вы проиграли")
            balance = balance - stavka

    #ПРАВИЛА ДЛЯ ДИЛЕРА
    while ruka_dealer < 21 and ruka_igrok <= 21:
        if ruka_dealer < 17:
            ruka_dealer = ruka_dealer + list.pop(koloda)
            time.sleep(1)
            if ruka_dealer != 21:
                print(ruka_dealer)
                time.sleep(1)
                continue
            else:
                print(ruka_dealer)
                time.sleep(1)
                print("У дилера 21!")
                print()
                break
        elif ruka_dealer >= 17 and ruka_dealer < 21:
            print("У дилера: ", ruka_dealer)
            print()
            break
    else:
        if ruka_dealer > 21:
            print("У дилера перебор:",ruka_dealer)
            print()
            print("Ты выиграл!")
            balance = balance + stavka

    if ruka_dealer > ruka_igrok and ruka_dealer <= 21:
        print("Ты проиграл")
        time.sleep(1)
        balance = balance - stavka
    elif ruka_dealer == ruka_igrok:
        print("Ничья")
        time.sleep(1)
    elif ruka_dealer < ruka_igrok and ruka_igrok <= 21:
        print("Ты выиграл")
        time.sleep(1)
        balance = balance + stavka
    print()
    print("Твой баланс: ", balance)
    print()
    soglasie = input("Игра окончена, напишите 'ВЫХОД' для выхода или другой набор для продолжения: ")
    print()
