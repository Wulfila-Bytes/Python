IDADE_MINIMA = 18

idade_usuario = input('Digite a sua idade: ')
idade_int = int(idade_usuario)

if idade_int >= IDADE_MINIMA:
    print('O usuário é maior de idade')
elif idade_int == 16 or 17:
    print('O usuário é menor de idade e tem 16 ou 17 anos')
else:
    ('O usuário é menor de idade')