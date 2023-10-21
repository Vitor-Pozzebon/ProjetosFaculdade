#include <stdio.h>
#include <time.h>
#include <unistd.h>

int main()
{
    int v[] = {1,2,3,55,8,55,10,66,47,10};
    int size = sizeof(v)/sizeof(v[0]);
    int key;

    clock_t start, end;
	double cpuTime = 0;

    //impressão dos dados do vetor original
    printf("\nVetor original: ");
    for(int i = 0; i < size; i++){
        printf(" %d", v[i]);
    }

    //pedido da chave ao usuário para pesquisa
    printf("\n\nDigite a chave que deseja conferir: ");
    scanf("%d", &key);

    start = clock();
    //estrutura para repetição de verificação dos valores
    for(int j = 0; j < size; j++){
        if(v[j] == key){
            printf("\n\nO numero %d encontra-se na posicao %d", key,j);
        }
    }

    printf("\nAguarde um momento...");
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado para a busca no vetor - Busca Sequencial: %f ms", cpuTime);
    
    return 0;
}