clientes_ativos = {'Ana', 'Pedro', 'Maria'}
novos_clientes = {'João', 'Maria', 'Lucas'}

novos_clientes.discard('Maria')

uniao = clientes_ativos | novos_clientes

print(uniao)