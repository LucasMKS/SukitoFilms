import notas

sair = 0

while sair == 0:
    print("|======================================================|")
    option = input('| 1 - Acessar tabela de Filmes/Series já assistidos    |\n| 2 - Adicionar Filmes/Series a tabela de lançamentos  |\n| 3 - Fechar                                           |\n|======================================================|\n Opção: ')
    print('')
    if option == '1':
        conc = notas.assistido()
        print(conc)
    elif option == '2':
        conc1 = notas.lancamentos()
        print(conc1)
    elif option == '3':
        print('Saindo...')
        sair = 1

