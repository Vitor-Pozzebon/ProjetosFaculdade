//busca em largura
#include <stdio.h>
#include <stdlib.h>
#define true 1
#define false 2
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

// Fila Din
typedef int TIPOCHAVE;
typedef struct
{
    TIPOCHAVE chave;
    // outros campos ...
} REGISTRO;

typedef struct aux
{
    REGISTRO reg;
    struct aux *prox;
} ELEMENTO, *PONT;

typedef struct
{
    PONT inicio;
    PONT fim;
} FILA;

void inicializarFila(FILA *f)
{
    f->inicio = NULL;
    f->fim = NULL;
}

boolean inserirNaFila(FILA *f, REGISTRO reg)
{
    PONT novo = (PONT)malloc(sizeof(ELEMENTO));
    novo->reg = reg;
    novo->prox = NULL;
    if (f->inicio == NULL)
        f->inicio = novo;
    else
        f->fim->prox = novo;
    f->fim = novo;
    return true;
}

boolean excluirDaFila(FILA *f, REGISTRO *reg)
{
    if (f->inicio == NULL)
        return false;
    *reg = f->inicio->reg;
    PONT apagar = f->inicio;
    f->inicio = f->inicio->prox;
    free(apagar);
    if (f->inicio == NULL)
        f->fim = NULL;
    return true;
}

// fim Fila Din

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
        printf("chave(%d) v%d: ", gr->adj[i].chave, i);
        ADJACENCIA *ad = gr->adj[i].cab;
        while (ad)
        {
            printf("v%d(%d) ", ad->vertice, ad->peso);
            ad = ad->prox;
        }
        printf("\n");
    }
}

void visitaL(GRAFO *g, int s, boolean *expl)
{
    FILA f;
    inicializarFila(&f);
    expl[s] = true;
    REGISTRO *u = (REGISTRO *)malloc(sizeof(REGISTRO));
    u->chave = s;
    inserirNaFila(&f, *u);
    while (f.inicio)
    {
        excluirDaFila(&f, u);
        ADJACENCIA *v = g->adj[u->chave].cab;
        while (v)
        {
            if (!expl[v->vertice])
            {
                expl[v->vertice] = true;
                u->chave = v->vertice;
                inserirNaFila(&f, *u);
            }
            v = v->prox;
        }
    }
    free(u);
}

void largura(GRAFO *g, int proc)
{
    boolean expl[g->vertices];
    int i;
    boolean f = 2;
    for (i = 0; i < g->vertices; i++)
    {
    	if(g->adj[i].chave == proc){
    		printf("\nValor %d encontrado no vertice v%d", proc, i);
    		f = 1;
    		break;
		}
        expl[i] = false;
    }
    if(f == false){
    	printf("\nValor %d nao encontrado", proc);
	}
    for (i = 0; i < g->vertices; i++)
    {
        if (!expl[i])
            visitaL(g, i, expl);
    }
}

int main()
{
	int valores[5] = {10,11,12,13,14};
	GRAFO *grafo = criarGrafo(5, valores);
	
	criaAresta(grafo, 0, 1, 1);
	criaAresta(grafo, 1, 2, 1);
	criaAresta(grafo, 2, 3, 1);
	criaAresta(grafo, 2, 4, 1);
	criaAresta(grafo, 4, 3, 1);
	
	imprime(grafo);
	
	largura(grafo, 10);
	largura(grafo, 13);
	largura(grafo, 5);
	return 0;
}
