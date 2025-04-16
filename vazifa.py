# # import time
# # from multiprocessing import Process

# # students = ["ali", "vali", "sami", "lola", "dina"]

# # def print_students():
# #     print("Talabalar ro'yxati chiqarilmoqda...")
# #     time.sleep(2)
# #     for i in students:
# #         print(i)

# # def print_capitalized_students():
# #     time.sleep(4) 
# #     print("Har bir talaba ismi bosh harf bn chiqarilmoqda...")
# #     time.sleep(2)
# #     for i in students:
# #         print(i.capitalize())

# # if __name__ == "__main__":
# #     p1 = Process(target=print_students)
# #     p2 = Process(target=print_capitalized_students)

# #     p1.start()
# #     p2.start()

# #     p1.join()
# #     p2.join()




# # class Product:
# #     def __init__(self, name, price, quantity):
# #         self.name = name
# #         self.price = price
# #         self.quantity = quantity

# # class ShoppingCart:
# #     def __init__(self):
# #         self.products = []

# #     def add_product(self, dish):
# #         self.products.append(dish)
# #         print(f"{dish.name} menyuga qo'shildi")

# #     def remove_product(self, name_product):
# #         for product in self.products:
# #             if product.name.lower() == name_product.lower():
# #                 self.products.remove(product) 
# #                 print(f"{product.name} menyudan o'chirildi")
# #                 break
# #         else:
# #             print(f"{name_product} menyuda topilmadi")

# #     def calculate_total(self):
# #         total = sum(d.price * d.quantity for d in self.products)
# #         return total

# # obj = Product('sok', 45000, 24)
# # obj1 = Product('olma', 23000, 32)

# # cart = ShoppingCart()
# # cart.add_product(obj)
# # cart.add_product(obj1)

# # print("Jami summa:", cart.calculate_total())

# # cart.remove_product('olma')
# # print("Yangi summa:", cart.calculate_total())






















# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity

# class ShoppingCart:
#     def __init__(self):
#         self.products=[]

#     def add_product(self,product):
#         self.products.append(product)
#         print(f"{product.name} menyuga qoshildi")

#     def remove_product(self,name_product):
#         for product in self.products:
#             if product.name.lower()==name_product.lower():
#                 self.products.remove(product)
#                 print(f"{name_product} menyudan ochirildi")
#                 break

#         else:
#             print(f"{name_product} menyudan topilmadi")

#     def calculate_total(self):
#         total=sum(d.price*d.quantity for d in self.products)
#         return total

# obj=Product('sok',45000,24)
# obj1=Product('ruchka',4000,34)
                
# cart=ShoppingCart()
# cart.add_product(obj)
# cart.add_product(obj1)

# print("Jami summa :", cart.calculate_total())

# cart.remove_product('sok')
# print("Yangi summa:",cart.calculate_total())

# s = "abcabcbb"
# k=0
# son=[]
# for i in range(len(s)):
#     if s[i]!=s[i+1] :
#         k+=1
#     else:
#         son.append(k)
#         k=0
# print(max(son))
x = 2.00000
n = -2
print("{:.5f}".format(pow(x,n)))