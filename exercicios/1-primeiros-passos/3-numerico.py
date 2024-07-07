data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

data_nascimento = '05-10-1976'
idade_numerica = 46
altura = 1.74

# Descubra o tipo de dado de cada variável
print(type(data_nascimento))  # <class 'str'>
print(type(idade_numerica))   # <class 'int'>
print(type(altura))           # <class 'float'>

# Realize uma operação entre dados do tipo string e inteiro
# Vamos repetir a string 'idade_numerica' vezes
print(data_nascimento * idade_numerica)  # Resultado: '05-10-197605-10-1976... (46 vezes)'

# Realize uma operação entre dados do tipo inteiro e float
# Vamos multiplicar idade_numerica por altura
resultado = idade_numerica * altura
print(resultado)  # Resultado: 80.04

