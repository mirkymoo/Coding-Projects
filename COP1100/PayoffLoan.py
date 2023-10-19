loan = float(input())
payment_amount = float(input())
interest_rate = float(input())
num_payments = 0

while loan > 0:
    loan += loan * interest_rate
    loan -= payment_amount
    num_payments += 1

if num_payments > 1:
    print(num_payments, "payments")
else:
    print(num_payments, "payment")