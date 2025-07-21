# compound_interest.py: Compute compound interest (P, R, T).  CI=P(1+i)^n −P
compound_interest.pyp = float(input("Enter principal: "))
r = float(input("Enter rate of interest (in decimal): "))
t = int(input("Enter time (years): "))
n = int(input("Compounded how many times per year? "))

amount = p * (1 + r / n) ** (n * t)
print("Compound Interest:", round(amount - p, 2))
print("Final Amount:", round(amount, 2))
principal = 1000
rate = 0.05
time = 10
n = 12

amount = principal * (1 + rate / n) ** (n * time)
print(amount)


