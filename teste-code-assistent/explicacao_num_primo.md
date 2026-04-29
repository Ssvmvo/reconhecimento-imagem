# Explicação da função de número primo

## Função: is_prime(n)

- Se o número for menor ou igual a 1, retorna False, pois não é primo
- Se for 2 ou 3, retorna True
- Se for divisível por 2, retorna False
- Depois verifica divisores ímpares até a raiz quadrada do número
- Se encontrar divisor, retorna False
- Caso contrário, retorna True

## Melhorias aplicadas

- Nome de função mais claro
- Redução de verificações desnecessárias
- Uso de lógica mais eficiente (até raiz quadrada)
- Código mais limpo e legível