age_str = input('Digite a sua idade: ')
try:
    age_int = int(age_str)
    if age_int >= 18:
        print('Você é maior de idade')
    else:
        print('Você é menor de idade')
except ValueError:
    print('Valor inválido. Por favor digite um número para a sua idade.')