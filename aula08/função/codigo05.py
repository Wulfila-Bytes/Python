def somar(x, y):
    return x, y

print(somar(10, 10))

somar = lambda x, y: x + y

print(somar(25,35))

def dobrar(x): 
    return x * 2 
numeros = [1, 2, 3] 
dobrados = list(map(dobrar, numeros)) # Resultado: [2, 4, 6]
print(dobrados)

numeros = [1, 2, 3] 
dobrados = list(filter(lambda x: x >= 2, numeros))
print(dobrados) 
# Resultado: [2, 4, 6]

alunos = [("João", 25), ("Maria", 20), ("Pedro", 22)] 
# Usando sorted() para ordenar a lista de alunos pela idade # A 'key' com lambda instrui sorted a usar o 2º elemento de cada tupla (a idade) 

alunos_ordenados_por_idade = sorted(alunos, key=lambda aluno: aluno[1]) 
print(alunos_ordenados_por_idade) 
# Saída: [('Maria', 20), ('Pedro', 22), ('João', 25)]
