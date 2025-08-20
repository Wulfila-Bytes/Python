senha = Python123

senha_valida = (
    not (senha == "")            # A senha não é vazia
    and not (len(senha) <= 8)    # A senha tem mais de 8 caracteres
    and senha == "Python123"     # A senha é exatamente igual a "Python123"
    and not (senha == "123456")  # A senha é diferente de "123456"
)
 print(senha_valida)