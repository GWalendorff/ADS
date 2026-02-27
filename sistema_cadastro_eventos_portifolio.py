# print ("Hello, World!")

# SISTEMA DE CADASTRO DE EVENTOS

from colorama import Fore, init
init (autoreset=True)
import os # HABILITA COMANDOS PARA TRABALHAR COM O SISTEMA OPERACIONAL.

def limpar_tela(): # RESPONSÁVEL POR LIMPAR O TERMINAL/CONSOLE.
    os.system('cls' if os.name == "nt" else 'clear')


def pausa(): # APÓS FINALIZAR UMA AÇÃO TANTO DE CADASTRO, DE VISUALIZAR EVENTOS, OU ETC, IRÁ PEDIR SE DESEJA CONTINUAR, E PARA CONTINUAR VOCÊ DEVE DIGITAR "ENTER".
    input(f"{Fore.BLACK} Digite ENTER para continuar...")

def exibir_menu(): # RESPONSÁVEL POR EXIBIR O MENU DO SISTEMA DE CADASTRO DE EVENTOS.
    print (f"{Fore.CYAN} =======> SISTEMA DE ORGANIZAÇÃO DE EVENTOS - UniFECAF <=======")
    print (f"{Fore.CYAN} 1. Cadastrar Evento.")
    print (f"{Fore.CYAN} 2. Atualizar Evento.")
    print (f"{Fore.CYAN} 3. Visualizar Eventos Disponíveis.")
    print (f"{Fore.CYAN} 4. Inscrever Aluno(a).")
    print (f"{Fore.CYAN} 5. Visualizar Inscrições.")
    print (f"{Fore.CYAN} 6. Cancelar Evento.")
    print (f"{Fore.CYAN} 7. SAIR.")


eventos = [] # "LISTA" CHAMADA DE EVENTOS, ONDE ARMAZENARÁ O HISTÓRICO DE EVENTOS.

def processar_opcao(opcao): # RESPONSÁVEL POR CHAMAR A OPÇÃO DESEJADA.
    if opcao == "1": # RESPONSÁVEL POR CADASTRAR EVENTO.
        nome_evento = input("Digite o nome do evento: ")
        data_evento = input("Digite a data do evento (DD/MM/AAAA): ")
        descricao_evento = input("Descrição do evento: ")
        try:
            vagas_evento = int(input("Digite o número maximo de vagas: "))
        except ValueError:
            print(f"{Fore.RED}Valor inválido para número de vagas. Tente novamente.")
            return  # ou repetir o input

        evento = { #CRIA UM DICIONÁRIO.
             "Nome": nome_evento,
             "Data": data_evento,
             "Descrição": descricao_evento,
             "Vagas": vagas_evento,
             "Inscritos": []
        }

        eventos.append(evento) # ".append" ADICIONA UM NOVO ELEMENTO NO FINAL DA LISTA.
        print(f"{Fore.GREEN} Evento cadastrado com sucesso!")

    elif opcao == "2": # OPÇÃO DE ATUALIZAR EVENTOS.
        if not eventos:
            print (f"{Fore.RED} Nenhum evento registrado.") # SE NÃO HOUVER EVENTOS REGISTRADOS APARECERÁ ESTA MENSAGEM.
            return
        
        else:
            novo_evento = input("Digite o nome evento a atualizar: ")
        
        for evento in eventos: # PERCORRE A LISTA "EVENTOS."
            if evento["Nome"].lower() == novo_evento.lower(): 
                nova_data_evento = input("Digite a nova data (DD/MM/AAAA): ")
                evento["Data"] = nova_data_evento # ATUALIZA A DATA.

                try:
                    novas_vagas_evento = int(input("Digite o novo número de vagas: "))
                    evento["Vagas"] = novas_vagas_evento #ATUALIZA NUMERO DE VAGAS.
                    print(f"{Fore.GREEN} Evento {novo_evento} atualizado com sucesso!") # RESPONSÁVEL POR CONFIRMAR SE O EVENTO FOI ATUALIZADO.
                except ValueError:
                    print(f"{Fore.RED} Valor inválido para número de vagas.") # RESPONSÁVEL POR AVISAR SE O VALOR DIGITADO FOR INVÁLIDO.
                break #SAI DO LOOP AO ENCONTRAR O EVENTO.
        else:
            print(f"{Fore.RED}Evento não encontrado no registro.") # SE NÃO HOUVER O NOME DO EVENTO DIGITADO, IRÁ APARECER ESTA MENSAGEM.

    elif opcao == "3": # RESPONSÁVEL POR VISUALIZAR EVENTOS.
        if not eventos:
            print (f"{Fore.RED} Nenhum evento cadastrado.") # SE NÃO HOUVER EVENTOS CADASTRADOS APARECERÁ ESTA MENSAGEM.

        else: 
            for i, evento in enumerate(eventos, 1): # LOOP USADO PARA PERCORRER CADA EVENTO DA LISTA EVENTOS, ENUMERANDO CADA UM.
                vagas_restantes = evento["Vagas"] - len(evento["Inscritos"])
                print (f"{Fore.CYAN}{i}. Evento: {evento['Nome']} - Dia: {evento['Data']}")
                print (f"{Fore.LIGHTCYAN_EX} Descrição: {evento['Descrição']}")
                print (f"{Fore.LIGHTCYAN_EX} Vagas restantes: {vagas_restantes}\n")
    
    elif opcao == "4": # RESPONSÁVEL POR INSCREVER ALUNOS AOS EVENTOS.
        if not eventos: # VERIFICA SE HÁ EVENTOS CADASTRADOS.
            print (f"{Fore.RED} Nenhum evento cadastrado para inscrição.")
            return 
        
        inscrever_evento = input("Por favor, digite o nome do evento desejado para inscrição: ")
        aluno = input("Seu nome: ")

        for evento in eventos:
            if evento['Nome'].lower() == inscrever_evento.lower(): # BUSCA O NOME DO EVENTO.
                if len(evento['Inscritos']) < evento['Vagas']: # VERIFICA SE HÁ VAGAS, E SE O ALUNO JA FOI INSCRITO OU NÃO.
                    if aluno not in evento['Inscritos']:
                        evento["Inscritos"].append(aluno) # SE ESTIVER TUDO CERTO, ELE ADICIONA O ALUNO.
                        print (f"{Fore.GREEN} Inscrição realizada com sucesso!")
                    else:
                        print (f"{Fore.RED} Sua inscrição neste evento já foi realizada.")
                else:
                    print (f"{Fore.RED} Inscrições esgotadas.")
                break
        else:
            print(f"{Fore.RED} Evento não encontrado.")
    
    elif opcao == "5": # VISUALIZAR INSCRIÇÕES.
        if not eventos: # VERIFICA SE HÁ EVENTOS.
            print (f"{Fore.RED}Nenhum evento cadastrado.")
            return # INTERROMPE A FUNÇÃO.

        visualizar_evento = input ("Digite o nome do evento para visualizar as inscrições: ") # LE O NOME DO EVENTO.
        for evento in eventos: 
            if evento['Nome'].lower() == visualizar_evento.lower(): # PERCORRE A LISTA DE EVENTOS, E MOSTRA A LISTA DE INSCRITOS SE ENCONTRAR.
                print (f"\n{Fore.CYAN} =======> INSCRITOS NO EVENTO - '{evento['Nome']}' <=======")
                if evento['Inscritos']:
                    for i, aluno in enumerate(evento['Inscritos'], 1): # MOSTRA OS INSCRITOS DE FORMA ENUMERADA, PARA FICAR MELHOR APRESENTADO.
                        print(f"{Fore.GREEN} {i}. {aluno}")
                else:
                    print(f"{Fore.YELLOW} Nenhum aluno inscrito ainda.")
                break
        else:
            print (f"{Fore.RED} Evento não encontrado.")


    elif opcao == "6": # CANCELAR EVCENTO.
        if not eventos: # VERIFICA SE HÁ EVENTOS.
            print(f"{Fore.RED}Nenhum evento cadastrado.")
            return

        evento_cancelar = input("Digite o nome do evento a cancelar: ")
        for evento in eventos: # PERCORRE LISTA DE EVENTOS.
            if evento["Nome"].lower() == evento_cancelar.lower(): 
                eventos.remove(evento) # REMOVE EVENTO ENCONTRADO.
                print (f"{Fore.GREEN} Evento cancelado com sucesso!")
                break
        else:
            print (f"{Fore.RED} Evento não encontrado.")

    else: # EXECUTA ESSA MENSAGEM CASO NÃO EXISTIR A OPÇÃO DIGITADA.
        print(f"{Fore.RED}Opção inválida. Tente novamente.")



def executar_sistema(): 
    while True: # ESSA ETAPA É RESPONSÁVEL POR REPETIR O MENU, ATÉ O MOMENTO QUE A PESSOA DECIDIR FECHÁ-LO, ESCOLHENDO A OPÇÃO "7".
        limpar_tela() 
        exibir_menu() # RESPONSÁVEL POR EXECUTAR O MENU.
        opcao = input("Digite a opção desejada: ")
        limpar_tela()

        if opcao == "7": # RESPONSÁVEL POR SAIR DO SISTEMA.
            print(f"{Fore.BLUE} Saindo do sistema...")
            break # USADO PARA ENCERRAR LOOP ATUAL.

        processar_opcao(opcao) # PROCESSA A OPÇÃO DESEJADA.
        pausa() # PAUSA, E APÓS APERTAR "ENTER", IRÁ CONTINUAR O LOOP.
        limpar_tela() # LIMPA TELA ANTES DE REINICIAR O LOOP.

executar_sistema() # REPONSÁVEL POR EXECUTAR O SISTEMA