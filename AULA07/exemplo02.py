soma = 0
for i in range(1, 11):
    n = int(input(f"Entre com a {i}º. idade: "))
    soma = soma + n
media = soma / 10
print (f"A média das idades é {media:5.2f}")
