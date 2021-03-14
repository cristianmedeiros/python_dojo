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

    """
    mes,ano,fator
    8,1994,100
    9,1994,100.381
    10,1994,101.71
    11,1994,104.11
    """    
    
    arquivo = open("incc.csv", "r")   #abre o arquivo em modo leitura
    arquivo_incc = []

    for linha in arquivo: #passa pelas linhas do aruivo
        linha = linha.strip() #remove espaços e caracteres especiais
        arquivo_incc.append(linha.split(",")) #quebra a linha em cada virgula, e adiciona no array arquivo_incc

    parcela = 1000.00 #Valor inicial da parcela, esse valor poderia vir de um input do usuario
    
    data_inicio = "{},{}".format(9,2008).split(",") #Esse valor podemos definir na mao, ou pegar do input do usuario
    data_inicio_mes = data_inicio[0]
    data_inicio_ano = data_inicio[1]

    data_fim = "{},{}".format(12,2008).split(",") #Esse valor podemos definir na mao, ou pegar do input do usuario
    data_fim_mes = data_fim[0]
    data_fim_ano = data_fim[1]
    
    range_incio = 0
    for linha_i in arquivo_incc:
        if linha_i[0] == data_inicio_mes and linha_i[1] == data_inicio_ano:
            print(linha_i)
            break
        range_incio = range_incio + 1

    range_fim = 0
    for linha_f in arquivo_incc:
        if linha_f[0] == data_fim_mes and linha_f[1] == data_fim_ano:
            print(linha_f)
            break
        range_fim = range_fim + 1
    
    
    #range_incio = 0000 #Esse valor deve vir da data de inicio
    #range_fim = 0000 #Esse valor deve vir da data de fim
    ##                                  ###
    ##  TEMOS QUE RESOLVER A DEFAZAGEM  ###
    ##                                  ###

    for periodo in range(range_incio,range_fim):
        incc_inicio = float(arquivo_incc[periodo][2])
        incc_final = float(arquivo_incc[periodo + 1][2])
        
        print("inicio {} - final {}".format(incc_inicio, incc_final))
        
        parcela = (parcela / incc_inicio * incc_final) 
        
        print(parcela)

if __name__ == "__main__":
    memoria_do_calculo()

"""
git status - lista os arquivos que foram alterados
git add NOMEDOARQUIVO - adiciona os arquivos que foram alterados
git commit -m MENSAGEMDECOMMIT - Envia os arquivos alterados para o repositorio local, com a mensagem das alterações
git push origin master - Envia os arquivos do repositorio local para o repositorio remoto
"""