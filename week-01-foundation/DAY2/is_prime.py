# 1. Checking prime number or not
def is_prime(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

is_prime(7)
is_prime(9)
is_prime(11)
is_prime(1)
is_prime(6)



