# print ("Hello, World!")

# ========= SISTEMA DE CONTROLE DE ESTOQUE =========
# ==> Loja de ELETRÔNICOS.

# => ADICIONAR PRODUTOS.
# => ATUALIZAR PRODUTOS.
# => VIZUALIZAR ESTOQUE.
# => REGISTRAR VENDAS.
# => CANCELAR VENDAS.
# => HISTÓRICO DE VENDAS.
# => FATURAMENTO.

from colorama import Fore, init # RESPONSÁVEL POR "SETAR" CORES EM MENSAGENS NO TERMINAL.
import os # IMPORTA A BIBLIOTECA "OS", ONDE ME PERMITIU USAR A FUNÇÃO DE LIMPAR TERMINAL.
init (autoreset=True)

def limpar_tela(): # RESPONSÁVEL POR LIMPAR O TERMINAL/CONSOLE.
    os.system('cls' if os.name == "nt" else 'clear') 

def pausa(): # APÓS FINALIZAR UMA AÇÃO TANTO DE CADASTRO, DE VISUALIZAR ESTOQUE, OU ETC, IRÁ PEDIR SE DESEJA CONTINUAR, E PARA CONTINUAR VOCÊ DEVE DIGITAR "ENTER".
    input(f"{Fore.BLACK} Digite ENTER para continuar...")

def exibir_menu(): # RESPONSÁVEL POR EXIBIR O MENU.
    print (f"{Fore.CYAN} =======> SISTEMA DE CONTROLE DE ESTOQUE - LOJA DE ELETRÔNICOS <=======")
    print (f"{Fore.CYAN} 1. Visualizar Estoque.")
    print (f"{Fore.CYAN} 2. Adicionar Produto.")
    print (f"{Fore.CYAN} 3. Atualizar Produto.")
    print (f"{Fore.CYAN} 4. Registrar Venda.")
    print (f"{Fore.CYAN} 5. Cancelar Venda.")
    print (f"{Fore.CYAN} 6. Histórico de Vendas.")
    print (f"{Fore.CYAN} 7. Faturamento.")
    print (f"{Fore.CYAN} 8. SAIR.")

produtos = {} # "DICIONÁRIOS" CHAMADO PRODUTOS, ONDE GUARDARÁ OS ITENS CADASTRADOS NO ESTOQUE.
vendas= [] # "LISTA" CHAMADA DE VENDAS, ONDE ARMAZENARÁ O HISTÓRICO DE VENDAS.

def processar_opcao(opcao): # RESPONSÁVEL POR CHAMAR A OPÇÃO DESEJADA.
    if opcao == "1": 
        if not produtos:
            print (f"{Fore.RED} Nenhum produto cadastrado.") # SE NÃO HOUVER PRODUTOS CADASTRADOS APARECERÁ ESTA MENSAGEM.
        else:
            print (f"{Fore.CYAN} =======> ESTOQUE <=======")
            print ("\n Produtos disponíveis:") # SE HOUVER PRODUTOS CADASTRADOS, IRÁ APARECER ESTA MENSAGEM.
            # for nome, info in produtos.items(): # PERCORRE OS PRODUTOS CADASTRADOS NO DICIONARIO "PRODUTOS".
            for i, (nome, info) in enumerate(produtos.items(), 1): # "enumerate" USADO PARA PERCORRE A LISTA PRODUTOS, ENUMERNADO ELA EM (1, 2, 3...).
                print (f"{Fore.GREEN} {i}. Produto: {nome}  |  Quantidade: {info['Quantidade']}  | Valor Unitário: R$ {info['Preço']:.2f}")
                # A INFORMAÇÃO A CIMA LHE DARÁ O NOME DO PRODUTO, SUA QUANTIDADE E VALOR UNITÁRIO.

    if opcao == "2": # RESPONSÁVEL POR ADICIONAR PRODUTOS A LISTA, JUNTAMENTE COM SUA QUANTIDADE E VALOR.
        nome = input("Digite o nome do produto: ") # ADICIONA O NOME DO PRODUTO.
        if nome in produtos:
            print (f"{Fore.GREEN}Produto já cadastado. ") # AFIRMA QUE O PRODUTO FOI CADASTRADO.
        else:
            try:
                qtd = int(input("Digite a quantidade do produto: ")) # ADICIONA A QUANTIDADE QUE VOCÊ ESCOLHER.
                preco = float(input("Digite o preço do produto: ")) # ADICIONA O PREÇO QUE VOCÊ ESCOLHER.
                produtos[nome]= {"Quantidade": qtd, "Preço": preco} # ADICIONA DADOS DO PRODUTO NO SISTEMA.
                print (f"{Fore.GREEN}Produto {nome} cadastrado com sucesso!")
            except ValueError:
                print (f"{Fore.RED}Quantidade e preço inválidos!") # CASO HAJA ALGUMA FALHA NO CADASTRO DO PRODUTO, ESTA MENSAGEM IRÁ APARECER.

    elif opcao == "3":

            print (f"{Fore.CYAN} =======> ESTOQUE <=======")
            print ()
            for i, (nome, info) in enumerate(produtos.items(), 1): # "enumerate" USADO PARA PERCORRE A LISTA PRODUTOS, ENUMERNADO ELA EM (1, 2, 3...).
                print (f"{Fore.GREEN} {i}. Produto: {nome}  |  Quantidade: {info['Quantidade']}  | Valor Unitário: R$ {info['Preço']:.2f}")

            print ()
            nome = input("Digite o nome do produto a atualizar: ")

            if nome not in produtos: # SE NÃO HOUVER O PRODUTO LISTADO EM ESTOQUE.
                print (f"{Fore.RED} Produto não encontrado.")
                return # RESPONSÁVEL POR ENCERRAR A AÇÃO, PARA ELA NÃO CONTINUAR E DAR ERRO.
            
            try:
                nova_qtd = int(input("Digite a nova quantidade: ")) # RESPONSÁVEL POR PEDIR A NOVA QUANTIDADE.
                produtos[nome]['Quantidade'] = nova_qtd # ATUALIZA A QUANTIDADE ANTIGA (qtd) PARA A NOVA (nova_qtd).

                alterar_preco = input("Deseja alterar o preço? (s/n): ") # RESPONSÁVEL POR PEDIR SE DESEJA ALERAR O "PREÇO".

                if alterar_preco == "s": # PARA "s" ELE IRÁ PEDIR O "PREÇO" NOVO.
                    novo_preco = float(input("Novo preço: R$ "))
                    produtos[nome]['Preço'] = novo_preco # ATUALIZA O PREÇO ANTIGO (preco) PARA O NOVO (novo_preco).
                    print(f"{Fore.GREEN}Produto '{nome}' atualizado com nova quantidade e novo preço!") # INFORMA A ALTERAÇÃO NA QUANTIDADE, MANTENDO O PREÇO.
                else:
                    print(f"{Fore.GREEN}Produto '{nome}' atualizado com nova quantidade. {Fore.YELLOW}Preço mantido: R$ {produtos[nome]['Preço']:.2f}") # INFORMA A ALTERAÇÃO NA QUANTIDADE E NO PREÇO.
            except ValueError:
                print("Valor numérico inválido.")

    elif opcao == "4":
        print (f"{Fore.CYAN} =======> ESTOQUE <=======")
        print ()
        for i, (nome, info) in enumerate(produtos.items(), 1): # "enumerate" USADO PARA PERCORRE A LISTA PRODUTOS, ENUMERNADO ELA EM (1, 2, 3...).
                print (f"{Fore.GREEN} {i}. Produto: {nome}  |  Quantidade: {info['Quantidade']}  | Valor Unitário: R$ {info['Preço']:.2f}")

        print()
        nome = input("Produto vendido (ou 'cancelar' para fechar esta opção): ").strip() # SOLICITA O NOME DO PRODUTO VENDIDO, PORÉM CASO QUEIRA SAIR DESTA OPÇÃO SÓ DIGITAR "CANCELAR".
        if nome.lower() == "cancelar": # ".lower" TRASNFORMA TODOS OS CARACTERES DA STRING PARA MINÚSCULAS.
            print(f"{Fore.YELLOW} Registro de venda cancelado.")
            return

        if nome not in produtos: # RESPONSÁVEL POR VERIFICAR SE EXISTE O PRODUTO DIGITADO.
            print(f"{Fore.RED} Produto não encontrado.")
            return

        try:
            qtd = int(input("Digite a quantidade vendida: ")) # PEDE PARA DIGITAR A QUANTIDADE VENDIDA.
            if qtd <= 0: # SE A QUANTIDADE FOR ZERO OU NEGATIVA, MOSTRA O ERRO E SAI DA FUNÇÃO.
                print(f"{Fore.RED} Quantidade deve ser positiva.")
                return

            if produtos[nome]['Quantidade'] < qtd: # VERIFICA SE O ESTOQUE POSSUI A QUANTIDADE SUFICIENTE PARA VENDER, SE NÃO TIVER, MOSTRA "ESTOQUE INSIFICIENTE".
                print(f"{Fore.RED}Estoque insuficiente. Disponível: {produtos[nome]['Quantidade']}")
                return

            produtos[nome]['Quantidade'] -= qtd # SUBTRAI A QUANTIDADE VENDIDA DO ESTOQUE.
            total = qtd * produtos[nome]['Preço'] # CALCULA O VALOR TOTAL DA VENDA (QUANTIDADE * VALOR UNITÁRIO).
            vendas.append({"Produto": nome, "Quantidade": qtd, "Total": total})
            print(f"{Fore.GREEN} Venda registrada com sucesso: {qtd} x {nome} - Total: R$ {total:.2f}") # REGISTRA A VENDA, NA LISTA "VENDAS", GUARDANDO O PRODUTO, QUANTIDADE E VALOR TOTAL.

        except ValueError:
            print(f"{Fore.RED} Quantidade inválida.")

    elif opcao == "5":
        if not vendas: # VERIFICA SE HÁ VENDAS REGISTRADAS, SE NÃO HOUVER ENVIA A MENSAGEM ABAIXO.
            print(f"{Fore.RED} Nenhuma venda registrada.")
            return

        print (f"{Fore.CYAN} =======> VENDAS REGISTADAS <=======")
        print ()
        for i, venda in enumerate(vendas, 1): # MOSTRA O HISTÓRICO DE VENDAS E OS PRODUTOS.
            print (f"{Fore.GREEN}{i}. Produto: {venda['Produto']} | Quantidade: {venda['Quantidade']} | Total: R$ {venda['Total']:.2f}")
        
        print()
        nome_cancelar = input("Produto a cancelar: ").strip().lower() # SOLICITA O NOME DO PRODUTO A CANCELAR.
        try:
            qtd_cancelar = int(input("Quantidade a cancelar: ")) # SOLICITA A QUANTIDADE A CANCELAR DO PRODUTO.
        except ValueError:
            print(f"{Fore.RED} Quantidade inválida.")
            return
        
        for venda in vendas: # ONDE OCORRE O CANCELAMENTO DA VENDA.
            nome = venda['Produto'] # PERCORRE A LISTA VENDAS.
            if venda['Quantidade'] >= qtd_cancelar: # VERIFICA SE DA PRA CANCELAR A QUANTIDADE DESEJADA
                venda['Quantidade'] -= qtd_cancelar # SUBTRAI A QUANTIDADE DO PRODUTO.
                produtos[nome]['Quantidade'] += qtd_cancelar # DEVOLVE A QUANTIDADE QUE FOI SUBTRAIDA PARA O ESTOQUE.
                venda ['Total'] = venda['Quantidade'] * produtos[nome]['Preço'] # CALCULA O NOVO VALOR TOTAL DE VENDAS.
                print (f"{Fore.GREEN} Cancelado {qtd_cancelar} unidade(s) de '{nome}'.")

                if venda['Quantidade'] == 0: # SE A QUANTIDADE VIRAR "0", CANCELA O REGISTRO DE VENDA DO PRODUTO.
                    vendas.remove(venda)
                    print (f"{Fore.GREEN} Registro de vendas removido, pois a quantidade chegou a ZERO.")
                return
            else: # VERIFICA SE A QUANTIDADE A SE CANCELAR É VALIDA.
                print (f"{Fore.RED} Quantidade a cancelar é acima do que a quantidade vendida.")
                return
        print (f"{Fore.RED} Produto não encontrado em vendas.")

    elif opcao == "6":
        if not vendas:
            print (f"{Fore.RED} Nenhuma venda registrada.") # SE NÃO HOUVER VENDAS REGISTRADAS.
            return
        else:
            print (f"{Fore.CYAN} =========> HISTÓRICO DE VENDAS <=========") # SE HOUVER HISTÓRICO DE VENDAS, IRÁ APARECER ESTA MENSAGEM.
            print()
            for i, venda in enumerate(vendas, 1):  # PERCORRE A LISTA VENDA, ENUMERNADO ELA EM (1, 2, 3...).
                print (f"{Fore.GREEN}{i}. Produto: {venda['Produto']}  |  Quantidade: {venda['Quantidade']}  |  Preço total: R$ {venda['Total']:.2f}")
        

    elif opcao == "7":
        if not vendas:
            print (f"{Fore.RED} Nenhuma venda registrada.") # SE NÃO HOUVER VENDAS REGISTRADAS.
            return
        faturamento_total = sum(venda["Total"] for venda in vendas) # CALCULA O VALOR TOTAL RECEBIDO ATRAVÉS DAS VENDAS FEITAS.
        print (f"{Fore.GREEN} Faturamento total: R$ {faturamento_total:.2f}")


def executar_sistema(): 
    while True: # ESSA ETAPA É RESPONSÁVEL POR REPETIR O MENU, ATÉ O MOMENTO QUE A PESSOA DECIDIR FECHÁ-LO, ESCOLHENDO A OPÇÃO "8".
        limpar_tela()
        exibir_menu()
        opcao = input("Digite a opção desejada: ")
        

        if opcao == "8":
            print(f"{Fore.BLUE} Saindo do sistema...")
            break # USADO PARA ENCERRAR LOOP ATUAL, DECIDI POR ELE E NÃO O "exit()", QUE EU HAVIA COLOCADO DE PRIMEIRA, POIS VI QUE ERA MAIS SEGURO E IDEAL PARA SISTEMAS CONTÍNUOS.

        processar_opcao(opcao)
        pausa()
        limpar_tela()

executar_sistema() # REPONSÁVEL POR EXECUTAR O SISTEMA


# =========== Finalização feita pela primeira vez (ABAIXO), porém pesquisando e vendo mais alguns vídeos entendi que usando  "while True" e
# finalizar usando "break" era uma situação mais segura, de melhor abordagem e eficiência. ===========

    # if opcao == "8":
    #     print (f"{Fore.BLUE}Saindo do sistema...")
    #     exit()
#     else:
#         print (f"{Fore.RED}Opção inválida!")


# def executar_sistema():
#     exibir_menu()
#     opcao = input("Digite a opção desejada: ")
#     limpar_tela()
#     processar_opcao(opcao)
#     pausa()
#     limpar_tela()
#     executar_sistema()

# executar_sistema()