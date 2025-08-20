IDADE_MINIMA = 18

idade_usuario = input('Digite a sua idade: ')
idade_int = int(idade_usuario)

if idade_int >= IDADE_MINIMA:
    print('Você é maior de idade')
else:
    ('Você é menor de idade')