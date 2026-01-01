balans = 100_000

while True:
    print("\n1. Balansni ko‘rish")
    print("2. Pul qo‘shish")
    print("3. Pul yechish")
    print("4. Chiqish")

    tanlov = input("Tanlang: ")

    if tanlov == "1":
        print("Balans:", balans)

    elif tanlov == "2":
        summa = int(input("Summa: "))
        balans += summa
        print("✅ Pul qo‘shildi")

    elif tanlov == "3":
        summa = int(input("Summa: "))
        if summa <= balans:
            balans -= summa
            print("✅ Pul yechildi")
        else:
            print("❌ Mablag‘ yetarli emas")

    elif tanlov == "4":
        print("Dastur tugadi")
        break

    else:
        print("❌ Noto‘g‘ri tanlov")
