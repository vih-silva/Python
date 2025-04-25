investimentoInicial = float(input("imforme o investimento inicial: "))
taxaDesconto = float(input("Informe a taxa de desconto: "))

contador = 1
quantidadefluxosCaixa = int(input("Quantos anos você tem previsto de fluxo de caixa"))
valorpresenteLiquido = 0

while contador <= qndFluxosCaixa:
    faturamento = float(input(f"Digite o valor do faturamento do ano (contador): "))
    valorpresenteLiquido += faturamento / (1 + taxaPorcentagem) ** contador
    contador += 1



if (valorpresneteliquido - investimentoIicial) > 0:
    print(f"Seu porjeto é viavél")
else:
    print(f"Seu projeto é inviável")
