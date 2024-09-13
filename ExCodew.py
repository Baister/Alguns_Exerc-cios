#Par ou ímpar

num = int(input())
def par_ou_impar(num):
    if num % 2 == 1:
        return "Ímpar"
    else:
        return "Par"
print(f"O resultado é {par_ou_impar(num)}")