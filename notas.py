#encoding: utf-8
# -*- coding: utf-8 -*-

import sqlite3
import pandas as pd
from datetime import date
import quickstart



# Conectar ao banco de dados
conn = sqlite3.connect('E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\sukitoFilms.db')
cursor = conn.cursor()

# Criar tabela
conn.execute('CREATE TABLE IF NOT EXISTS conteudos( id integer PRIMARY KEY AUTOINCREMENT, nome string, data date, tipo string, streaming string, nota REAL, genero1 string, genero2 string, produtora string, adicionado date);')
conn.commit()
query = 'SELECT * FROM conteudos'
filmes = pd.read_sql_query(query, conn)

data_atual = date.today()
data_em_texto = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)

# 1 = Assistido // 2 = Lançamento Futuro

def assistido():
    qry = "SELECT * FROM conteudos"
    rows = cursor.execute(qry).fetchall()
    for r in rows:
        print(r)
    conn.commit()
    num = 0
    # Abrir menu
    while num == 0:
        print('\n===============================')
        option = input('1 - Inserir dados manualmente\n2 - Atualizar dados\n3 - Deletar dados\n4 - Consulta Especifica\n5 - Sair\n===============================\n\nDigite a opção desejada: ')
        print(" ")
        print('===============================')

        # Inserir dados manualmente
        if option == '1':
            insercao = insert_assistido()
            print(insercao)

        # Atualizar dados  =========== adicionar while, loop até digitar 0 e parar de atualizar tudo
        elif option == '2':
            id_up = input("Digite o ID do conteudo que deseja alterar: ")
            
            cont = 0
            while cont == 0:
                select = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_up,)).fetchall()
                print(" ")
                print(select)
                choice = input("==================\n1 - Nome\n2 - Data\n3 - Tipo\n4 - Nota\n5 - Genero 1\n6 - Genero 2\n7 - Streaming\n8 - Produtora\n0 - Voltar \n==================\n Qual dado deseja atualizar? ") ###############

                if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8':
                    if choice == '1':
                        choice = "nome"
                    elif choice == '2':
                        choice = "data"
                    elif choice == '3':
                        choice = "tipo"
                    elif choice == '4':
                        choice = "nota"
                    elif choice == '5':
                        choice = "genero1"
                    elif choice == '6':
                        choice = "genero2"
                    elif choice == '7':
                        choice = "streaming"
                    elif choice == '8':
                        choice = "produtora"
                    print(" - - - - - - - - - - - - - - - - ")
                    modif = input(f"Digite o novo {choice}: ")
                    conn.execute(f'UPDATE conteudos SET {choice} = ? WHERE id = ?', (modif, id_up))
                    select = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_up,)).fetchall()
                    print(select)
                    conn.commit()
                elif choice == '0':
                    print('Voltando')
                    cont = 1
                else:
                    print('Numero invalido')
  
        # Deletar dados
        elif option == '3':
            print(" ")  
            deletar = input("Qual linha deseja deletar? (Digite o ID): ")
            print(" ")
            del_opc = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (deletar,)).fetchall()
            del_confirm = input('Tem certeze que deseja deletar: ', del_opc, "? ('Sim' ou 'Não') ")
            print(" ")
            if del_confirm == 'Sim' or del_confirm == 'sim':
                conn.execute('DELETE FROM conteudos WHERE id = ?', (deletar,))
                print("Deletado com sucesso!")
                conn.commit()
                print(" ")
            
            qry = "SELECT * FROM conteudos"
            rows = cursor.execute(qry).fetchall()
            for r in rows:
                print(r)
            conn.commit() 
            print(" ")       

        # Consultar dados
        elif option == '4':
            print(" ")  
            consulta = input("==================\n1 - Por nome\n2 - Por nota\n3 - Por tipo\n4 - Por genero\n5 - Por streaming\n6 - Por produtora\n==================\nQual tipo de consulta especifica deseja fazer? ")
            
            if consulta == '1' or consulta == '2' or consulta == '3' or consulta == '4' or consulta == '5' or consulta == '6' or consulta == '7' or consulta == '8':
                contador = 0
                if consulta == '1':
                    const = input(f"Qual nome deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE nome LIKE '%{const}%' ORDER BY nome ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")
                    
                elif consulta == '2':
                    const = input(f"Qual nota deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE nota LIKE '%{const}%' ORDER BY nota ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")
                    
                elif consulta == '3':
                    const = input(f"Qual tipo (\'Serie\' ou \'Filme\') deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE tipo LIKE '%{const}%' ORDER BY nota ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")
                    
                elif consulta == '4':
                    const = input(f"Qual genero deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE genero1 LIKE '%{const}%' ORDER BY nota ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")
                    
                elif consulta == '5':
                    const = input(f"Qual streaming deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE streaming LIKE '%{const}%' ORDER BY nota ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")
                    
                elif consulta == '6':
                    const = input(f"Qual produtora deseja consultar? ")
                    print(" ")
                    qry = f"SELECT * FROM conteudos WHERE produtora LIKE '%{const}%' ORDER BY nota ASC"
                    rows = cursor.execute(qry).fetchall()
                    for r in rows:
                        print(r)
                        contador += 1
                    conn.commit()
                    print(" ")
                    print("|- - - - - - - - -|")
                    print("|                 |")
                    print("| Quantidade: ", contador, " |")
                    print("|                 |")
                    print("|- - - - - - - - -|")

        # Sair
        elif option == '5':
            print("Saindo...")
            num = 1
    conc = 'Dados adicionados/alterados/removidos da agenda Notas'
    return conc
            
        
def insert_assistido():
    nome = input('Nome: ')
    data = input('Data: ')
    tipo = input('Tipo (Serie / Filme): ')
    nota = input('Nota: ')
    gen1 = input('Genero 1: ')
    gen2 = input('Genero 2: ')
    stream = input('Streaming: ')
    prod = input('Produtora: ')
    print(" ")

    cursor.execute("INSERT INTO conteudos(nome, data, tipo, streaming, nota, genero1, genero2, produtora, adicionado) VALUES(?,?,?,?,?,?,?,?,?)",(nome, data, tipo, stream, nota, gen1, gen2, prod, data_em_texto))
    conn.commit()
    
    data_hoje = date.today()
    data_add = '{}-{}-{}'.format(data_hoje.year, data_hoje.month, data_hoje.day)
    
    id_calendar = quickstart.create_watched(nome, data_add, data, tipo, nota, gen1, gen2, stream, prod)
    id_db = cursor.lastrowid
    
    print(conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_db,)).fetchall())
    correcao = input("Deseja fazer alguma correção? ('Sim' ou 'Não') ")
            
    if correcao == 'Sim' or correcao == 'sim':
        cont = 0
        while cont == 0:
            selecao = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_db,)).fetchall()
            print(" ")
            print(selecao)
                    
            choice = input("==================\n1 - Nome\n2 - Data\n3 - Tipo\n4 - Nota \n5 - Genero 1\n6 - Genero 2\n7 - Streaming\n8 - Produtora\n0 - Voltar \n==================\n Qual dado deseja atualizar? ") ###############

            if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8':
                if choice == '1':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Nome atual: ', nome)
                    nome = input(f"Digite o novo nome: ")
                    conn.execute(f'UPDATE conteudos SET nome = ? WHERE id = ?', (nome, id_db))
                    conn.commit()
                elif choice == '2':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Data atual: ', data)
                    data = input(f"Digite a nova data: ")
                    conn.execute(f'UPDATE conteudos SET data = ? WHERE id = ?', (data, id_db))
                    conn.commit()
                elif choice == '3':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Tipo atual: ', tipo)
                    tipo = input(f"Digite o novo tipo: ")
                    conn.execute(f'UPDATE conteudos SET tipo = ? WHERE id = ?', (tipo, id_db))
                    conn.commit()
                elif choice == '4':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Nota atual: ', nota)
                    nota = input(f"Digite a nova nota: ")
                    conn.execute(f'UPDATE conteudos SET nota = ? WHERE id = ?', (nota, id_db))
                    conn.commit()
                elif choice == '5':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Genero atual: ', gen1)
                    gen1 = input(f"Digite o novo genero: ")
                    conn.execute(f'UPDATE conteudos SET genero1 = ? WHERE id = ?', (gen1, id_db))
                    conn.commit()
                elif choice == '6':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Genero atual: ', gen2)
                    gen2 = input(f"Digite o novo genero: ")
                    conn.execute(f'UPDATE conteudos SET genero2 = ? WHERE id = ?', (gen2, id_db))
                    conn.commit()
                elif choice == '7':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Streaming atual: ', stream)
                    stream = input(f"Digite o novo streaming: ")
                    conn.execute(f'UPDATE conteudos SET streaming = ? WHERE id = ?', (stream, id_db))
                    conn.commit()
                elif choice == '8':
                    print(" - - - - - - - - - - - - - - - - ")
                    print('Produtora atual: ', prod)
                    prod = input(f"Digite a nova Produtora: ")
                    conn.execute(f'UPDATE conteudos SET produtora = ? WHERE id = ?', (prod, id_db))
                    conn.commit()
                        
                att = quickstart.update_watched(id_calendar, nome, data_add, data, tipo, nota, gen1, gen2, stream, prod)
                print(att, ' atualizado no calendar')
                print(" - - - - - - - - - - - - - - - - ")
            elif choice == '0':
                print('Voltando')
                cont = 1
                        
            else:
                print("Numero invalido")
    else:
        print('Voltando')
    dado_adc = conn.execute(f'SELECT nome FROM conteudos WHERE id = ?', (id_db,)).fetchall()
    result = dado_adc," adicionado com sucesso"
    return result
      
          
            
def lancamentos():
    print('')
    data_atual_con = date.today().strftime('%Y-%m-%d')
    qry = f"SELECT * FROM conteudos WHERE data > '{data_atual_con}' ORDER BY data ASC"
    rows = cursor.execute(qry).fetchall()
    for r in rows:
        print(r)
    conn.commit()
    num = 0
        # Abrir menu
    while num == 0:
        print('|========================|')
        option = input('| 1 - Inserir dado       |\n| 2 - Sair               |\n|========================|\n\nDigite a opção desejada: ')
        print(" ")

        # Inserir dado
        if option == '1':
            nome = input('Nome: ')
            data = input('Data (YYYY-mm-dd ex: 2023-01-23): ')
            tipo = input('Tipo (Serie / Filme): ')
            if tipo == 'Serie' or tipo == 'serie':
                tipografia = input(' 1 - Episodio semanal \n 2 - Lançamento completo \n ')
                if tipografia == '1':
                    freque = 'WEEKLY'
                    ep_count = input("Quantas semanas que terão lançamento de episodio? ")
                else:
                    freque = 'DAILY'
                    ep_count = '1'
            gen1 = input('Genero 1: ')
            gen2 = input('Genero 2: ')
            stream = input('Streaming: ')
            prod = input('Produtora: ')
            print(" ")
            id_calendar = quickstart.create_future(nome, data, tipo, gen1, gen2, stream, prod, freque, ep_count)
            

            cursor.execute("INSERT INTO conteudos(nome, data, tipo, streaming, genero1, genero2, produtora, adicionado) VALUES(?,?,?,?,?,?,?,?)",(nome, data, tipo, stream, gen1, gen2, prod, data_em_texto))
            conn.commit()
            id_db = cursor.lastrowid
            
            correcao = input("\nDeseja fazer alguma correção? ('Sim' ou 'Não') ")
            
            if correcao == 'Sim' or correcao == 'sim':
                cont = 0
                while cont == 0:
                    select = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_db,)).fetchall()
                    print(" ")
                    print(select)
                    
                    choice = input("|==================|\n| 1 - Nome\n| 2 - Data\n| 3 - Tipo\n| 4 - Genero\n| 5 - Streaming\n| 6 - Produtora\n| 0 - Voltar \n|==================|\n Qual dado deseja atualizar? ")

                    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
                        if choice == '1':
                            print('| Nome atual: ', nome)
                            choice = "nome"
                        elif choice == '2':
                            print('| Data atual: ', data)
                            choice = "data"
                        elif choice == '3':
                            print('| Tipo atual: ', tipo)
                            choice = "tipo"
                        elif choice == '4':
                            print('| Genero atual: ', gen1)
                            choice = "genero1"
                        elif choice == '5':
                            print('| Streaming atual: ', stream)
                            choice = "streaming"
                        elif choice == '6':
                            print('| Produtora atual: ', prod)
                            choice = "produtora"
                        print('|================================|')
                        modif = input(f"Digite o novo {choice}: ")
                        conn.execute(f'UPDATE conteudos SET {choice} = ? WHERE id = ?', (modif, id_db))
                        select = conn.execute(f'SELECT * FROM conteudos WHERE id = ?', (id_db,)).fetchall()
                        print(select)
                        conn.commit()
                        
                        att = quickstart.update(id_calendar, nome, data, tipo, gen1, stream, prod)
                        print(att, ' atualizado no calendar')
                        
                    elif choice == '0':
                        print('Voltando')
                        cont = 1
                        
                    else:
                        print("Numero invalido")
            else:
                print('Voltando')
        elif option == '2':
            conn.close()
            exit()
    conc1 = 'Dados adicionados/alterados/removidos da agenda de lançamentos'
    return conc1



# result = conn.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%ão%',))
#query = "SELECT * FROM conteudos WHERE tipo = Filme"
#df = pd.read_sql_query(query, conn)
#print(df.head())
# pyinstaller --onefile notas.py



