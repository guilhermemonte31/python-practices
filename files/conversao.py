def converter(bytes):
    tot = 1024*1024
    return bytes/tot


arq = open("files/arquivo.txt")
linhas = arq.readlines()
tot =0
cont =0
for linha in linhas:
    valor = linha[15:]
    numero = int(valor)
    mb = converter(numero)
    tot += mb
    cont += 1

    nome = linha[:15]
    print(f"{linha[:15]}{mb:.2f} MB ")

media = tot/cont
print(f"Total: {tot:.2f} MB")
print(f"Media: {media:.2f} MB")

