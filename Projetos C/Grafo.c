#include <stdio.h>
#include <stdlib.h>
#define true  1
#define false 2
typedef int boolean;
typedef int TIPOPESO;

typedef struct adjacencia {
    int vertice;
    TIPOPESO peso;
    struct adjacencia *prox;
} ADJACENCIA;

typedef struct vertice {
    // outros dados
    ADJACENCIA *cab;
} VERTICE;

typedef struct grafo{
    int vertices;
    int arestas;
    VERTICE *adj;
} GRAFO;

GRAFO *criarGrafo(int v){
    int i;
    GRAFO *g = (GRAFO *) malloc(sizeof(GRAFO));
    g->vertices = v;
    g->arestas = 0;
    g->adj = (VERTICE *) malloc(sizeof(VERTICE)* v);
    for (i=0;i<v;i++){
        g->adj[i].cab = NULL;
    }
    return (g);
}

ADJACENCIA *criaAdj(int v, int peso){
    ADJACENCIA *temp = (ADJACENCIA *) malloc(sizeof(ADJACENCIA));
    temp->vertice = v;
    temp->peso = peso;
    temp->prox = NULL;
    return (temp);
}

boolean criaAresta(GRAFO *gr,int vi, int vf, TIPOPESO p){
    if (!gr) return false;
    if ((vf<0) || (vf >= gr->vertices)) return false;
    if ((vi<0) || (vi >= gr->vertices)) return false;
    ADJACENCIA *novo = criaAdj(vf,p);
    novo->prox = gr->adj[vi].cab;
    gr->adj[vi].cab = novo;
    gr->arestas++;
    return true;
}

void imprime(GRAFO *gr){
    int i;
    printf("Vertices: %d, Arestas: %d\n",gr->vertices,gr->arestas);
    for (i=0;i<gr->vertices; i++){
        printf("v%d: ",i);
        ADJACENCIA *ad = gr->adj[i].cab;
        while(ad){
            printf("v%d(%d) ",ad->vertice, ad->peso);
            ad = ad->prox;
        }
        printf("\n");
    }
}

int main() {
	
	GRAFO *grafo = criarGrafo(5);
	criaAresta(grafo, 0, 1, 1);
	criaAresta(grafo, 1, 2, 10);
	criaAresta(grafo, 0, 3, 1);
	criaAresta(grafo, 2, 4, 15);
	
	imprime(grafo);
	
   return 0;
}
