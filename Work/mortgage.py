# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
while principal > 0:
    real_payment = payment + 1000 if month <= 12 else payment
    principal = principal * (1+rate/12) - real_payment
    total_paid = total_paid + real_payment
    month += 1

print('Total paid', total_paid)
