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

    #valor_da_divida = int(input("Entre com o valor da parcela: "))
    # abrir arquivo incc.csv
    ## Modos de abertura de arquivo: r (read), w (write), a (append)
    # ler as linhas do arquivo
    # separar as informações da linha
    # pegar o valor fator do incc
    
    arquivo = open("incc.csv", "r")
    arquivo_incc = []

    for linha in arquivo:
        linha = linha.strip()
        arquivo_incc.append(linha.split(","))

    parcela = 1000.00
    incc_inicio = float(arquivo_incc[3][2])
    incc_final = float(arquivo_incc[5][2])
    saldo_devedor = (parcela / incc_inicio * incc_final) 
    
    print(saldo_devedor)    

"""
    #valor_do_juros = 0
    incc_compra = 685.489
    incc_hoje = 845.268
    #igpm = 2.58
    
    
    incc_valor_compra = valor_da_divida * incc_compra
    incc_valor_hoje = valor_da_divida * incc_hoje
    # valor_da_parcela / incc_compra * incc_hoje
    print((valor_da_divida / incc_valor_compra) * incc_valor_hoje)
"""
if __name__ == "__main__":
    memoria_do_calculo()

