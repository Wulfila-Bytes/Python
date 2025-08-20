esta_chovendo = bool(True)
nao_esta_chovendo = not (esta_chovendo)
resultado = (esta_chovendo or nao_esta_chovendo)

print(f'Está chovendo? {resultado}')