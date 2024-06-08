# 1
# i = 1
# soma = 0
# while i <= 5:
#     print(i)
#     i = i + 1
#     soma = soma + i
# print(soma)

# 2
soma = 0
count = 0
continuar = str(input("Deseja informar números? S/N : ")).upper()
while continuar == "S":
    num = int(input("Informe um número: "))
    if num >= 0:
        soma = soma + num
    else:
        count = count + 1
    continuar = str(input("Deseja informar números? S/N : ")).upper()
print("A soma dos postivos", soma)
print("A soma dos negativos", count)