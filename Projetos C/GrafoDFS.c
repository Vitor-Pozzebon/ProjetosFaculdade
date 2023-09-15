#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 2
#define BRANCO 0
#define AMARELO 1
#define VERMELHO 2
typedef int boolean;
typedef int TIPOPESO;

typedef struct adjacencia
{
    int vertice;
    TIPOPESO peso;
    struct adjacencia *prox;
} ADJACENCIA;

typedef struct vertice
{
    // outros dados
    int chave;
    ADJACENCIA *cab;
} VERTICE;

typedef struct grafo
{
    int vertices;
    int arestas;
    VERTICE *adj;
} GRAFO;

GRAFO *criarGrafo(int v, int *val)
{
    int i;
    GRAFO *g = (GRAFO *)malloc(sizeof(GRAFO));
    g->vertices = v;
    g->arestas = 0;
    g->adj = (VERTICE *)malloc(sizeof(VERTICE) * v);
    for (i = 0; i < v; i++)
    {
    	g->adj[i].chave = val[i];
        g->adj[i].cab = NULL;
    }
    return (g);
}

ADJACENCIA *criaAdj(int v, int peso)
{
    ADJACENCIA *temp = (ADJACENCIA *)malloc(sizeof(ADJACENCIA));
    temp->vertice = v;
    temp->peso = peso;
    temp->prox = NULL;
    return (temp);
}

boolean criaAresta(GRAFO *gr, int vi, int vf, TIPOPESO p)
{
    if (!gr)
        return false;
    if ((vf < 0) || (vf >= gr->vertices))
        return false;
    if ((vi < 0) || (vi >= gr->vertices))
        return false;
    ADJACENCIA *novo = criaAdj(vf, p);
    novo->prox = gr->adj[vi].cab;
    gr->adj[vi].cab = novo;
    gr->arestas++;
    return true;
}

void imprime(GRAFO *gr)
{
    int i;
    printf("Vertices: %d, Arestas: %d\n", gr->vertices, gr->arestas);
    for (i = 0; i < gr->vertices; i++)
    {
        printf("chave (%d) v%d: ", gr->adj[i].chave, i);
        ADJACENCIA *ad = gr->adj[i].cab;
        while (ad)
        {
            printf("v%d(%d) ", ad->vertice, ad->peso);
            ad = ad->prox;
        }
        printf("\n");
    }
}

void visitaP(GRAFO *g, int u, int *cor)
{
    cor[u] = AMARELO;
    ADJACENCIA *v = g->adj[u].cab;
    while (v)
    {
        if (cor[v->vertice] == BRANCO)
            visitaP(g, v->vertice, cor);
        v = v->prox;
    }
    cor[u] = VERMELHO;
}

void profundidade(GRAFO *g, int proc)
{
    int cor[g->vertices];
    int u;
    boolean f = 2;
    for (u = 0; u < g->vertices; u++)
    {
    	if(g->adj[u].chave == proc){
    		printf("\nValor %d encontrado no vertice v%d", proc, u);
    		f = 1;
    		break;
		}
        cor[u] = BRANCO;
    }
    if(f == false){
    	printf("\nValor %d nao encontrado", proc);
	}
    for (u = 0; u < g->vertices; u++)
    {
        if (cor == BRANCO)
            visitaP(g, u, cor);
    }
    
}

int main()
{
	int valores[5] = {10,20,30,40,50};
	GRAFO *grafo = criarGrafo(5, valores);
	criaAresta(grafo, 0, 1, 1);
	criaAresta(grafo, 1, 2, 1);
	criaAresta(grafo, 1, 4, 1);
	criaAresta(grafo, 2, 3, 1);
	criaAresta(grafo, 2, 4, 1);

	imprime(grafo);
	
	profundidade(grafo, 10);
	profundidade(grafo, 11);
	profundidade(grafo, 30);
	
	return 0;
}
