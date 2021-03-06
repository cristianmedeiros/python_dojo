# tres planilhas
# 1 atualizada pelo incc - em obra
# empreendimento pronto - parcela atualizada pelo IGPM
# Compra na planta - Converte do incc para IGPM
# mes da conversado do indice
# data da compra
# vencimento da parcela
# Calculo valido até
# Calculo juros e encargos

# 1. Calculo do fator do incc
# 2. Calculo do fator do igpm

# Ler arquivo com idice do incc
# Ler arquivo com idice do igpm

# 3. data de inicio dos pagamentos
# 4. prazo total da divida
# 5. valor total da dívida
# 6. valor de cada parcela até o vencimento da dívida

# Mes de conversao do indice

# ler o historico de fatores do incc de um arquivo
# ler o historico de fatores do igpm de um arquivo

# Gerar arquivo com a memoria de calculo

def memoria_do_calculo():
    
    arquivo = open("incc.csv", "r")   #abre o arquivo em modo leitura
    arquivo_incc = []

    for linha in arquivo: #passa pelas linhas do aruivo
        linha = linha.strip() #remove espaços e caracteres especiais
        arquivo_incc.append(linha.split(",")) #quebra a linha em cada virgula, e adiciona no array arquivo_incc

    parcela = 1000.00 #Valor inicial da parcela, esse valor poderia vir de um input do usuario
    
    print("Qual a data da compra")
    data_inicio = pede_data() #Esse valor podemos definir na mao, ou pegar do input do usuario
    data_inicio_mes, data_inicio_ano  = captura_data(data_inicio) 
    
    print("Qual o vencimento da parcela")
    data_venc_dia, data_venc_mes, data_venc_ano = data_completa() #Esse valor podemos definir na mao, ou pegar do input do usuario
    print("dia {}, mes {}, ano {}".format(data_venc_dia, data_venc_mes, data_venc_ano))
    
    print("Qual a data base do cálculo")
    data_fim = pede_data()
    data_fim_mes, data_fim_ano = captura_data(data_fim)
    
    
        
    range_incio = intervalo(data_inicio_mes, data_inicio_ano, arquivo_incc)
    range_fim = intervalo(data_fim_mes, data_fim_ano, arquivo_incc)
    
    ##### Tratamento de parcela atrasada ####
    #Data de vencimento da parcela#
    #Multa é sempre 2%
    #Juros é 1% ao mes dividido pela quantidade de dias em atraso

    for periodo in range(range_incio, range_fim):
        incc_inicio = float(arquivo_incc[periodo][2])
        incc_final = float(arquivo_incc[periodo + 1][2])
        
        print("inicio {} - final {}".format(incc_inicio, incc_final))
        
        parcela = (parcela / incc_inicio * incc_final) 
        
        print(parcela)


def captura_data(data, defazagem=2):
    data_vec = data.split(",")
    data_vec[0] = int(data_vec[0]) - defazagem
    data_vec[1] = int(data_vec[1])

    if data_vec[0] == -1:
        data_vec[0] = 11
        data_vec[1] = data_vec[1] - 1

    if data_vec[0] == 0:
        data_vec[0] = 12
        data_vec[1] = data_vec[1] - 1 
        
    return data_vec[0], data_vec[1]

def intervalo(data_mes,data_ano,arquivo_incc):
    periodo = 0
    for linha_i in arquivo_incc:
        if int(linha_i[0]) == data_mes and int(linha_i[1]) == data_ano:
            print(linha_i)
            break
        periodo = periodo + 1
    return periodo

def data_completa():
    data = input("Informe a data: ")
    return fatias(data)

def fatias(data_completa):
    data_completa_inicio_calculo = data_completa.split("/")
    data_completa_inicio_calculo_dia = int(data_completa_inicio_calculo[0])
    data_completa_inicio_calculo_mes = int(data_completa_inicio_calculo[1])
    data_completa_inicio_calculo_ano = int(data_completa_inicio_calculo[2])
    return data_completa_inicio_calculo_dia, data_completa_inicio_calculo_mes, data_completa_inicio_calculo_ano
    

def pede_data():
    data_mes = input("Qual o mes do periodo? ")
    data_ano = input("Qual o ano do periodo? ")
    data = "{},{}".format(data_mes.strip(),data_ano.strip())
    return data
       

if __name__ == "__main__":
    memoria_do_calculo()

"""
git status - lista os arquivos que foram alterados
git add NOMEDOARQUIVO - adiciona os arquivos que foram alterados
git commit -m MENSAGEMDECOMMIT - Envia os arquivos alterados para o repositorio local, com a mensagem das alterações
git push origin master - Envia os arquivos do repositorio local para o repositorio remoto
"""