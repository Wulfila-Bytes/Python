conjunto = {1, 2, 3, 4, 5}
conjunto = set([1, 2, 3, 4, 5])

print(conjunto)

conjunto.add(6)
print(conjunto)

print(conjunto)
conjunto.remove(6)
print(conjunto)

print(conjunto)
for valor in enumerate(conjunto):
    print(valor)

conjunto.discard(5)
print(conjunto)

print(conjunto)
conjunto.clear()
print(conjunto)




# conjunto[]