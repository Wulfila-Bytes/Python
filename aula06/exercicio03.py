comidas = 'lasanha'

match comidas:
    case 'lasanha':
        print('Que lasanha gostosa...')
    case 'pirão':
        print('Que pirão gostoso...')
    case 'strogonoff':
        print('Que strogonoff gostoso...')
    case 'feijão carioca':
        print('Que feijão carioca gostoso...')
    case _ :
        print('Comando inválido')