#include <stdio.h>
#include <stdlib.h>

void preencherVetor (int nV, int *vetor);
void imprimirVetor (int nV, int *vetor);
void preencherMatriz (int m, int nM, int *matriz);
void imprimirMatriz ();

int main(void) {
  system("clear");

  //declaração dos ponteiros
  int i, m, nV, nM;
  int *vetor;     //vetor
  int **matriz;    //matriz

  nV = 3;

  //Alocação de memória para o vetor de inteiros (nV posições)
  vetor = (int*) malloc (nV * sizeof(int));
  
  //alocação de memória para a matriz (m x nM)
  matriz = (int**) malloc (m * sizeof(int*));

  for (int i=0;i<m;i++) {
    matriz[i] = (int*) malloc (nM * sizeof(int));
  }
 
  //preencher o vetor
  preencherVetor(nV, vetor);
  
  //preencher a matriz
  preencherMatriz(m, nM, matriz);
  
  //imprimir o vetor
  imprimirVetor(nV, vetor);
  
  //impressão da matriz na tela
  imprimirMatriz();
  
  //liberar memória do vetor
  free(vetor);
  
  //liberar memória da matriz
  for (i=0;i<m;i++) {
    free(matriz[i]);
  }
  free(matriz);
  return 0;
}

void preencherVetor (int nV, int *vetor) {
  for (int i=0;i<nV;i++) {
    printf("\nvetor[%d] = ", i);
    scanf("%d", &vetor[i]);
  }
}

void imprimirVetor (int nV, int *vetor) {
  for (int i=0;i<nV;i++) {
    printf("\nvetor[%d] = %d ", i, vetor[i]);
  }
}