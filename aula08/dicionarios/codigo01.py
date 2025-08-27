dicionario = {"nome": "ailton", "idade": 28, "tem_carro": True, "qtd carros": ["corolla", "porche"]}

print(dicionario["nome"])

print(len(dicionario))

dicionario["nome"] = "thiago"
print(dicionario["nome"])

print(dicionario["nome"])
dicionario.update({"nome": "Maria L"})
print(dicionario["nome"])

# print(dicionario["renda_mensal"])
dicionario.update({"renda_mensal": 5000})
print(dicionario["renda_mensal"])

# print(dicionario["tem_passaporte"])
dicionario["tem_passaporte"] = True
print(dicionario["tem_passaporte"])

del dicionario["tem_passaporte"]

# print(dicionario["qtd_carros"])
# dicionario.pop("qtd_carros")
# print(dicionario)

print(dicionario.keys())

print(dicionario.values())

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")

print(dicionario)
dicionario.clear()
print(dicionario)