def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            print("Not Prime")
    if is_prime:
        print("Prime")
n = int(input("Number: "))
prime_checker(number = n)
