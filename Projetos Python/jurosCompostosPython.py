import time
import os

os.system("cls")

def jurosCompostos(v, p, t, a=0, c=1, vIn=0):
    vt = t / 100
    vInicioOp = 0
    
    # cálculo dos juros compostos
    if a == 0 and c == 1:
        print("\n\n*** CALCULO SEM O APORTE MENSAL ***")
        vIn = v
    if a != 0 and c == 1:
        print("\n\n*** CALCULO COM O APORTE MENSAL ***")
        vIn = v
    
    vInicioOp = v
    v = v + (v * vt)
    print(f"O valor depois do {c} mes sera de R$ {v:.2f}")
    print(f"O lucro desse mes foi no valor de R$ {v - vInicioOp:.2f}")
    print("------------------------------------------------------------------")
    v += a
    
    if c == p:
        print("==================================================================")
        print(f"O valor final apos {p} meses com taxa de {t:.2f} sera R$ {v:.2f}")
        print("==================================================================")
        print(f"A diferenca entre o valor final e o inicial do investimento e de R$ {v - vIn:.2f}")
        print("==================================================================")
    
    if c < p:
        c += 1
        jurosCompostos(v, p, t, a, c, vIn)

def main():
    valor = float(input("Digite o valor que deseja investir: "))
    periodo = int(input("Digite o periodo (em meses) que deseja verificar os juros: "))
    taxa = float(input("Digite a taxa que sera aplicada ao valor: "))
    aporte = float(input("Digite o valor do aporte mensal para comparacao: "))
    
    inicio = time.time()
    jurosCompostos(valor, periodo, taxa)
    jurosCompostos(valor, periodo, taxa, aporte)
    fim = time.time()
    
    tempoTotal = fim - inicio
    
    print(f"O tempo total de execucao foi de {tempoTotal:.6f} segundos")

if __name__ == "__main__":
    main()