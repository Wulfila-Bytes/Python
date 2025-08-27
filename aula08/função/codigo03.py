def funcao():
    pass

def soma():
    print(5 + 5)

soma()


def somar(x, y):
    print(x + y)

somar(5, 5)

def somar(x, y):
    return x + y

soma10 = somar(10, 10)
print(soma10)

def soma():
    return 5 + 5 

def somar(*valores):
    return sum(valores)

soma_elementos = somar(10, 25, 40)
print(soma_elementos)

def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')

criar_perfil(nome='Ana', idade=25, cidade='Lisboa')


