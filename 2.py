users={}
books = {
    1: {"title": "urush", "author": "tolstoy", "genre": "tragediya", "available": 8},
    2: {"title": "qirol lir", "author": "shekspir", "genre": "tragedya", "available": 0},
    3: {"title": "Aliakbarni sarguzashtlari", "author": "ali", "genre": "drama", "available": 1},
}
s={}
current_user=''
while True:
    print('🔑 Tizimga kirish')
    print('1. Login')
    print("2. Ro'yxatdan o'tish")
    k=input('>>> Tanlovingiz(1 yoki 2): ')
    if k=='1':
        n=input('👤 login: ')
        m=input('🔑 parol: ')
        current_user=n
        if n in users and users[n] == m:
            while True:
                print("🖼️ FOYDALANUVCHI PANELI")
                print("1. Barcha kitoblarni ko'rish")
                print("2. Kitob zakaz qilish")
                print("3. Chiqish")
                print(f'Agar boshqa bir kitob kerak bolsa {len(books)+1} tugmasini bosing')
                t=int(input())
                if t==3:
                    print("! Dastur yakunlandi")
                    break
                elif t==1:
                    print("\n📚 Kutubxona katalogi:")
                    for num, book in books.items():
                        print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                elif t==2:
                    for num, book in books.items():
                        print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                    choise=int(input(f'📖 Qaysi kitobni olishni istaysiz? (raqam) 1-{len(books)} '))
                    if choise in books and books[choise]["available"] > 0:
                        son=int(input("Nechta buyurtma qilmoqchisiz"))
                        if books[choise]["available"]>=son:
                            books[choise]["available"] -= son
                        else:
                            print("❌ Uzur bu kitobimiz soni buncha emas")
                        print(f"✅ {current_user} '{books[choise]['title']}' kitobini oldi!")
                    else:
                        print('❌ Uzur bu kitobimiz mavjud emas')
                elif t==len(books)+1:
                    nomi=input('Qaysi kitob qo\'shilishini istaysiz: ')
                    muallifi=input("Qo'shmoqchi bo'lgan kitobingizni muallifi: ")
                    janri=input("Qo'shmoqchi bo'lgan kitobingizni janri: ")
                    print('Istagingiz qabul qilindi😊')
                    s['title']=nomi
                    s['author']=muallifi
                    s['genre']=janri
        elif n=='admin' and m=='admin123':
            if len(s)>0:
                while True:
                    print("🖼️ ADMIN PANELI")
                    print("1. Barcha kitoblarni ko'rish")
                    print("2. Kitob qo'shish")
                    print("3. Chiqish")
                    print('4. Sizga taklif bor📩')
                    t=int(input())
                    if t==3:
                        print("! Dastur yakunlandi")
                        break
                    elif t==1:
                        print("\n📚 Kutubxona katalogi:")
                        for num, book in books.items():
                            print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                    elif t==2:
                        print('1.📚 Yangi kitob qoshish')
                        print('2.📚 Ba\'zi bir kitoblar sonini ko\'paytirish')
                        yangi=input('>>> Tanlovingiz (1-2): ')
                        if yangi=='1':
                            malumot={}
                            yangi_kitob=input("Yangi qo'shmoqchi bo'lgan kitobingiz: ")
                            muallif=input("Yangi qo'shmoqchi bo'lgan kitobingiz muallifi: ")
                            janr=input("Yangi qo'shmoqchi bo'lgan kitobingiz janri: ")
                            soni=input("Yangi qo'shmoqchi bo'lgan kitobingiz soni: ")
                            malumot['title']=yangi_kitob
                            malumot['author']=muallif
                            malumot['genre']=janr
                            malumot['available']=soni
                            books[len(books)+1]=malumot
                            for num, book in books.items():
                                print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                        elif yangi=='2':
                            for num, book in books.items():
                                print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                            choise=int(input(f'📖 Qaysi kitobni kopaytirishni istaysiz? (raqam) '))
                            if choise in books :
                                plus=int(input("Nechta kitob qo'shmoqchisiz: "))
                                books[choise]["available"] += plus
                            for num, book in books.items():
                                print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                    elif t==4:
                        print(f"{s['title']} - {s['author']} [{s['genre']}]")
                        soni=int(input('Nechta qo\'shmoqchisiz: '))
                        s['available']=soni
                        umumiy={len(books)+1:s}
                        books.update(umumiy)
                        for num, book in books.items():
                            print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                        print('muvoffaqiyatli qo\'shildi ✅')
                        if books[len(books)]['title'] == nomi:
                            s={}
            else:
                while True:
                    print("🖼️ ADMIN PANELI")
                    print("1. Barcha kitoblarni ko'rish")
                    print("2. Kitob qo'shish")
                    print("3. Chiqish")
                    t=int(input())
                    if t==3:
                        print("! Dastur yakunlandi")
                        break
                    elif t==1:
                        print("\n📚 Kutubxona katalogi:")
                        for num, book in books.items():
                            print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                    elif t==2:
                        print('1.📚 Yangi kitob qoshish')
                        print('2.📚 Ba\'zi bir kitoblar sonini ko\'paytirish')
                        yangi=input('>>> Tanlovingiz (1-2): ')
                        if yangi=='1':
                            malumot={}
                            yangi_kitob=input("Yangi qo'shmoqchi bo'lgan kitobingiz: ")
                            muallif=input("Yangi qo'shmoqchi bo'lgan kitobingiz muallifi: ")
                            janr=input("Yangi qo'shmoqchi bo'lgan kitobingiz janri: ")
                            soni=input("Yangi qo'shmoqchi bo'lgan kitobingiz soni: ")
                            malumot['title']=yangi_kitob
                            malumot['author']=muallif
                            malumot['genre']=janr
                            malumot['available']=soni
                            books[len(books)+1]=malumot
                            for num, book in books.items():
                                print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                        elif yangi=='2':
                            for num, book in books.items():
                                print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")
                            choise=int(input(f'📖 Qaysi kitobni kopaytirishni istaysiz? (raqam) '))
                            if choise in books :
                                plus=int(input("Nechta kitob qo'shmoqchisiz: "))
                                books[choise]["available"] += plus
                            for num, book in books.items():
                                    print(f"{num}. {book['title']} - {book['author']} [{book['genre']}] ({book['available']} available)")

        else:
            print("Avval ro'yxatdan o'ting ❌")
    else:
        n=input('👤 Yangi login: ')
        m=input('🔑 Yangi parol: ')
        users[n]=m
        print(f"✅ {n} ro'yxatdan o'tdi!")
