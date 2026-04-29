def calcular_soma_e_media(numeros):
    """
    Calcula a soma e a média de uma lista de números.
    """
    soma = sum(numeros)
    media = soma / len(numeros)
    return {"soma": soma, "media": media}


numeros = [10, 20, 30, 40]
resultado = calcular_soma_e_media(numeros)

print(f"Soma: {resultado['soma']}")
print(f"Média: {resultado['media']}")