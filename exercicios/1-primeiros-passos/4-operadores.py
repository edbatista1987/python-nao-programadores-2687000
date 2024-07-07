ano_nascimento = 1989
ano_formatura = 2010


# 1. Descubra a idade de Gerlaine no ano da sua formatura
idade_na_formatura = ano_formatura - ano_nascimento
print(idade_na_formatura)  # Resultado: 21

# 2. Escreva expressões comparativas usando os operadores relacionais >, <= e ==. Imprima na tela as respostas
print(ano_formatura > ano_nascimento)    # True, pois 2010 > 1989
print(ano_nascimento <= ano_formatura)   # True, pois 1989 <= 2010
print(ano_nascimento == ano_formatura)   # False, pois 1989 não é igual a 2010

# 3. Crie expressões comparativas mais complexas utilizando operadores lógicos and, or e not. Imprima na tela as respostas
print((ano_nascimento < ano_formatura) and (idade_na_formatura == 21))  # True, ambas as condições são verdadeiras
print((ano_nascimento > ano_formatura) or (idade_na_formatura == 21))   # True, uma das condições é verdadeira
print(not (ano_nascimento == ano_formatura))                            # True, nega a condição falsa, resultando em verdadeiro
