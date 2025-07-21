# compound_interest.py: Compute compound interest (P, R, T).  CI=P(1+i)^n −P
principal = 1000
rate = 0.05
time = 10
n = 12

amount = principal * (1 + rate / n) ** (n * time)
print(amount)


