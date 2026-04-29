def calc(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s, s/len(l)

lista = [10, 20, 30, 40]
resultado = calc(lista)
print(resultado)