#include <stdio.h>
#include <time.h>
#include <unistd.h>

//função para fazer a busca binária
void buscaBinaria(int vetor[], int tamanho, int chave) {
    int encontrou = 0;
    int inicio = 0;
    int fim = tamanho - 1;

    while (inicio <= fim && encontrou == 0) {
        int meio = (inicio + fim) / 2;

        if (vetor[meio] == chave) {
            encontrou = 1;

            // Mostra a posição do elemento encontrado
            printf("\nElemento %d encontrado na posicao %d\n", chave, meio);

            int cont = 1;
            while(vetor[meio-cont] == chave){
                printf("\nElemento %d encontrado na posicao %d\n", chave, meio-cont);
                cont++;
            }

            cont = 1;
            while(vetor[meio+cont] == chave){
                printf("\nElemento %d encontrado na posicao %d\n", chave, meio+cont);
                cont++;
            }

            // Procura por mais ocorrências à esquerda
            fim = meio - 1;
        } else if (vetor[meio] < chave) {
            inicio = meio + 1;
        } else {
            fim = meio - 1;
        }
    }

    if (encontrou == 0) {
        printf("\n\nElemento %d nao encontrado no vetor.\n", chave);
    }
}

//função bubblesort para ordenar os elementos do vetor
void bubbleSort(int *vec, int s){
    int aux;
    for(int v1 = 0; v1 < s; v1++){
       for(int v2 = 0; v2 < s; v2++){
            if(vec[v1] < vec[v2]){
                aux = vec[v1];
                vec[v1] = vec[v2];
                vec[v2] = aux;
            }
       }
    }
}

int main()
{
    int v[] = {1,2,3,55,8,55,10,66,47,10,11,22,11,10};
    int size = sizeof(v)/sizeof(v[0]);
    int key;

    clock_t start, end;
	double cpuTime = 0;

    //impressão dos dados do vetor original
    printf("\nVetor original: ");
    for(int i = 0; i < size; i++){
        printf(" %d", v[i]);
    }

    //pedido da chave de verificação para o usuário
    printf("\n\nDigite a chave que deseja procurar: ");
    scanf("%d", &key);

    start = clock();
    //função para ordenar o vetor
    bubbleSort(v, size);

    //impressão dos dados do vetor ordenado
    printf("\nVetor ordenado: ");
    for(int j = 0; j < size; j++){
        printf(" %d", v[j]);
    }

    //verificação das condições para impressão dos valores repetidos
    buscaBinaria(v, size, key);

    printf("\nAguarde um momento...");
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado para a busca no vetor - Busca Sequencial: %f ms", cpuTime);
    
    return 0;
}