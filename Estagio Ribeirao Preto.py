'''Escolhi a linguagem python para poder resolver os problemas dados'''

''' 1 '''

Soma = 0
Indice = 13
K = 0

for K in range(1, Indice + 1):
    Soma = Soma + K

print(Soma)

''' 2 '''

def pertence_fibonacci(x):
    a, b = 0, 1

    while a <= x:
        if a == x:
            return True
        a, b = b, a + b

    return False

numero_informado = int(input("Informe um numero: "))

if pertence_fibonacci(numero_informado):
    print(f'O número {numero_informado} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero_informado} não pertence à sequência de Fibonacci.')

''' 3 Essa questao não envolve codigos apenas lógica mesmo'''

# a) A lógica é adicionar 2 ao número anterior. O próximo número é 9.

# b) A lógica é multiplicar o número anterior por 2. O próximo número é 128.

# c) A lógica é elevar o número anterior ao quadrado. O próximo número é 49.

# d) A lógica não é uma sequência de quadrados perfeitos. O próximo número seria 100.

# e) A lógica é a sequência de Fibonacci. O próximo número é 13 (8 + 5).

# f) A lógica é adicionar o próximo número primo à sequência. O próximo número é 23.

''' 4 tambem não envolve codigos apenas lógica '''

# Primeira ida:Ligando o primeiro interruptor e esperando alguns minuto depois desligando o primeiro interruptor e ligando o segundo
# após isso entraria na sala das lampadas.

# Segunda ida: Observaria as lampadas acesas se a lâmpada está acesa, o interruptor controlado pelo primeiro interruptor é o responsável por ela.
# se a lâmpada está apagada, toque a lâmpada para verificar a temperatura e com isso temos 3 casos, a lâmpada que está acesa foi controlada pelo segundo interruptor.
# a lâmpada que está apagada e quente foi controlada pelo terceiro interruptor.
# a lâmpada que está apagada e fria foi controlada pelo primeiro interruptor.

''' 5 '''

def inverter_string(original):
    string_invertida = ""
    for char in original:
        string_invertida = char + string_invertida
    return string_invertida

# Exemplo de uso
string_original = "Estágio Ribeirão Preto"
string_invertida = inverter_string(string_original)

print(f'String original: {string_original}')
print(f'String invertida: {string_invertida}')