# print ("Hello, World!") -Tem que ter esse sempre né professor! ;)

# NOME: GABRIEL AUGUSTO WALENDORFF

####################################################
print(
"""
Imobiliária R.M — Sistema de Orçamento de Aluguel
Projeto acadêmico — Algorithmic Thinking & Orientação a Objetos
""")
####################################################
from colorama import init, Fore, Back, Style # importa o módulo de formatação de cores para uma melhor exibição dos códigos no terminal
init(autoreset=True)
import csv                          # importa o módulo padrão de leitura e escrita de arquivos csv
import os                           # importa o módulo para interagir com o sistema operacional
from datetime import datetime       #importa a classe datetime para obter data e hora atual

from datetime import date                           # importa a classe date para trabalhar com datas
from dateutil.relativedelta import relativedelta    # importa relativedelta para somar os meses corretamente



####################################################
#          CLASSES — Orientação a Objetos          #
####################################################

class Imovel:                   # classe criada para qualquer tipo de imóvel, define estrutura e comportamentos comuns
    Valor_Contrato = 2000.00    # valor fixo do contrato imobiliário (R$ 2.000,00)
    Maximo_Parcelas = 5         # número máximo de parcelas do contrato
    Minimo_Parcelas = 1

    def __init__(self, tipo: str):      # executado ao criar um objeto Imovel
        self.tipo = tipo                # armazena o tipo de Imóvel (ex: "Apartamento", "Casa")
        self.valor_base = 0.0           # inicia o valor base do aluguel como zero
        self.extras = []                # inicia lista de adicionais (extras) vazia

    def calcular_aluguel(self) -> float:                            # método que deve ser implementado pelas subclasses
        raise NotImplementedError("Implemente em subclasse.")       # lança erro caso for chamado diretamente na classe base
    
    def resumo_extras(self) -> str:         # retorna os adicionaios como texto formatado
        if not self.extras:                 # verifica se a lista extra esta vazia
            return "Nenhum adicional."      # retorna mensagem padrão caso não tenha extras
        return "\n  ".join(self.extras)     # une os extras em uma string, separados por uma linha nova + espaços
    
    def __str__(self):                                                              # metodo especial: define representação em texto do objeto
        return f"Imóvel: {self.tipo} | Aluguel: R$ {self.calcular_aluguel():.2f}"   # retorna string com o tipo e o aluguel formatado com 2 casas decimais
    

class Apartamento(Imovel):                  # classe criada para apartamentos que terão 1 ou 2 quartos, garagem e desconto caso não haja crianças / subclasse que herda o Imovel e representa especificamente um apartamento
    Valor_Base = 700.00             # valor base mensal do apartamento
    Add_2_Quartos = 200.00          # valor adicional por ter 2 quartos
    Add_Garagem = 300.00            # valor adicional por ter garagem
    Desconto_sem_Crianca = 0.05     # desconto de 5% para inquilinos sem crianças

    def __init__ (self, quartos: int, garagem: bool, tem_criancas: bool):   # contrutor do apartamento: recebe número de quartos, se tem garagem e se tem criança 
        super().__init__("Apartamento")                                     # chama o construtor da classe pai (Imovel), passando tipo
        self.quartos = quartos                                              # armazenao número de quartos
        self.garagem = garagem                                              # armazena se o apartamento tem ou não garagem (True/False)
        self.tem_criancas = tem_criancas                                     # armazena se tem crianças (True/False)
        self.valor_base = self.Valor_Base                                   # define o valor base usando a constante da classe

    def calcular_aluguel(self) -> float:    # subscreve o método da classe pai (polimorfismo)
        total = self.valor_base             # começa o cálculo com o valor base
        self.extras = []                    # reseta a lista de extras a cada cálculo

        if self.quartos == 2:                                                   # verifica se tem 2 quartos no apartamentop
            total += self.Add_2_Quartos                                         # adiciona o valor de 2 quartos
            self.extras.append(f"2 quartos: + R$ {self.Add_2_Quartos:.2f}")     # registra o adicional na lista de extras como valor formatado

        if self.garagem:                                                      # verifica se tem garagem
            total += self.Add_Garagem                                         # adiciona o valor da garagem
            self.extras.append(f"Garagem: + R$ {self.Add_Garagem:.2f}")       # registra o adicional da garagem na lista
        
        if not self.tem_criancas:                               # verifica se NÃO há crianças (executa o desconto se for True)
            desconto = total * self.Desconto_sem_Crianca        # calcula o valor do desconto
            total -= desconto                                   # subtrai o desconto do total
            self.extras.append(f"Desconto sem crianças (5%): - R$ {desconto:.2f}")      # registra o desconto na lista

        return total                                                            # retorna o valor final calculado


class Casa(Imovel):                  # subclasse que herda de Imovel e representa uma casa
    Valor_Base = 900.00             # valor base mensal da casa
    Add_2_Quartos = 250.00          # valor adicional por 2 quartos
    Add_Garagem = 300.00            # valor adicional por garagem
   

    def __init__ (self, quartos: int, garagem: bool):   # contrutor do casa: recebe número de quartos, se tem garagem e se tem criança 
        super().__init__("Casa")                                     # chama o construtor da classe pai com o tipo "casa"
        self.quartos = quartos                                              # armazenao número de quartos
        self.garagem = garagem                                              # armazena se o apartamento tem ou não garagem (True/False)
        self.valor_base = self.Valor_Base                                   # define o valor base da casa

    def calcular_aluguel(self) -> float:    # implementação do cálculo para casa
        total = self.valor_base             # começa o cálculo com o valor base
        self.extras = []                    # reseta a lista de extras 

        if self.quartos == 2:                                                   # verifica se tem 2 quartos no apartamentop
            total += self.Add_2_Quartos                                         # adiciona o valor de 2 quartos
            self.extras.append(f"2 quartos: + R$ {self.Add_2_Quartos:.2f}")     # registra o adicional na lista de extras como valor formatado

        if self.garagem:                                                        # verifica se tem garagem
            total += self.Add_Garagem                                           # adiciona o valor da garagem
            self.extras.append(f"Garagem: + R$ {self.Add_Garagem:.2f}")       # registra o adicional da garagem na lista

        return total                                                            # retorna o valor final calculado


class Estudio(Imovel): # estúdio possui vagas de estacionamento variáveis / subclasse para estúdio, que cobra por vagas de estacionamento

    Valor_Base = 1200.00                
    Valor_Pacote_2_Vagas = 250.00       
    Valor_Vaga_Extra = 60.00            

    def __init__(self, vagas: int):             # construtor recebe apenas o número de vagas
        super().__init__("Estúdio")             # chama o construtor da classe pai com o tipo Estúdio
        self.vagas = vagas                      # armazena o número de vagas desejada
        self.valor_base = self.Valor_Base       # define o valor base do estúdio

    def calcular_aluguel(self) -> float:        # implementação do cálculo para Estúdio
        total = self.valor_base                 # inicia com valor base
        self.extras = []                        

        if self.vagas >= 2:                                                                             # se tem 2 ou mais vagas, aplica o pacote
            total += self.Valor_Pacote_2_Vagas                                                          # adiciona o valor do pacote de 2 vagas
            self.extras.append(f"{Fore.WHITE}Pacote 2 vagas: + R$ {self.Valor_Pacote_2_Vagas:.2f}")                 # registra o pacote de vagas
            
            vagas_extras = self.vagas - 2                                                               # calcula quantas vagas extras existem além das 2 do pacote
            if vagas_extras > 0:                                                                        # se houver vagas extras além das 2 do pacote
                adicional = vagas_extras * self.Valor_Vaga_Extra                                        # multiplica vagas extras pelo valor unitário
                total += adicional                                                                      # adiciona o custo nas vagas extras
                self.extras.append(f"{Fore.WHITE}{vagas_extras} vaga(s) extra(s): + R$ {adicional:.2f}")            # registra as vagas extras e o valor cobrado
        elif self.vagas == 1:                                                                       # se tem exatamente 1 vaga, cobra o pacote mínimo de 2
            total += self.Valor_Pacote_2_Vagas                                                      # cobra o pacote mínimo mesmo com 1 vaga
            self.extras.append(f"{Fore.WHITE}1 vaga (pacote mínimo 2): + R$ {self.Valor_Pacote_2_Vagas:.2f}")   # informa o cliente que 1 vaga cobra o pacote ínimo de 2

        elif self.vagas == 0:
            self.extras.append(f"{Fore.RED}Sem vagas de estacionamento.")

        return total                                                                                # retorna o valor calculado
        

class Orcamento: # exibe o orçamento completo com parcelas do contrato / classe responsável por montar, exibir e exportar o orçamento final
    def __init__(self, imovel: Imovel, parcelas_contrato: int, nome_cliente: str):      # contrutor: recebe o imóvel escolhido, número de parcelas e nome do cliente
        self.imovel = imovel                                                            # armazena o objeto imóvel ("Casa", "Apartamento", "Estúdio")
        self.parcelas_contrato = min(parcelas_contrato, Imovel.Maximo_Parcelas)         # garante que as parcelas n ultrapassemo máximo parmitido usando min()
        self.nome_cliente = nome_cliente                                                # armazena nome do cliente
        self.data = datetime.now().strftime("%d/%m/%Y  %H:%M")                          # obtém a data e hora atual fomatada como: DIA/MÊS/ANO  HORA:MINUTOS

        self.valor_parcela_contrato = (Imovel.Valor_Contrato / self.parcelas_contrato) # calcula o valor de cada parcela do contrato dividindo o valor total pela quantidade de parcelas

        self.aluguel_mensal = self.imovel.calcular_aluguel()                            # chama o método do imóvel uma vez e guarda o resultado como atributo normal


    def exibir(self):            # exibe o orçamento formatado no terminal
        sep = "=" * 55           # cria uma linha separadora com 55 sinais de "="
        print(f"{Fore.WHITE}\n{sep}")        # Imprime linha separadora com linha em branco antes
        print(f"{Fore.BLUE}     IMOBILIÁRIA R.M — ORÇAMENTO DE ALUGUEL")       # título do orçamento
        print(f"{Fore.WHITE}\n{sep}")        # separador
        print(f"{Fore.CYAN} Cliente      :{Fore.WHITE} {self.nome_cliente}")           # exibe nome do cliente
        print(f"{Fore.CYAN} Data         :{Fore.WHITE} {self.data}")           # exibe a data e hora do orçamento
        print(f"{Fore.CYAN} Imóvel       :{Fore.WHITE} {self.imovel.tipo}")           # exibe tipo de imóvel
        print(f"{Fore.CYAN} Valor base   :{Fore.WHITE} R$ {self.imovel.valor_base:.2f}")        # exibe valor base formatado
        print(f"{Fore.CYAN}\nAdicionais : ")           # cabeçalho da seção de adicionais
        print(f"{Fore.WHITE}{self.imovel.resumo_extras()}")  # exibe os extras calculados
        print(f"{Fore.WHITE}{sep}")          # separador
        print(f"{Fore.CYAN} ALUGUEL MENSAL TOTAL : {Fore.WHITE}R$ {self.aluguel_mensal:.2f}")       # total do aluguel
        print(f"{Fore.WHITE}{sep}")          # separador
        print(f"{Fore.CYAN} CONTRATO IMOBILIÁRIO : {Fore.WHITE}R$ {Imovel.Valor_Contrato:.2f}")     # valor total do contrato
        print(f"{Fore.CYAN} Parcelado em {Fore.WHITE}{self.parcelas_contrato}x de R$ {self.valor_parcela_contrato:.2f}")     # exibe o parcelamento do contrato
        print(f"{Fore.WHITE}{sep}")          # separador


    def gerar_csv(self):        # gera um arquivo CSV com as 12 parcelas do orçamento
        nome_arquivo = f"orcamento_{self.nome_cliente.replace(' ', '_').lower()}.csv"   # cria o nome do arquivo substituindo por "_" e convertendo para minúsculo
        caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)     # monta caminho completo do arquivo na mesma pasta do script

        with open(caminho, "w", newline="", encoding="utf-8") as f:     # abre ou cria o arquivo CSV pára escrita, sem quebras de linhas extras, em UTF-8
            writer = csv.writer(f)   # cria o objeto escritor de CSV
            writer.writerow([
                    "Parcela", "Mês/Ano", "Aluguel (R$)",
                "Parcela Contrato (R$)", "Total Mensal (R$)"
            ])      # escreve a linha do cabeçalho com os nomes das colunas

            data_base = date.today()                            # obtém a data atual como data de partida

            for i in range(1, 13):                              # loop de 1 a 12 (12 meses de contrato)
                mes = data_base + relativedelta(months=i - 1)   # calcula o mês correspondente à parcela i
                mes_str = mes.strftime("%m/%Y")                 # formata o mês como "Mês/Ano"
                parcela_contrato = self.valor_parcela_contrato if i <= self.parcelas_contrato else 0.0  # se ainda estiver dentro do número de parcelas do contrato, usa o valor, senão, zero
                total_mes = self.aluguel_mensal + parcela_contrato     # soma aluguel + parcela do contrato
                writer.writerow([
                    i, mes_str,
                    f"{self.aluguel_mensal:.2f}",
                    f"{parcela_contrato:.2f}",
                    f"{total_mes:.2f}",
                ])      # escreve uma linha no CSV com: número de parcela, mês, aluguel, parcela contrato e total

        print (f"{Fore.GREEN}\n  ✅ CSV gerado: {nome_arquivo}")
        return caminho      # retorna o caminho do arquivo criado
    

####################################################
#             Interface de Terminal                #
####################################################

def menu_int(msg: str, minimo: int, maximo: int) -> int:         # solicita ao usuário um número inteiro dentro de um intervalo válido
    while True:                                                  # loop infinito até receber entrada válida
        try:
            val = int(input(msg))                                # exibe a mensagem e tenta converter a entrada para inteiro
            if minimo <= val <= maximo:                          # verifica se o valor está dentreo do intervalo permitido
                return val                                       # retorna o valor válido e encerra o loop
            print (f"{Fore.WHITE} Digite um número entre {minimo} e {maximo}.")     # avisa sobre intervalor inválido
        except ValueError:                                                          # erro se o usuário digitar algo que não é número
            print (f"{Fore.WHITE} Entrada inválida. Digite um número.")             # avisa sobre entrada não numérica

def menu_sim_nao(msg: str) -> bool:                                         # função que solicita uma resposta SIM/NÃO e retorna True ou False
    while True:                                                             # loop até entrada válida
        r = input(msg).strip().upper()                                      # lê a entrada, remove espaços e converte em maiúsculas
        if r in ("S", "SIM"):                                               # verifica se a resposta é afirmativa
            return True                                                     # retorna True para "SIM"
        if r in ("N", "NÃO", "NAO"):                                        # verifica se a resposta é negativa
            return False                                                    # retorna False para "NÃO"
        print(f"{Fore.WHITE} Digite (S) para SIM e (N) para Não.")          # avisa sobre a entrada invlaida


def coletar_imovel() -> Imovel:             # função que exibe o menu de tipos de imóvel e retorna o objeto correspondente
    print (f"{Fore.BLUE}\n Tipos de Imóvel: ")                     # cabeçalho
    print (f"{Fore.WHITE} [1] Apartamento — Valor base R$ 700,00 / quarto")    # exibe opção de apartamento
    print (f"{Fore.WHITE} [2] Casa        — Valor base R$ 900,00 / quarto")    # exibe opção de casa
    print (f"{Fore.WHITE} [3] Estúdio     — Valor base R$ 1.200,00")           # exibe opção de estúdio
    escolha = menu_int("  Escolha (1-3): ", 1, 3)                   # escolha do tipo (1 a 3)

    if escolha == 1:                                                # se a escolha foi Apartamento
        quartos = menu_int(" Número de quartos (1 ou 2): ", 1, 2)   # solicita número de quartos
        garagem = menu_sim_nao(" Deseja garagem? (S/N) ")           # pergunta se tem garagem
        criancas = menu_sim_nao(" Possui crianças? (S/N) ")         # pergunta se tem crianças
        return Apartamento(quartos, garagem, criancas)              # cria e retorna objeto Apartamento


    elif escolha == 2:                                                                # se o usuário escolheu Casa
        quartos = menu_int(" Número de quartos (1 ou 2): ", 1, 2)                   # solicita número de quartos
        garagem = menu_sim_nao(" Deseja garagem? (S/N) ")                           # pergunta sobre garagem
        return Casa(quartos, garagem)                                               # cria e retorna objeto Casa
    
    else:                                                                           # se o usuário escolheu Estúdio (a opção 3)
        vagas = menu_int(" Quantas vagas de estacionamento? (0 a 10): ", 0, 10)     # solicita número de vagas
        return Estudio(vagas)                                                       # cria e retorna objeto Estúdio
    

def main():                                                         # função principal, ponto de entrada do programa, coordena toda a execução
    print(f"{Fore.WHITE}\n" + "=" * 55)                             # imprime linha separadora
    print(f"{Fore.BLUE}    IMOBILIÁRIA R.M — SISTEMA DE ORÇAMENTO") # exibe título  do sistema
    print(f"{Fore.WHITE}" + "=" * 55)                             # linha separadora

    nome = input(f"{Fore.BLUE}\n  Nome do cliente: ").strip() or "Cliente"   # lê o nome do cliente, ou se vazio, usa "cliente"

    imovel = coletar_imovel()           # chama a função que coleta o tipo de imóvel e retorna objeto

    parcelas = menu_int(
        f"   Parcelas do contrato (1 a {Imovel.Maximo_Parcelas}): ",
        1, Imovel.Maximo_Parcelas
    )                                       # solicita o número de parcelas do contrato, entre 1 e o máximo de 5

    orcamento = Orcamento(imovel, parcelas, nome)        # cria o objeto Orcamento com os dados coletados
    orcamento.exibir()                                   # exibe o orçamento completo

    if menu_sim_nao(f"{Fore.WHITE}\n  Deseja gerar o arquivo CSV com as 12 parcelas? (S/N):"):  # pergunta se o usuário quer gerar o CSV
        orcamento.gerar_csv()   # gera o arquivo CSV  com o cronograma

    print (f"{Fore.YELLOW}\n  Obrigado por utilizar o sistema da Imobiliária R.M!")      # mensagem de encerramento
    print (f"{Fore.WHITE}\n" + "=" * 55)

if __name__ == "__main__":  # verificar se o script está sendo executado diretamente
    main()                  # chama a função principal para iniciar o programa