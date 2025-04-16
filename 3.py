# import stripe
# from django.conf import settings
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.db import models
# from rest_framework import serializers, viewsets
# from django.urls import path
# from rest_framework.routers import DefaultRouter

# # Stripe API kalitlari
# stripe.api_key = settings.STRIPE_SECRET_KEY

# @api_view(['POST'])
# def create_checkout_session(request):
#     try:
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'product_data': {
#                             'name': 'Premium Subscription',
#                         },
#                         'unit_amount': 5000,  # 50.00 USD
#                     },
#                     'quantity': 1,
#                 }
#             ],
#             mode='payment',
#             success_url=settings.SITE_URL + '/success/',
#             cancel_url=settings.SITE_URL + '/cancel/',
#         )
#         return JsonResponse({'sessionId': session.id})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# @api_view(['POST'])
# def verify_payment(request):
#     payload = request.body
#     sig_header = request.headers.get('Stripe-Signature')
#     endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    
#     try:
#         event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#         if event['type'] == 'checkout.session.completed':
#             session = event['data']['object']
#             print(f'Payment successful: {session}')
#         return JsonResponse({'status': 'success'})
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)

# --- Shaxsiy moliyaviy boshqaruv modeli ---
# class Transaction(models.Model):
#     TRANSACTION_TYPES = [
#         ('income', 'Income'),
#         ('expense', 'Expense'),
#     ]
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     category = models.CharField(max_length=255)
#     type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
#     date = models.DateTimeField(auto_now_add=True)

# class TransactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = '__all__'

# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer

# # Django REST router
# router = DefaultRouter()
# router.register(r'transactions', TransactionViewSet)

# urlpatterns = [
#     path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
#     path('verify-payment/', verify_payment, name='verify-payment'),
# ] + router.urls
# # import { useState, useEffect } from "react";

# export default function App() {
#   const [transactions, setTransactions] = useState([]);
#   const [amount, setAmount] = useState("");
#   const [category, setCategory] = useState("");
#   const [type, setType] = useState("income");

#   useEffect(() => {
#     fetch("http://127.0.0.1:8000/transactions/")
#       .then((res) => res.json())
#       .then((data) => setTransactions(data));
#   }, []);

#   const handleAddTransaction = () => {
#     fetch("http://127.0.0.1:8000/transactions/", {
#       method: "POST",
#       headers: {
#         "Content-Type": "application/json",
#       },
#       body: JSON.stringify({ amount, category, type }),
#     })
#       .then((res) => res.json())
#       .then((data) => setTransactions([...transactions, data]));
#   };

#   return (
#     <div className="p-5 max-w-md mx-auto">
#       <h1 className="text-xl font-bold mb-4">Moliya Boshqaruv</h1>
#       <div className="mb-4">
#         <input
#           type="number"
#           placeholder="Miqdor"
#           value={amount}
#           onChange={(e) => setAmount(e.target.value)}
#           className="p-2 border rounded w-full mb-2"
#         />
#         <input
#           type="text"
#           placeholder="Kategoriya"
#           value={category}
#           onChange={(e) => setCategory(e.target.value)}
#           className="p-2 border rounded w-full mb-2"
#         />
#         <select
#           value={type}
#           onChange={(e) => setType(e.target.value)}
#           className="p-2 border rounded w-full"
#         >
#           <option value="income">Daromad</option>
#           <option value="expense">Xarajat</option>
#         </select>
#         <button
#           onClick={handleAddTransaction}
#           className="bg-blue-500 text-white p-2 rounded w-full mt-2"
#         >
#         #  Qo'shish
#         </button>
#       </div>
#       <h2 className="text-lg font-bold mb-2">Tranzaksiyalar</h2>
#       <ul>
#         {transactions.map((t) => (
#           <li key={t.id} className="p-2 border-b">{t.category}: ${t.amount} ({t.type})</li>
#         ))}
#       </ul>
#     </div>
#   );
# }
# import threading
# import multiprocessing
# import requests
# def fetch_and_process(url):
#     response = requests.get(url)  # 1. Ma’lumot olish (I/O)
#     words = response.text.split()
#     word_lengths = [len(word) for word in words]  # 2. Matnni qayta ishlash (CPU)
#     print(f"{url} - o‘rtacha so‘z uzunligi: {sum(word_lengths) / len(word_lengths)}")
# urls = [
#     "https://example.com",
#     "https://google.com",
#     "https://github.com"
# ]
# threads = []
# for url in urls:
#     t = threading.Thread(target=fetch_and_process, args=(url,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Barcha vebsaytlar qayta ishlangan!")
#
# import requests
# url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()
#     usd = next((item for item in data if item["Ccy"] == "USD"), None)
#     if usd:
#         print(f"1 usd = {usd['Rate']} UZS ({usd['Date']})")
#     else:
#         print("USD kursi topilmadi.")
import threading
import time

# def download_data(site):
#     print(f"{site} yuklanmoqda...")
#     time.sleep(2)
#     print(f"{site} yuklab olindi!")
# threads = []
# for site in ["site1.com", "site2.com", "site3.com"]:
#     t = threading.Thread(target=download_data, args=(site,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()
# # print("Barcha yuklashlar tugadi!")
# import threading
# import time
import random

def sonni_top():
    son=random.randint(1,10)
    print(son)
    a=int(input('sonni taxmin qiling'))

    if a==son:
        print('siz sonni topdingiz')
    else:
        print('sonni topolmadingiz')

sonni_top()
