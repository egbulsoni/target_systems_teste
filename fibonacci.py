def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def pertence_fibo(n):
    for i in range(n + 1):
        if fibo(i) == n:
            return True
    
    return False


# print(fibo(0))
# print(fibo(1))
# print(fibo(2))
# print(fibo(3))
# print(fibo(4))
# print(fibo(5))


# print(pertence_fibo(5))
# print(pertence_fibo(6))
# print(pertence_fibo(7))
# print(pertence_fibo(13))

n = input("Digite um número para saber se ele pertence ao fibonacci: ")
if pertence_fibo(n):
    print(f"O número {n} está contido na sequencia de fibonacci")
else:
    print(f"O número {n} não está contido na sequencia de fibonacci")