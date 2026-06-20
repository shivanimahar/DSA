def armstrong(n):
    digits = len(str(n)) #We write str(n) because len() works on strings, lists, tuples, etc. — not directly on integers.
    total = 0
    dup = n

    while n > 0:
        ld = n % 10
        total += ld ** digits #total + ld^digits
        n = n // 10

    return total == dup


num = 1645

if armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")