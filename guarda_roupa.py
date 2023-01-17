from datetime import date

def cria_id(): #cria um novo ID apartir do ultimo ID criado
    arq_ID = open('ID.txt','r')
    ID_antigo = arq_ID.readline()
    arq_ID.close()
    if ID_antigo == '':
        arq_ID = open('ID.txt','w')
        arq_ID.write('0')
        ID_antigo = 0
        arq_ID.close()
    ID = int(ID_antigo) + 1
    arq_ID = open('ID.txt','w')
    arq_ID.write(str(ID))
    arq_ID.close()
    return ID

def listar_guardaroupa(): # Mostra todas as peças do guarda roupa
    arquivo = open('pecas.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()
    for i in range(len(linhas)):
        print(linhas[i])

def inserir_estilo1(linhas,nome_peca,ID,i): #função criada para dar suporte a função inserir peça
    arq_estilos = open('estilos.txt','w')
    if linhas[i*4 + 1] == '\n':
        linhas[i*4 + 1] = ['\n']
        linhas[i*4 + 1].insert(0, nome_peca)
        linhas[i*4 + 1].insert(0,'{}'.format(ID))
    else:
        linhas[i*4 + 1] = linhas[i*4 + 1].split(',')
        linhas[i*4 + 1].insert(0,nome_peca)
        linhas[i*4 + 1].insert(0,ID)
    t = '{},'.format(linhas[i*4 + 1][0])
    for j in range(len(linhas[i*4 + 1])-1):
        t = t + '{},'.format(linhas[i*4 + 1][j+1])
    if t[-3] == ',':
        linhas[i*4 + 1] = t[:-3] + '\n'
    else:
        linhas[i*4 + 1] = t[:-1]
    for d in range(len(linhas)):
        arq_estilos.write(linhas[d])
    arq_estilos.close()

def inserir_estilo2(linhas,nome_peca,ID,i): #função criada para dar suporte a função inserir peça
    arq_estilos = open('estilos.txt','w')
    if linhas[i*4 + 2] == '\n':
        linhas[i*4 + 2] = ['\n']
        linhas[i*4 + 2].insert(0, nome_peca)
        linhas[i*4 + 2].insert(0,'{}'.format(ID))
    else:
        linhas[i*4 + 2] = linhas[i*4 + 2].split(',')
        linhas[i*4 + 2].insert(0,nome_peca)
        linhas[i*4 + 2].insert(0,ID)
    t = '{},'.format(linhas[i*4 + 2][0])
    for j in range(len(linhas[i*4 + 2])-1):
        t = t + '{},'.format(linhas[i*4 + 2][j+1])
    if t[-3] == ',':
        linhas[i*4 + 2] = t[:-3] + '\n'
    else:
        linhas[i*4 + 2] = t[:-1]
    for d in range(len(linhas)):
        arq_estilos.write(linhas[d])
    arq_estilos.close()

def inserir_estilo3(linhas,nome_peca,ID,i): #função criada para dar suporte a função inserir peça
    arq_estilos = open('estilos.txt','w')
    if linhas[i*4 + 3] == '\n':
        linhas[i*4 + 3] = ['\n']
        linhas[i*4 + 3].insert(0, nome_peca)
        linhas[i*4 + 3].insert(0,'{}'.format(ID))
    else:
        linhas[i*4 + 3] = linhas[i*4 + 3].split(',')
        linhas[i*4 + 3].insert(0,nome_peca)
        linhas[i*4 + 3].insert(0,ID)
    t = '{},'.format(linhas[i*4 + 3][0])
    for j in range(len(linhas[i*4 + 3])-1):
        t = t + '{},'.format(linhas[i*4 + 3][j+1])
    if t[-3] == ',':
        linhas[i*4 + 3] = t[:-3] + '\n'
    else:
        linhas[i*4 + 3] = t[:-1]
    for d in range(len(linhas)):
        arq_estilos.write(linhas[d])
    arq_estilos.close()

def inserir_estilo(dic): # Inserir peça em um estilo existente
    dic_estilo = {}
    pecas = []
    nome_estilo = dic['estilo']
    ID = dic['ID']
    nome_peca = dic['nome']
    arq_estilos = open('estilos.txt','r')
    if dic['tipo'] == 'Superior':
        tipo = 1
    elif dic['tipo'] == 'Inferior':
        tipo = 2
    elif dic['tipo'] == 'Calçado' or dic['tipo'] == 'Calï¿½ado':
        tipo = 3
    else:
        tipo = dic['tipo']
    linhas = arq_estilos.readlines()
    arq_estilos.close()
    for i in range((len(linhas)//4)):
        if (linhas[i*4].split(','))[0] == nome_estilo and tipo == 1:
            inserir_estilo1(linhas,nome_peca,ID,i)
            break
        elif (linhas[i*4].split(','))[0] == nome_estilo and tipo == 2:
            inserir_estilo2(linhas,nome_peca,ID,i)
            break
        elif (linhas[i*4].split(','))[0] == nome_estilo and tipo == 3:
            inserir_estilo3(linhas,nome_peca,ID,i)
            break
    arq_estilos.close()

def estilo_geral(dic): #função criada para definir se o estilo inserido existe ou não
    arq_estilos = open('estilos.txt','r')
    linhas_est = arq_estilos.readlines()
    if linhas_est == []:
        k = 0
    else:
        for i in range((len(linhas_est)//4)):
            if dic['estilo'] == (linhas_est[i*4].split(','))[0]:
                k = 1
                arq_estilos.close()
                break
            else:
                k = 0
    if k == 0:
        arq_estilos.close()
        criar_estilo(dic['estilo'],dic['tipo'],dic['ID'],dic['nome'])
    elif k == 1:
        inserir_estilo(dic)

def organizar_estilos(): #função criada para organizar os estilos em ordem do mais popular ao menos popular
    arq_est = open('estilos.txt','r')
    estilos = arq_est.readlines()
    arq_est.close()
    estilos_matriz = []
    for i in range(len(estilos)//4):
        estilo = (estilos[i*4] + estilos[i*4 +1] + estilos[i*4 +2] + estilos[i*4 + 3])
        estilos_matriz.append(estilo)
    for i in range(len(estilos_matriz)):
        for j in range(len(estilos_matriz)):
            if j < i:
                j = i
            if int(estilos_matriz[i].split(',')[1][0]) < int(estilos_matriz[j].split(',')[1][0]):
                a = estilos_matriz.pop(j)
                estilos_matriz.insert(i,a)
    arq_est = open('estilos.txt','w')
    for i in range(len(estilos_matriz)):
        arq_est.write(estilos_matriz[i])

def registrar_dados(): # Coloca todos os dados em um dicionário
    dic = {}

    ID = cria_id()
    dic.update({'ID':ID})

    # Tipo da roupa: Superior, Inferior, Calçado
    while True: # Tratando para ser apenas 1, 2 ou 3
        try: 
            tipo = int(input('Tipo da peça\n1-Superior\n2-Inferior\n3-Calçado: '))
            if tipo == 1 or tipo == 2 or tipo == 3:
                dic.update({'tipo':tipo})
                break
            else:
                print('Opção inválida. ')
        except ValueError:
            print('Opção inválida. ')

    while True:
        nome = input('Nome da peça \nExemplo:Camisa, Chinela, Bermuda,...\n')
        if nome.isnumeric() == False and nome != '' and nome != ' ': # Se todos os caracteres não foram números
            nome = nome.capitalize() 
            dic.update({'nome':nome})
            break
        else: 
            print('Inválido. ')

    tamanhos_disponiveis = ['P', 'M', 'G'] # Tamanhos disponíveis
    while True:
        tamanho = input('Tamanho da peça (P,M ou G): ')
        if (tamanho.isalpha()) == True: # Se for string
            tamanho = tamanho.upper()
            if tamanho in tamanhos_disponiveis: # Se estiver na lista de tamanho, break
                dic.update({'tamanho':tamanho})
                break
            else:
                print('Tamanho não disponível. ')
        else:
            print('Inválido.')

    padroes_disponiveis = ['MASCULINO', 'FEMININO', 'UNISSEX'] # Padrões disponíveis
    while True:
        padrao = input('Padrão da peça(Masculino,Feminino,Unissex): ')
        if (padrao.isalpha()) == True and padrao != '' and padrao != ' ': 
            padrao = padrao.upper()
            if padrao in padroes_disponiveis:
                dic.update({'padrao': padrao})
                break
            else:
                print('Padrão não disponível. ')
        else:
            print('Inválido.')

    while True:
        cor = input('Cor da peça: ')
        if (cor.isnumeric()) == False and cor != '' and cor != ' ':  
            cor = cor.capitalize()
            dic.update({'cor':cor})
            break
        else:
            print('Inválido')

    data_aquisicao = date.today() # Importa a data exata do sistema operacional (aaa/mm/dd)
    dic.update({'data de aquisicao':data_aquisicao})

    dic.update({'situacao':'Guardada'}) 

    # preco = float(input('Preço da peça: '))
    dic.update({'preco':' '}) # Inicialmente, a peça só é guardada

    while True:
        estilo_peca = input('Estilo da peça: ')
        if (estilo_peca.isnumeric()) == False and estilo_peca != '' and estilo_peca != ' ':
            estilo_peca = estilo_peca.capitalize()
            dic.update({'estilo':estilo_peca})
            break
        else:
            print('Inválido. ')

    estilo_geral(dic)
    return dic

def criar_estilo(estilo_peca,tipo,ID,nome): #criar novo estilo quando estilo da peça não existir
    string = '{},0\n'.format(estilo_peca)
    if tipo == 1 or tipo == 'Superior':
        string2 ='{},{}\n'.format(ID,nome)
    else:
        string2 = '\n'
    if tipo == 2 or tipo == 'Inferior':
        string3 ='{},{}\n'.format(ID,nome)
    else:
        string3 = '\n'
    if tipo == 3 or tipo == 'Calçada':
        string4 ='{},{}\n'.format(ID,nome)
    else:
        string4 = '\n'
    arq_estilos = open('estilos.txt','a')
    arq_estilos.write(string + string2 + string3 + string4)
    arq_estilos.close()

def inserir_peca(dic): #inserir dados da peça no arquivo pecas.txt
    if dic['tipo'] == 1:
        tipo = 'Superior'
    elif dic['tipo'] == 2:
        tipo = 'Inferior'
    elif dic['tipo'] == 3:
        tipo = 'Calçado'
    else:
        tipo = dic['tipo']
    linha = '{},{},{},{},{},{},{},{},{},{}\n'.format(dic['ID'],tipo,dic['nome'],dic['tamanho'],dic['padrao'],dic['cor'],dic['data de aquisicao'],dic['situacao'],dic['preco'],dic['estilo'])
    arquivo = open('pecas.txt','a')
    arquivo.write(linha)

def buscar_interesse(tamanho, padrao): # lista de roupas
    #listar peças com o tamanho e padrão desejados
    # se a roupa tiver tamanho e padrão desejados, listá-la
    with open('pecas.txt', 'r') as pecas:
        linhas = pecas.readlines()
    roupas_desejadas = []
    for i in range(len(linhas)): 
        if tamanho in linhas[i] and padrao in linhas[i]:
            roupas_desejadas.append(linhas[i])

    if roupas_desejadas == []:
        return False
    else:
        print('ROUPAS QUE PODEM SER DO SEU INTERESSE: ')
        for j in roupas_desejadas:
            print(j)

def buscar_donatario(donatario): # Busca o donatário e lista os itens que foram doados para ele
    with open('doadas.txt','r') as arq_doadas:
	    linhas = arq_doadas.readlines() 
    k = 0 # bug do VS Code
    for i in range(len(linhas)):
        linha = linhas[i].replace(', ,', ',')
        if ((linha.split(','))[-1][:-1]).upper() == donatario:
            print(linha)
            k = 1
    if k == 0:
        print('O donatário não existe.')

def listar_todos_estilos(): #Lista todos os estilos existentes em ordem do mais popular ao menos popular
    arq_estilos = open('estilos.txt','r')
    estilos = arq_estilos.readlines()
    for i in range(len(estilos)//4):
        print((estilos[i*4].split(',')[0]))

def apresentar_estilos(): #apresenta os estilos que podem ser selecionados pela opção de buscar estilo pelo nome
    with open('estilos.txt', 'r') as todas_pecas:
        pecas = todas_pecas.readlines()
        for i in range(len(pecas)):
            pecas[i] = pecas[i].split(',')
        for i in range((len(pecas)//4)):
            print('{}'.format(pecas[i*4][0]))

def buscar_estilo(estilo): # retorna todas as peças do estilo escolhido
    arq_estilos = open('estilos.txt','r')
    linhas = arq_estilos.readlines()
    arq_estilos.close()
    l = 0
    for i in range(len(linhas)//4):
        if (linhas[i*4].split(','))[0].capitalize() == estilo:
            l1 = linhas[i*4].split(',')
            l2 = linhas[(i*4) + 1].split(',')
            l3 = linhas[(i*4) + 2].split(',')
            l4 = linhas[(i*4) + 3].split(',')
            l = [l1,l2,l3,l4]
            break
    if l == 0:
        print('Estilo não existe.')
        exit()
    else:
        return l

def contador_arq(estilo_cont): #atualiza o contador do estilo quando ele é escolhido
    arq_estilos = open('estilos.txt','r')
    linhas = arq_estilos.readlines()
    arq_estilos.close()
    estilo = (estilo_cont)[0]
    for i in range(len(linhas)//4):
        if (linhas[i*4].split(','))[0] == estilo:
            linhas[i*4] = estilo_cont[0] + ',' + estilo_cont[1]
    arq_estilos = open('estilos.txt','w')
    for i in range(len(linhas)):
        arq_estilos.write(linhas[i])

def mostrar_estilo(linha): #mostra todas as peças do estilo escolhido e seus IDs, além de somar 1 ao contador
    l1 = linha[0]
    l2 = linha[1]
    l3 = linha[2]
    l4 = linha[3]
    if l2 == ['\n'] and l3 == ['\n'] and l4 == ['\n']: # ['\n'] é um elemento na lista
        print('Esse estilo está vazio.')
        exit()

    # l1[1] = str(int(l1[1][0]) + 1) + '\n' # +1 incrementa o contador
    t1 = '{}\n'.format(l1[0])
    t2 = t3 = t4 = ''
    for i in range(len(l2)):
        t2 = t2 + '{},'.format(l2[i])
    for i in range(len(l3)):
        t3 = t3 + '{},'.format(l3[i])
    for i in range(len(l4)):
        t4 = t4 + '{},'.format(l4[i])
    t2 = t2[:-2] + '\n'
    t3 = t3[:-2] + '\n'
    t4 = t4[:-2] + '\n'
    t = t1 + t2 + t3 + t4
    print(t)

    decisao_alternativas = ['SIM', 'NÃO']
    while True:
        decisao = input('VOCÊ DESEJA MUDAR O ESTILO? ')
        decisao = decisao.upper()
        if decisao in decisao_alternativas:
            break
        else:
            print('Resposta inválida. ')

    if decisao == 'NÃO':
        l1[1] = str(int(l1[1][0]) + 1) + '\n' # +1 incrementa o contador
        contador_arq(l1)
    elif decisao == 'SIM':
        # começa tudo de novo
        apresentar_estilos()
        while True:
            nome_estilo = input('INSIRA O NOME DO ESTILO DESEJADO: ') # escolher 1
            if nome_estilo.isnumeric() == False and nome_estilo != '' and nome_estilo != ' ':
                break
            else:
                print('Estilo inválido.')

        estilo_escolhido = buscar_estilo(nome_estilo.capitalize()) # listar TODAS as peças do estilo escolhido (add contador dentro da função)
        mostrar_estilo(estilo_escolhido)

def remover_peca(ID): #remove peça do guarda roupa
    with open('pecas.txt','r') as arquivo:
        linhas = arquivo.readlines()
    t = []
    k = 0
    for i in range(len(linhas)):
        t.append(linhas[i].split(','))
    for i in range(len(t)):
        if int(t[i][0]) == ID:
            linhas.pop(i)
            k = 1
            break
    if k == 0:
        print('ID NÃO ENCONTRADO')
    with open('pecas.txt','w') as arquivo:
        for i in range(len(linhas)):
            arquivo.write(linhas[i])

def doar_peca(ID): #tranfere uma peça do guarda roupa para a lista de peças doadas e adiciona um donatario
    k = 0
    with open('pecas.txt','r') as arquivo: # Mudando o 'pecas.txt' (fazer isso com 'estilos.txt' também)
        linhas = arquivo.readlines() # ler todas as linhas do arquivo
    for i in range(len(linhas)):
        if linhas[i][0] == str(ID): # dar split na linha 
            linha = linhas[i]
            linha = linha.replace('Guardada', 'Doada')
            k = 1 # contador verificador do ID 
            while True:
                donatario = input('DIGITE O DONATÁRIO (Pessoa física ou jurídica): ')
                if donatario == '' or donatario == ' ':
                    print('Inválido.')
                else:
                    break
            linha = linha[:len(linha)-1]
            linha += ',' + str(donatario) + '\n'
            with open('doadas.txt','a') as arquivo:
                arquivo.write(linha) # escrever as linhas de novo no arquivo
    if k == 1:
        remover_peca(ID) 

    else:
        print('ID não encontrado')

    with open('pecas.txt','r') as arquivo: 
        linhas = arquivo.readlines() # ler todas as linhas do arquivo
    for i in range(len(linhas)):
        if linhas[i][0] == str(ID):
            linha = linhas[i]
            linha = linha.replace('Guardada', 'À venda')
            with open('a_venda.txt','a') as arquivo: #
                arquivo.write(linha) # escrever as linhas de novo no arquivo
  
def vender_peca(ID, preco,comprador): # Função para VENDER --> Vai para arquivo 'vendidas.txt'
    k = 0
    with open('pecas.txt','r') as arquivo: # Mudando o 'pecas.txt' 
        linhas = arquivo.readlines() # ler todas as linhas do arquivo
    for i in range(len(linhas)):
        if linhas[i][0] == str(ID):
            linha = linhas[i]
            linha = linha.replace('Guardada', 'Vendida')
            dados = ',R$' + str(preco) + ',' + comprador + ',' # entre vírgulas
            linha = linha.replace(', ,', dados)
            with open('vendidas.txt','a') as arquivo: #
                arquivo.write(linha) # escrever as linhas de novo no arquivo
            k = 1
    if k == 1:
        remover_peca(ID)
    else:
        print('ID não encontrado')

def apagar_estilo1_1(t,i): #tratamento da função apagar_estilo
    if t[i] == []:
        t[i].append('\n')
    elif t[i][-1][-1] != '\n':
        t[i][-1] = t[i][-1] + '\n'
    return t

def apagar_estilo1(linhas,t,k,ID): #retorna as novas linhas do arquivo estilos.txt
    for i in range(len(linhas)):
        t.append(linhas[i].split(','))
    for i in range(len(linhas)):
        for j in range(len(t[i])//2):
            if t[i][j*2] == ID:
                t[i].pop(j*2)
                t[i].pop(j*2)
                t = apagar_estilo1_1(t,i)
                k = 1
                break
        if k == 1:
            if t[i] == []: 
                t[i].append('\n')
            break
    linhas = []
    for i in range(len(t)):
        m = ''
        for j in range(len(t[i])):
            m = m + '{},'.format(t[i][j])
        m = m[:-1]
        linhas.append(m)
    return linhas

def apagar_estilo(ID): #remove peça do arquivo
    ID = str(ID)
    arq_estilos = open('estilos.txt','r')
    linhas = arq_estilos.readlines()
    arq_estilos.close()
    t = [] #lista que conterá as informações de cada linha no futuro
    k = 0 #variavel para verificar se uma parte do codigo foi executada
    linhas = apagar_estilo1(linhas,t,k,ID)
    arq_estilos = open('estilos.txt','w')
    for i in range(len(linhas)):
        arq_estilos.write(linhas[i])
    arq_estilos.close()

def dic_alt(t): #função para alterar e retornar caracteristicas de uma peça no guarda roupa
    print('1-TIPO')
    print('2-NOME')
    print('3-TAMANHO')
    print('4-PADRÃO')
    print('5-COR')
    print('6-ESTILO')
    escolha = int(input('ESCOLHA O NUMERO DA OPÇÃO QUE DESEJA SER ALTERADA:\n'))
    if escolha == 1:
        t[1] = int(input('DIGITE O NOVO TIPO\n1-SUPERIOR\n2-INFERIOR\n3-CALÇADO\n'))
    elif escolha == 2:
        t[2] = input('DIGITE O NOVO NOME\n')
    elif escolha == 3:
        t[3] = input('DIGITE O NOVO TAMANHO\n')
    elif escolha == 4:
        t[4] = input('DIGITE O NOVO PADRÃO\n')
    elif escolha == 5:
        t[5] = input('DIGITE A NOVA COR\n')
    elif escolha == 6:
        t[9] = (input('DIGITE O NOME DO ESTILO\n')).capitalize()
    dic = {}
    dic.update({'ID':t[0]})
    dic.update({'tipo':t[1]})
    dic.update({'nome':t[2]})
    dic.update({'tamanho':t[3]})
    dic.update({'padrao':t[4]})
    dic.update({'cor':t[5]})
    dic.update({'data de aquisicao':t[6]})
    dic.update({'situacao':t[7]})
    dic.update({'preco':t[8]})
    dic.update({'estilo':t[9]})
    return dic

def alterar_dados(ID): #modifica guarda roupa depois de receber novas caracteristicas de uma peça
    arquivo = open('pecas.txt','r')
    linhas = arquivo.readlines()
    arquivo.close()
    t = []
    k = 0
    for i in range(len(linhas)):
        t = linhas[i].split(',')
        if t[0] == str(ID):
            k = 1
            break
    if k == 1:
        t[9] = t[9][:-1]
        dic = dic_alt(t)
        remover_peca(ID)
        apagar_estilo(ID)
        estilo_geral(dic)
        inserir_peca(dic)
    else:
        print('ID não encontrado')

def listar_doadas(): # Lista todas as roupas que foram doadas da mais recente a mais antiga
    with open('doadas.txt', 'r') as doadas: 
        linhas = doadas.readlines()
    if linhas == []:
        print('Nenhuma roupa foi doada ainda.')
    else:
        for i in range(len(linhas)-1,-1,-1):
            linha = linhas[i].split(',')
            # print('Roupa(s) doadas para a ONG %s: '%(linha[-1]))
            # Esse print dará certo quando a ONG estiver no final de cada linha
            # Por enquanto, linha[-1] é o estilo
            ONG = linha.pop(-1) # Se a ONG estiver no final da linha, será excluida
            ONG = ONG[:len(ONG)-1]
            linha.pop(8)
            linha.pop(-2)
            print('ROUPAS DOADAS PARA O(A) DONATÁRIO(A) %s: '%ONG)
            print(linha)
            print()

def listar_vendidas(): #lista roupas vendidas na ordem do mair para o menor preço
    with open('vendidas.txt', 'r') as vendidas:
        linhas = vendidas.readlines()
    if linhas == []:
        print('Nenhuma roupa foi vendida ainda.')
    else:
        for i in range(len(linhas)):
            linha = linhas[i].split(',')
            estilo = linha.pop(-1)
            estilo = estilo[:len(estilo)-1]
            linha.append(estilo)
            print(linha)

def organizar_precos(): #organiza os preços do maior ao menor
    arq_venda = open('vendidas.txt','r')
    linhas = arq_venda.readlines()
    arq_venda.close()
    for i in range(len(linhas)):
        for j in range(len(linhas)):
            if j < i:
                j = i
            if float(linhas[i].split(',')[8][2:]) < float(linhas[j].split(',')[8][2:]): # preço na posição 8
                # trocam de posição
                maior_valor = linhas.pop(j)
                linhas.insert(i,maior_valor)
    arq_venda = open('vendidas.txt','w')
    for i in range(len(linhas)):
        arq_venda.write(linhas[i]) # escrevendo no arquivo na ordem de preços
    arq_venda.close()

# PROGRAMA PRINCIPAL
arquivo = open('pecas.txt','a') # Arquivo com todas as peças do guarda-roupa
arquivo.close()

arq_estilos = open('estilos.txt','a') # Arquivo com todos os estilos
# Um estilo continua na lista, mesmo que todas as suas peças sejam excluídas
# Um estilo só é excluído quando ele próprio é excluído
arq_estilos.close()

arq_doadas = open('doadas.txt','a') # Arquivo com histórico de peças já doadas
arq_doadas.close()

arq_vendidas = open('vendidas.txt', 'a') # Arquivo com histórico de peças já vendidas
arq_vendidas.close()

arq_ID = open('ID.txt','a') # Arquivo para organizar o ID. Mostra o último ID criado/utilizado
arq_ID.close()
# Inicializando arquivos 

print('OPÇÃO 1: OPÇÕES DE GUARDA-ROUPA') 
print('OPÇÃO 2: OPÇÕES DE VENDA')
print('OPÇÃO 3: OPÇÕES DE DOAÇÃO') 
print('OPÇÃO 4: BUSCAR PEÇAS COM BASE NO INTERESSE') 

# Roupas vendidas ou doadas são continuam no arquivo 'estilo.txt', mas roupas excluídas saem de 'pecas.txt' e 'estilos.txt'

while True:
    try:
        escolha = int(input('ESCOLHA O NÚMERO DA OPÇÃO: '))
        if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4:
            break
        else:
            print('Inválido.')
    except ValueError:
        print('Inválido.')

if escolha == 1: # OPÇÕES DE GUARDA-ROUPA
    print('OPÇÃO 1: PEÇA DE ROUPA')
    print('OPÇÃO 2: ESTILO')

    while True:
        try:
            escolha_1 = int(input('ESCOLHA UMA OPÇÃO: '))
            if escolha_1 == 1 or escolha_1 == 2:
                break
            else:
                print('Inválido.')
        except ValueError:
            print('Inválido.')

    if escolha_1 == 1: # PEÇA DE ROUPA
        print('OPÇÃO 1: INSERIR PEÇA DE ROUPA')
        print('OPÇÃO 2: REMOVER PEÇA DE ROUPA')
        print('OPÇÃO 3: ALTERAR DADOS DE PEÇA DE ROUPA')
        print('OPÇÃO 4: LISTAR TODAS AS PEÇAS NO GUARDA-ROUPA')

        while True:
            try:
                escolha_1_1 = int(input('ESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha_1_1 == 1 or escolha_1_1 == 2 or escolha_1_1 == 3 or escolha_1_1 == 4:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')

        if escolha_1_1 == 1: # INSERIR PEÇA DE ROUPA
            dados_peca = registrar_dados() # função irá perguntar todos os dados
            inserir_peca(dados_peca)

        if escolha_1_1 == 2: # REMOVER PEÇA DE ROUPA
            print('PEÇAS PRESENTES NO GUARDA-ROUPA: \n')
            listar_guardaroupa() # Mostra todas as roupas do guarda-roupa
            ID = int(input('DIGITE O ID DA PEÇA QUE DESEJA REMOVER: '))
            remover_peca(ID) # função para procurar e remover a peça     
            apagar_estilo(ID) #função para apagar do estilo
        if escolha_1_1 == 3: # ALTERAR DADOS DE PEÇA DE ROUPA
            ID = int(input('DIGITE O ID DA PEÇA QUE DESEJA ALTERAR: '))
            alterar_dados(ID)
        if escolha_1_1 == 4:
            listar_guardaroupa()

    if escolha_1 == 2: # ESTILO
        organizar_estilos()
        print('OPÇÃO 1: SELECIONAR ESTILO POR NOME')  
        print('OPÇÃO 2: LISTAR ESTILOS') # Usar contador para saber popularidade 

        while True:
            try:
                escolha_1_2 = int(input('ESCOLHA O NÚMERO DA OPÇÃO: '))
                if escolha_1_2 == 1 or escolha_1_2 == 2:
                    break
                else:
                    print('Inválido.')
            except ValueError:
                print('Inválido.')

        if escolha_1_2 == 1: # SELECIONAR ESTILO POR NOME
            apresentar_estilos()
            while True:
                nome_estilo = input('INSIRA O NOME DO ESTILO DESEJADO: ') # escolher 1
                if nome_estilo.isnumeric() == False and nome_estilo != '' and nome_estilo != ' ':
                    break
                else:
                    print('Estilo inválido.')

            estilo_escolhido = buscar_estilo((nome_estilo).capitalize()) # listar TODAS as peças do estilo escolhido (add contador dentro da função)
            mostrar_estilo(estilo_escolhido)

        if escolha_1_2 == 2: # LISTAR ESTILOS
            listar_todos_estilos() # listar TODOS os estilos
  
if escolha == 2: # OPÇÕES DE VENDA
    organizar_precos() # Ordena a lista das peças vendidas por ordem do maior preço para o menor preço
    print('OPÇÃO 1: LISTAR PEÇAS DE ROUPA VENDIDAS') # EM ORDEM DE PREÇO
    print('OPÇÃO 2: VENDER PEÇA')  

    while True:
        try:
            escolha_2 = int(input('ESCOLHA O NÚMERO DA OPÇÃO: '))
            if escolha_2 == 1 or escolha_2 == 2:
                break
            else:
                print('Inválido.')
        except ValueError:
            print('Inválido.')

    if escolha_2 == 1: # LISTAR PEÇAS DE ROUPA VENDIDAS
        listar_vendidas() 

    if escolha_2 == 2: # VENDER PEÇA
        print('PEÇAS PRESENTES NO GUARDA-ROUPA: \n')
        listar_guardaroupa() # Mostra todas as roupas do guarda-roupa
        ID = int(input('DIGITE O ID DA PEÇA QUE DESEJA VENDER: '))
        while True:
            preco = float(input('DIGITE O PREÇO DA PEÇA: '))
            comprador = input('DIGITE O NOME DO COMPRADOR: ').capitalize()
            if preco > 0:
                vender_peca(ID, preco, comprador)
                break
            else:
                print('Preço inválido. ')

if escolha == 3: # OPÇÕES DE DOAÇÃO
    print('OPÇÃO 1: LISTAR ROUPAS DOADAS')
    print('OPÇÃO 2: BUSCAR ROUPAS DOADAS')
    print('OPÇÃO 3: DOAR PEÇA')

    while True:
        try:
            escolha_3 = int(input('ESCOLHA O NÚMERO DA OPÇÃO: '))
            if escolha_3 == 1 or escolha_3 == 2 or escolha_3 == 3:
                break
            else:
                print('Inválido.')
        except ValueError:
            print('Inválido.')
    
    if escolha_3 == 1: # LISTAR ROUPAS DOADAS
        listar_doadas()

    if escolha_3 == 2: # BUSCAR ROUPAS DOADAS
        while True:
            donatario = input('DIGITE O DONATÁRIO QUE DESEJA PROCURAR: ')
            if donatario != '' and donatario != ' ' and (donatario.isnumeric()) == False:
                donatario = donatario.upper()
                buscar_donatario(donatario)
                break
            else:
                print('Donatário inválido.')

    if escolha_3 == 3: # DOAR PEÇA
        print('PEÇAS PRESENTES NO GUARDA-ROUPA: \n')
        listar_guardaroupa() # Mostra todas as roupas do guarda-roupa
        ID = int(input('DIGITE O ID DA PEÇA QUE DESEJA DOAR: '))
        doar_peca(ID)

if escolha == 4: # BUSCAR PEÇAS COM BASE NO INTERESSE
    print('TAMANHOS: P, M, G')
    tamanhos_disponiveis = ['P', 'M', 'G']
    while True:
        tamanho_user = input('TAMANHO DESEJADO: ')
        if (tamanho_user.isalpha()) == True:
            tamanho_user = tamanho_user.upper()
            if tamanho_user in tamanhos_disponiveis:
                break
            else:
                print('Tamanho não disponível. ')
        else:
            print('Inválido.')

    print('FEMININO, MASCULINO, UNISSEX')
    padroes_disponiveis = ['FEMININO', 'MASCULINO', 'UNISSEX']
    while True:
        padrao_user = input('PADRÃO DESEJADO: ')
        if (padrao_user.isalpha()) == True:
            padrao_user = padrao_user.upper()
            if padrao_user in padroes_disponiveis:
                break
            else:
                print('Padrão não disponível. ')
        else:
            print('Inválido.')

    interesse = buscar_interesse(tamanho_user, padrao_user)
    if interesse == False: # se o retorno for false
        print('Não há roupas de acordo com seu interesse. ')