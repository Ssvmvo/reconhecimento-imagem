# Análise da Refatoração

## Problemas no código original:

- Nome da função "calc" não é descritivo
- Uso de range(len(lista)) desnecessário
- Variáveis com nomes genéricos (s, l)
- Retorno sem estrutura clara (tupla)
- Sem documentação

## Melhorias aplicadas:

- Nome da função mais claro: calcular_soma_e_media
- Uso da função sum() para simplificar
- Variáveis mais descritivas
- Retorno em formato de dicionário
- Adição de docstring
- Código mais legível e organizado