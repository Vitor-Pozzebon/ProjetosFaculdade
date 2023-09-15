#include <stdio.h>
#include <time.h>

void jurosCompostos(float v, int p, float t, float a = 0, int c = 1, float vIn = 0){
	float vt = t/100;
	float vInicioOp;
	
	//calculo dos juros compostos
	if(a == 0 && c == 1){
		printf("\n\n*** CALCULO SEM O APORTE MENSAL ***");
		vIn = v;
	}
	if(a != 0 && c == 1){
		printf("\n\n*** CALCULO COM O APORTE MENSAL ***");
		vIn = v;
	}
	
	vInicioOp = v;
	v = v + (v * vt);
	printf("\nO valor depois do %d mes sera de R$ %.2f", c, v);
	printf("\nO lucro desse mes foi no valor de R$ %.2f", v - vInicioOp);
	printf("\n------------------------------------------------------------------");
	v += a;
	
	if(c == p){
		printf("\n==================================================================");
		printf("\nO valor final apos %d meses com taxa de %.2f sera R$ %.2f", p, t, v);
		printf("\n==================================================================");
		printf("\nA diferenca entre o valor final e o inicial do investimento e de R$ %.2f", v - vIn);
		printf("\n==================================================================");
	}
	
	if(c < p){
		c++;
		jurosCompostos(v, p, t, a, c, vIn);
	}
}

int main(){
	
	float valor;
	int periodo;  //em meses
	float taxa;
	float aporte;
	clock_t inicio, fim;
	double tempoTotal = 0;
	//int cont = 0;
	
	printf("\nDigite o valor que deseja investir: ");
	scanf("%f", &valor);
	printf("\nDigite o periodo (em meses) que deseja verificar os juros: ");
	scanf("%d", &periodo);
	printf("\nDigite a taxa que sera aplicada ao valor: ");
	scanf("%f", &taxa);
	printf("\nDigite o valor do aporte mensal para comparacao: ");
	scanf("%f", &aporte);
	printf("==================================================================");
	
	//inicio da contagem de tempo
	inicio = clock();
	jurosCompostos(valor, periodo, taxa);
	jurosCompostos(valor, periodo, taxa, aporte);
	fim = clock();
	
	tempoTotal = (double)(fim - inicio) / CLOCKS_PER_SEC;
	
	printf("\nO tempo total de execucao foi de %f segundos", tempoTotal);
	
	return 0;
}
