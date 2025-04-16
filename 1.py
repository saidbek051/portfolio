# with open('salom.txt','w') as myfile:
#     myfile.write('Saidbek')
#     print('ishladi')
# l=[' Sodiqov\n','on besh yoshda\n','Shuhratovich']
# with open('salom.txt','a') as myfile:
#     myfile.writelines(l)
# with open('salom.txt','w') as myfile:
#     print("Men yosh dasturchiman",file=myfile)
# with open("salom.txt", "r") as myfile:
#     str1 = myfile.readline()
#     print(str1, end="")  
#     str2 = myfile.readline()
#     print(str2)
# import csv
# FILENAME = "users.csv"
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34]
# ]
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     writer = csv.writer(file)
#     writer.writerow(user)
# import csv
# FILENAME = "users.csv"
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34]
# ]
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     reader.readrows(users)
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     reader = csv.reader(file)
#     reader.readrow(user)
# import csv
# FILENAME = "users2.csv"
# users = [
#     {"name": "Tom", "age": 28},
#     {"name": "Alice", "age": 23},
#     {"name": "Bob", "age": 34}
# ]
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()  # Ustun sarlavhalarini yozish
#     writer.writerows(users)  # Bir nechta qator yozish
#     user = {"name": "Sam", "age": 41}
#     writer.writerow(user)  # Bitta qator qo‘shish
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], "-", row["age"])
# import pickle
# FILENAME = "user.dat"
# name = "Tom"
# age = 19
# # Obyektlarni faylga yozish
# with open(FILENAME, "wb") as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
# # Obyektlarni fayldan o‘qish
# with open(FILENAME, "rb") as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     print("Ism:", name, "\tYosh:", age)
# import json
# data = {
#     "ism": "Ali",
#     "yosh": 25,
#     "shahar": "Toshkent",
#     "talaba": True
# }
# json_data = json.dumps(data)  
# print(json_data)
# import json
# json_text = '{"ism": "Ali", "yosh": 25, "shahar": "Toshkent"}'
# python_data = json.loads(json_text)
# print(python_data["ism"])  # Ali
# print(python_data["yosh"])
# s = [
#     {'ID': 1, 'Ism': 'Ali', 'Fan': 'Mathematics', 'Baho': 85},
#     {'ID': 2, 'Ism': 'Vali', 'Fan': 'Physics', 'Baho': 90},
#     {'ID': 3, 'Ism': 'Hasan', 'Fan': 'Computer Science', 'Baho': 95}
# ]

# def aniqla(k):
#     if k==1:
#         for i in s:
#             print(i)
#     elif k==2:
#         id=len(s)+1
#         ism=input("Qo'shmoqchi bo'lgan talabangizni ismi: ")
#         fan=input("Qo'shmoqchi bo'lgan talabangizni fani: ")
#         baho=input("Qo'shmoqchi bo'lgan talabangizni bahosi: ")
#         royxat={'ID':id,'Ism':ism,'Fan':fan,'Baho':baho}
#         s.append(royxat)
#     elif k==3:
#         id=int(input("Qidirmoqchi bo'lgan talabangizni id si: "))
#         if len(s)>=id:
#             print(s[id-1])
#         else:
#             print("Bu talaba ro'yxatda yo'q")
#     elif k==4:
#         id=int(input("Bahosini o'zgartirmoqchi bo'lgan talabangizni id si: "))
#         if len(s)>=id:
#             baho1=int(input("Bahosini kiriting: "))
#             s[id-1]['Baho']=baho1
#         else:
#             print("Bu talaba ro'yxatda yo'q")
#     elif k==5:
#         id=int(input("O'chirmoqchii bo'lgan talabangizni id si: "))
#         if len(s)>=id:
#             del s[id-1]
#         else:
#             print("Bu talaba ro'yxatda yo'q")
# while True:
#     k=int(input('Tanlovni kiriting: '))
#     if k==6:
#         break
#     aniqla(k)
import random
new=['+','-','/','*']
s,k=0,0
while True:
    s1=random.randint(1,10)
    s2=random.randint(1,10)
    amal=random.choice(new)
    if amal=='+':
        ans=s1+s2
    elif amal=='-':
        ans=s1-s2
    elif amal=='//':
        ans=s1//s2
    elif amal=='*':
        ans=s1*s2
    print(f"{s1}{amal}{s2}")
    user=input()
    if user=='stop':
        break
    if int(user)==ans:
        s+=1
    else:
        k+=1
    if s==5 or k==5:
        if s>k:
            print('siz g\'olib bo\'ldingiz')
        else:
            print('siz mag\'olib bo\'ldingiz')
        break
# oquvchilar = ["Ali", "Vali", "Laylo", "Mavluda"]
# reytinglar={
#     'Ali':(5,4,4),
#     'Vali':(4,4,5),
#     'Laylo':(5,4,5),
#     'Mavluda':(5,5,4)
# }
# tugilgan_kunlar={
#     'Ali':'04-06-2010',
#     'Vali':'03-09-2008',
#     'Laylo':'23-01-2006',
#     'Mavluda':'29-01-2010'
# }
# qatnashuvchilar={'Laylo'}
# yangi_oquvchi='Dilshod'
# yangi_tugilgan_kun='21-11-2005'
# oquvchilar.append(yangi_oquvchi)
# reytinglar[yangi_oquvchi]=(0,0,0)
# tugilgan_kunlar[yangi_oquvchi]=yangi_tugilgan_kun
# ochiriladigan_oquvchi='Vali'
# oquvchilar.remove(ochiriladigan_oquvchi)
# reytinglar.pop(ochiriladigan_oquvchi)
# tugilgan_kunlar.pop(ochiriladigan_oquvchi)
# for i in oquvchilar:
#     baholar=reytinglar.get(i,(0,0,0))
#     ortacha=sum(baholar)/len(baholar)
#     if ortacha>=4.5:
#         print(f'{i}ning natijalari alo')
#     elif 4.5>ortacha>=4.0:
#         print(f'{i}ning natijalari yaxshi')
#     else:
#         print(f'{i}ning natijalari yomon')
# for n,m in tugilgan_kunlar.items():
#     print(f"{n}: {m}")
# darsga_qatnashgan='Dilshod'
# darsga_kelmagan='Ali'
# qatnashuvchilar.add(darsga_qatnashgan)
# qatnashuvchilar.discard(darsga_kelmagan)
# print(qatnashuvchilar)
# meva=['olma','anor','nok']
# narx=[500,600,700]
# bog=list(zip(meva,narx))
# new={}
# for l,n in enumerate(bog):
#     new[n]=l
# print(new)
# def aniqla(n,k):
#     if all([len(n)<3,k>20]):
#         return 'Siz yoshi katta yapon ekansiz'
#     elif any([len(n)<3,k>20]):
#         return 'Siz yapon ekansiz'
#     else:
#         return 'Tanimadim'
# n=input('Ismingiz:')
# k=int(input('Yoshingiz:'))
# print(aniqla(n,k))
# def tashqi():
#     son=5
#     def ichki():
#         nonlocal son
#         son-=1
#         return son
#     return ichki
# k=tashqi()
# print(k())
# print(k())
# print(k())
# print(k())
# print(k())

# def decorater_nomi(k):
#     def wrapper:
#         if k%2:
#             k+=5
#             return k
#         else:
#             return k
# k=int(input())
# javob=decorater_nomi(k)
# print(javob)
# def fun(f,x):
#     return f(x)
# def squ(x):
#     return x*x
# res=fun(squ,5)
# print(res)
# try:
#     n=int(input())
#     if n<0:
#         #raise ValueError('Faqat musbat son kiriting!: ')
#         pass
# except ValueError as e:
#     print(f'Kiritishda xatolik: {e}')
# else:
#     print('Raxmat')
# finally:
#     print('Tugadi')
# def age_weight(age,weight):
#     if age<0 and weight<20:
#         raise ValueError('Age cannot be negative ')
#     print(f"{age}")
# try:
#     age=int(input('Yoshingiz: '))
#     weight=int(input('VAzninggiz: '))
# except ValueError as e:
#     print(e)
# with open('salom.txt','w') as myfile:
#     myfile.write('Saidbek')
#     print('ishladi')
# l=[' Sodiqov\n','on besh yoshda\n','Shuhratovich']
# with open('salom.txt','a') as myfile:
#     myfile.writelines(l)
# with open('salom.txt','w') as myfile:
#     print("Men yosh dasturchiman",file=myfile)
# with open("salom.txt", "r") as myfile:
#     str1 = myfile.readline()
#     print(str1, end="")  
#     str2 = myfile.readline()
#     print(str2)
# import csv
# FILENAME = "users.csv"
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34]
# ]
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     writer = csv.writer(file)
#     writer.writerow(user)
# import csv
# FILENAME = "users.csv"
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34]
# ]
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.reader(file)
#     reader.readrows(users)
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     reader = csv.reader(file)
#     reader.readrow(user)
# import csv
# FILENAME = "users2.csv"
# users = [
#     {"name": "Tom", "age": 28},
#     {"name": "Alice", "age": 23},
#     {"name": "Bob", "age": 34}
# ]
# with open(FILENAME, "w", newline="") as file:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(file, fieldnames=columns)
#     writer.writeheader()  # Ustun sarlavhalarini yozish
#     writer.writerows(users)  # Bir nechta qator yozish
#     user = {"name": "Sam", "age": 41}
#     writer.writerow(user)  # Bitta qator qo‘shish
# with open(FILENAME, "r", newline="") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["name"], "-", row["age"])
# import pickle
# FILENAME = "user.dat"
# name = "Tom"
# age = 19
# # Obyektlarni faylga yozish
# with open(FILENAME, "wb") as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
# # Obyektlarni fayldan o‘qish
# with open(FILENAME, "rb") as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     print("Ism:", name, "\tYosh:", age)
import random
s,k=0,0
a=['left','right','center']
while True:
    n=input()
    m=random.choice(a)
    if n=='stop':
        break
    s+=1
    if n==m:
        print(f'top qaytarildi')
    else:
        k+=1
        print('gol')
    if s==10:
        break
print(f'{k} ta gol va {s-k} ta urolmadingiz')
#1
g={'Ali':87,'Vali':92,'Hasan':78,'Husan':95,'Gulnoza':89}
s,k=[],[]
for i in g:
    s.append(i)
    k.append(g[i])
print(s[k.index(max(k))],max(k))
#2
a=list(map(int,input().split()))
s=[]
for i in a:
    if a.couunt(i)==1:
        s.append(i)
print(s)

#3
students = {
    "Ali": ("Matematika", 90),
    "Vali": ("Fizika", 85),
    "Hasan": ("Kimyo", 92)
}
for i,(n,m) in students.items():
    print(f"{i} {n} fanidan {m} ball oldi")

#4
ages = {"Ali": 24, "Vali": 17, "Hasan": 19, "Husan": 16, "Gulnoza": 22}
for i in ages:
    if ages[i]<18:
        print(i)
#5
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(set1.union(set2))
#6
products = {
    "un": (50, 10000),
    "shakar": (30, 15000),
    "yog'": (20, 25000),
    "choy": (10, 8000)
}
for i,(n,m) in products.items():
    if n<30:
        print(i)
#7
n,m=[],[]
students = {
    "Ali": [80,85,90],
    "Vali": [70,75,72],
    "Hasan": [92,95,98],
    "Husan": [60,65,55],
    "Gulnoza": [88,90,92]
}
for _ ,[i,j,k] in students.items():
    s=(i+j+k)/3
    if s>=85:
        n.append(_)
    elif s<70:
        m.append(_)
print(f"{n} alochi oquvchilar")
print(f"{m} takroriy dars kerak")
#8
a=[]
tickets = [
    ("Ali", "Toshkent", "Istanbul", 1000000),
    ("Vali", "Toshkent", "Moskva", 1200000),
    ("Hasan", "Samarqand", "Istanbul", 950000),
    ("Husan", "Toshkent", "Istanbul", 1100000),
    ("Gulnoza", "Buxoro", "Moskva", 1300000),
]
s=sum(1 for p in tickets if p[1] == "Toshkent" and p[2] == "Istanbul")  
k=[p[0] for p in tickets if p[3] > 1000000]
l=[p[3] for p in tickets]
print(s)
print(k)
print(max(l))
a=int(input())
korzinka={'cola':15000,'olma':18000,'shakar':21000,'non':3000}
l=[]
s=0
for i in range(a):
    n=input()
    l.append(n)
for j in l:
    if j in korzinka:
        s+=korzinka[n]
print(s)
# #1
# def max_son(sonlar):
#     if len(sonlar)>0:
#         print(max(sonlar))
#     else:print("Hech qanday son yo'q")
# sonlar=list(map,input().split())
# max_son(sonlar)
# #2
# def tugallangan_mahsulotlar(royxat):
#     print([m for m in royxat if m.get('status') == 'tugallangan'])
# royxat=list(map(str,input().split()))
# tugallangan_mahsulotlar(royxat)
# #3
# def yigindi(sonlar):
#     if len(sonlar)>0:print(sum(sonlar))
#     else:print("Hech qanday son yo'q")
# sonlar=list(map(int,input().split()))
# yigindi(sonlar)
# #4
# def farq(a,b):
#     farq = abs(a - b)
#     print(farq)
# a,b=map(int,input().split())
# farq(a,b)
# #5
# def umumiy_narx(narxlar):
#     print( sum(narxlar) if len(narxlar)>0 else "Hech qanday narx yo'q")
# narxlar=list(map(int,input().split()))
# umumiy_narx(narxlar)
# #6
# def juft_yoki_toq(a):
#     print("Juft" if a % 2 == 0 else "Toq")
# a=int(input())
# juft_yoki_toq(a)
# #7
# def narx_nisbati(a,b):
#     if a == 0 and b == 0:
#         print('Narx nolga teng')
#     print( a / b if b != 0 else "Bo'lish mumkin emas")
# a,b=map(int,input().split())
# narx_nisbati(a,b)
# #8
# def ajratish(sonlar):
#     musbat = [s for s in sonlar if s > 0]
#     manfiy = [s for s in sonlar if s < 0]
#     print(musbat)
#     print(manfiy)
# sonlar=map(int,input().split())
# ajratish(sonlar)
# #9
# def mahsulot_bormi(s,a):
#     if a in s:
#         print('Bor')
#     else:
#         print('Yoq')
# s=list(map(str,input().split()))
# mahsulot_bormi(s,a)
# #10
# def juft_sonlar(n):
#     print([i for i in range(2, n+1, 2)])
# n=int(input())
# juft_sonlar(n)
# import random
# new=['+','-','/','*']
# s,k=0,0
# while True:
#     s1=random.randint(1,10)
#     s2=random.randint(1,10)
#     amal=random.choice(new)
#     if amal=='+':
#         ans=s1+s2
#     elif amal=='-':
#         ans=s1-s2
#     elif amal=='//':
#         ans=s1//s2
#     elif amal=='*':
#         ans=s1*s2
#     print(f"{s1}{amal}{s2}")
#     user=input()
#     if user=='stop':
#         break
#     if int(user)==ans:
#         s+=1
#     else:
#         k+=1
#     if s==5 or k==5:
#         if s>k:
#             print('siz g\'olib bo\'ldingiz')
#         else:
#             print('siz mag\'olib bo\'ldingiz')
#         break

# a=input()
# sale=int(input())
# price=float(input())
# print(f'Umumiy sorilgan {a} lar soni {sale} ta har bir {a} {price} somdan turadi jami daromad esa {price*sale}')

# import random
# s,k=0,0
# a=['left','right','center']
# while True:
#     n=input()
#     m=random.choice(a)
#     if n=='stop':
#         break
#     s+=1
#     if n==m:
#         print(f'top qaytarildi')
#     else:
#         k+=1
#         print('gol')
#     if s==10:
#         break
# print(f'{k} ta gol va {s-k} ta urolmadingiz')
# #1
# g={'Ali':87,'Vali':92,'Hasan':78,'Husan':95,'Gulnoza':89}
# s,k=[],[]
# for i in g:
#     s.append(i)
#     k.append(g[i])
# print(s[k.index(max(k))],max(k))
# #2
# a=list(map(int,input().split()))
# s=[]
# for i in a:
#     if a.couunt(i)==1:
#         s.append(i)
# print(s)

# #3
# students = {
#     "Ali": ("Matematika", 90),
#     "Vali": ("Fizika", 85),
#     "Hasan": ("Kimyo", 92)
# }
# for i,(n,m) in students.items():
#     print(f"{i} {n} fanidan {m} ball oldi")

# #4
# ages = {"Ali": 24, "Vali": 17, "Hasan": 19, "Husan": 16, "Gulnoza": 22}
# for i in ages:
#     if ages[i]<18:
#         print(i)
# #5
# set1 = {1, 2, 3, 4, 5, 6}
# set2 = {4, 5, 6, 7, 8, 9}
# print(set1.union(set2))
# #6
# products = {
#     "un": (50, 10000),
#     "shakar": (30, 15000),
#     "yog'": (20, 25000),
#     "choy": (10, 8000)
# }
# for i,(n,m) in products.items():
#     if n<30:
#         print(i)
# #7
# n,m=[],[]
# students = {
#     "Ali": [80,85,90],
#     "Vali": [70,75,72],
#     "Hasan": [92,95,98],
#     "Husan": [60,65,55],
#     "Gulnoza": [88,90,92]
# }
# for _ ,[i,j,k] in students.items():
#     s=(i+j+k)/3
#     if s>=85:
#         n.append(_)
#     elif s<70:
#         m.append(_)
# print(f"{n} alochi oquvchilar")
# print(f"{m} takroriy dars kerak")
# #8
# a=[]
# tickets = [
#     ("Ali", "Toshkent", "Istanbul", 1000000),
#     ("Vali", "Toshkent", "Moskva", 1200000),
#     ("Hasan", "Samarqand", "Istanbul", 950000),
#     ("Husan", "Toshkent", "Istanbul", 1100000),
#     ("Gulnoza", "Buxoro", "Moskva", 1300000),
# ]
# s=sum(1 for p in tickets if p[1] == "Toshkent" and p[2] == "Istanbul")  
# k=[p[0] for p in tickets if p[3] > 1000000]
# l=[p[3] for p in tickets]
# print(s)
# print(k)
# print(max(l))
# a=int(input())
# korzinka={'cola':15000,'olma':18000,'shakar':21000,'non':3000}
# l=[]
# s=0
# for i in range(a):
#     n=input()
#     l.append(n)
# for j in l:
#     if j in korzinka:
#         s+=korzinka[n]
# print(s)