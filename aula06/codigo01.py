import random

semaforo = random.choice(['vermelho', 'amarelo', 'verde'])

if semaforo == 'vermelho':
    print('Não passa...')
elif semaforo == 'amarelo':
    print('Pode passar, com cuidado...')
else:
    print('Pode passar...')