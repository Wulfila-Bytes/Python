tem_wifi = False
tem_dados_moveis = True

pode_se_conectar_a_internet = (tem_wifi or tem_dados_moveis)
print(f"O celular pode se conectar na internet? {pode_se_conectar_a_internet}")