produtos = ["arroz", "feijão", "macarrão", "óleo de soja", "sal," "açúcar", "café",
             "leite", "pão", "manteiga", "ovos", "queijo", "presunto", "iorgute",
               "frango", "carne bovina", "peixe", "tomate", "cebola", "batata"]
var1 = produtos[0]
print(produtos[0], var1)

print(produtos[0:4])

print(produtos)
produtos.append("biscoito")
print(produtos)

print(produtos[19])
produtos.extend(["salgadinho", "melao"])
print(produtos)

print(produtos)
produtos.insert(0,"amendoim")
print(produtos)
produtos.insert(1, "arroz")

print(produtos)
#produtos.remove(["salgadinho", "melao"]) 
print(produtos)
produtos.remove("arroz")

print(produtos)
# produtos.pop([0])
print(produtos)

print(produtos)
produtos.sort()
print(produtos)

print(produtos)
produtos.reverse()
print(produtos)

print(produtos)
produtos.count("arroz")
print(produtos)

print(produtos.index("cebola"))
print(produtos)

print(len(produtos))

print(produtos)
del produtos[0]
print(produtos)
del produtos[0:4]

print(produtos)
produtos.clear()
print(produtos)

