#include <stdio.h>
#include <stdlib.h>
#include <termios.h>
#include <unistd.h>
#include <time.h>
#include <poll.h> 
#include <fcntl.h> 
#include <errno.h>

typedef struct jogador {
       char nome[50];
       int score;
} tjogador;

int msleep(long msec) //usar milisegundos
{
    struct timespec ts;
    int res;

    if (msec < 0)
    {
        errno = EINVAL;
        return -1;
    }

    ts.tv_sec = msec / 1000;
    ts.tv_nsec = (msec % 1000) * 1000000;

    do {
        res = nanosleep(&ts, &ts);
    } while (res && errno == EINTR);

    return res;
}

int kbhit(void)  //verifica se alguma tecla está sendo pressionada
{
  struct termios oldt, newt;
  int ch;
  int oldf;
 
  tcgetattr(STDIN_FILENO, &oldt);
  newt = oldt;
  newt.c_lflag &= ~(ICANON | ECHO);
  tcsetattr(STDIN_FILENO, TCSANOW, &newt);
  oldf = fcntl(STDIN_FILENO, F_GETFL, 0);
  fcntl(STDIN_FILENO, F_SETFL, oldf | O_NONBLOCK);
 
  ch = getchar();
 
  tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
  fcntl(STDIN_FILENO, F_SETFL, oldf);
 
  if(ch != EOF)
  {
    ungetc(ch, stdin);
    return 1;
  }
 
  return 0;
}

int getch(void) //verifica a tecla sendo pressionada
{
    struct termios oldattr, newattr;
    int ch;
    tcgetattr( STDIN_FILENO, &oldattr );
    newattr = oldattr;
    newattr.c_lflag &= ~( ICANON | ECHO );
    tcsetattr( STDIN_FILENO, TCSANOW, &newattr );
    ch = getchar();
    tcsetattr( STDIN_FILENO, TCSANOW, &oldattr );
    return ch;
}

void Mapa(char mapa[20][20], int tamanho) //constrói o mapa
{
  int x,y;
  for(x=0; x<tamanho ;x++)
  {
    for(y=0; y<tamanho ;y++)
    {
      if(x == 0 || x == tamanho-1 || y == 0 || y == tamanho - 1)
      {
        mapa[x][y]= 'X';
      }
      else
      {
        mapa[x][y]= ' '; 
      }
    }
  }   
}

void PMapa(char mapa[20][20], int tamanho, int corpo) //printa o mapa na tela
{
  int x,y;
  for(x=0; x<tamanho ;x++)
  {
    for(y=0; y<tamanho ;y++)
    {
      printf("%c ",mapa[x][y]);      //impressão do mapa na tela
			
			if(x == 3 && y ==tamanho-1)     
			{
				printf("\t score %d", corpo-1);   
			}	
		}
    printf("\n");
  }
}

//Função para a cobra crescer - sempre pelo final do corpo
void Crescer(char movimento, char mapa[20][20], int px[100], int py[100], int *vcorpo, int *r) 
{
  system("clear");
  if (movimento == 'w') 
  {
    mapa[px[0]][py[0]] = '^';
  }
  if (movimento == 'a') 
  {
    mapa[px[0]][py[0]] = '<';
  }
  if (movimento == 's') 
  {
    mapa[px[0]][py[0]] = 'v';
  }
  if (movimento == 'd') 
  {
    mapa[px[0]][py[0]] = '>';
  }
  *vcorpo = *vcorpo + 1;
  *r = 1;
}

void movi(int corpo, int px[100], int py[100])
{
	for(int a=0; a < corpo; a++ )
	{
		px[corpo-a] = px[corpo-a-1];
		py[corpo-a] = py[corpo-a-1];
	}
}

//Função para a cobra andar
void Andar(int px[100], int py[100], int *corpo, char mapa[20][20], char *gameover, char movimento, int *res, char *oposto) 
{
  int vcorpo = *corpo; 
  int r = *res;
  switch(movimento)
  {
    //ANDAR PARA CIMA
    case 'w':
    *oposto = 's';
    if(mapa[px[0]-1][py[0]] == ' ')
    {
      mapa[px[vcorpo-1]][py[vcorpo-1]] = ' ';
      
			movi(vcorpo, px, py);
			
			
      px[0]--;
      mapa [px[0]][py[0]] = '^';

			system("clear");
      
    }
    else if(mapa[px[0]-1][py[0]] == 'O'){
    
			movi(vcorpo, px, py);
			px[0] = px[0]-1;
    	Crescer(movimento, mapa, px, py, &vcorpo, &r);
      *res = r;
      *corpo = vcorpo;
    } 
    else
    {
			system("clear");
      *gameover = 's';
    }    
    break;

    //ANDAR PARA ESQUERDA
    case 'a':
    *oposto = 'd';
    if(mapa[px[0]][py[0]-1] == ' ')
    {
      mapa[px[vcorpo-1]][py[vcorpo-1]] = ' ';
			movi(vcorpo, px, py);
      py[0]--;
      
      mapa [px[0]][py[0]] = '<';
      system("clear");
    }
		else if(mapa[px[0]][py[0]-1] == 'O'){
    	movi(vcorpo, px, py);
			py[0] = py[0]-1;
    	Crescer(movimento, mapa, px, py, &vcorpo, &r);
      *res = r;
      *corpo = vcorpo;
    }
    else
    {
			system("clear");
      *gameover = 's';
    }
    break;
    
    //ANDAR PARA BAIXO
    case 's':
		*oposto = 'w';
    if(mapa[px[0]+1][py[0]] == ' ')
    {
      mapa[px[vcorpo-1]][py[vcorpo-1]] = ' ';
      movi(vcorpo, px, py);
			px[0]++;
      
      mapa [px[0]][py[0]] = 'V';
      system("clear");
      break;
    }
    else if(mapa[px[0]+1][py[0]] == 'O'){
   	 	movi(vcorpo, px, py);
			px[0] = px[0] +1;
    	Crescer(movimento, mapa, px, py, &vcorpo, &r);
      *res = r;
      *corpo = vcorpo;
    } 
    else
    {
			system("clear");
      *gameover = 's';
    }
    break;
    
    //ANDAR PARA DIREITA
    case 'd':
    *oposto = 'a';
    if(mapa[px[0]][py[0]+1] == ' ')
    {
      mapa[px[vcorpo-1]][py[vcorpo-1]] = ' ';
      movi(vcorpo, px, py);
			py[0]++;
      
      mapa [px[0]][py[0]] = '>';
      system("clear");
    }
    else if(mapa[px[0]][py[0]+1] == 'O'){
    movi(vcorpo, px, py);
		py[0] = py[0]+1;
    Crescer(movimento, mapa, px, py, &vcorpo, &r);
    *res = r;
    *corpo = vcorpo;
    } 
    else
    {
			system("clear");
      *gameover = 's';
    }
    break;

    default:
    system("clear");
    break;
  }
}

void Fruta(int corpo, int tamanho, char *gameover, int *res, char mapa[20][20]) //Função para a fruta aparecer no mapa
{
  int fx, fy;
  if( corpo == (tamanho-2)*(tamanho-2))
  {
    *gameover = 'g';
  } 
  else
  {
		fx = rand()%(tamanho-1);
		fy = rand()%(tamanho-1);
		while(*res == 1){
			if(fx == 0 || fy == 0 || mapa[fx][fy] == '^' || mapa[fx][fy] == 'V' || mapa[fx][fy] == 'v' ||mapa[fx][fy] == '>' || mapa[fx][fy] == '<')
			{
				fx = rand()%(tamanho-1);
				fy = rand()%(tamanho-1);
			}
			else
			{
        *res = 0;
				mapa [fx][fy] = 'O';
			}
		}
  }
}

//A função Jogo Vai iniciar todas essas funções, fazendo o jogo começar 
void Jogo() {
  char mmovimento = 'd';
  char mmovimento_oposto ='a';
  char mmovimento_anterior = ' ';

  //Estrutura de arquivo para guardar o nome e a pontuação dos jogadores ao começarem o jogo
  tjogador j;
  FILE *arq;
  arq = fopen("dados.dat","r");
  fread(&j, sizeof(j), 1, arq);
  int panterior = j.score;
  fclose(arq);
  tjogador h[1];
  printf("\nDigite o nome: ");
  scanf(" %[^\n]", h[1].nome);
  
  
 

  int escolha;

  int x, y;
  int tamanho = 20;
  char mmapa[20][20];

  int px[100] = {1},py[100] = {1};
  
  char gameover = 'n';
  

  int corpo = 1;

  int r = 1;

  Mapa(mmapa, tamanho);
  Fruta(corpo, tamanho, &gameover, &r, mmapa);
  PMapa(mmapa, tamanho, corpo);
 
  while(1)    //loop infinito
  {
    while( gameover != 's' && gameover != 'g')  //"s" - perder ; "g" - ganhar
    {
      while(!kbhit() && gameover != 's' && gameover !=  'g') //ta sendo pressionado
      {
        Andar(px,py,&corpo, mmapa, &gameover, mmovimento, &r, &mmovimento_oposto);
        Fruta(corpo, tamanho, &gameover, &r, mmapa);
        PMapa(mmapa, tamanho, corpo);
        msleep(500);
      }
      mmovimento_anterior = mmovimento;
      mmovimento = getch();   //movimento passa a ser a tecla pressionada
      if(mmovimento_oposto == mmovimento)
      {
      mmovimento = mmovimento_anterior;
      }
      if(mmovimento != 'w' && mmovimento != 'a' &  mmovimento != 's' && mmovimento != 'd')
      {
        mmovimento = mmovimento_anterior;
      }
      
    }
    if(gameover == 's')
    {
      h[1].score = corpo-1;   //score no struct "jogador"
      if(h[1].score >= panterior)
      {
        arq = fopen("dados.dat","w+");
        fwrite(&h[1], sizeof(h[1]), 1, arq);
        fclose(arq);
      }
      
      printf("\n*************************************");
      printf("\n*            GAME OVER              *");
      printf("\n*      DESEJA JOGAR NOVAMENTE?      *");
      printf("\n*      (1) - Sim  (2) - Não         *");
      printf("\n*************************************");
    } 
    else if(gameover == 'g')
    {
      h[1].score = corpo-1;
      arq = fopen("dados.dat","w+");
      fwrite(&h[1], sizeof(h[1]), 1, arq);
      fclose(arq);
      printf("\n*************************************");
      printf("\n*     PARABÉNS, VOCÊ GANHOU!!!      *");
      printf("\n*      DESEJA JOGAR NOVAMENTE?      *");
      printf("\n*      (1) - Sim  (2) - Não         *");
      printf("\n*************************************");
    }
    escolha = getch();
    switch(escolha)
    {
      case '1':
      Jogo();
      return;
      case '2':
      system("clear");
      return;
      default:
      system("clear");
      printf("\n");
      printf("OPÇÃO INVÁLIDA");
      printf("\n");
      break;
    }
  }
}

void Menu()
{
  while (1)   //o "1" serve para fazer um loop infinito
  {
    int opcao;
    //Início do Menu com interface amigável
    printf("*********************************\n");
    printf("* BEM VINDO AO JOGO DA COBRINHA *\n");
    printf("*********************************\n ");
    printf("Escholha uma opção: \n");
    printf("\n");
    printf(" 1: Começar\n 2: Como jogar\n 3: Melhor Jogador\n 4: Sair \n");
    opcao = getch(); 
    system("clear");
    switch( opcao )   //análise  das opções escolhidas pelo jogador
    {
      case '1':     //inicia o jogo
      Jogo();
      return;

      case '2':     //mostra os comandos e as regras do jogo
      while(1)
      {
        printf(" COMANDOS:\n *Caps Lock deve estar desativado*\n •Andar para cima: w\n •Andar para baixo: s\n •Andar para a direita: d\n •Andar para a esquerda: a\n \n REGRAS:\n •Coma as frutas para aumentar de tamanho\n •Perde ao bater em si mesmo ou na parede\n \n REPRESENTAÇÕES: \n Cobra: V/^/</> \n Fruta: O \n Parede do mapa: X\n  \n Escholha uma opção:\n 1: Voltar\n 2: Sair\n");
        opcao = getch(); 
        if(opcao == '1')  //volta para o menu principal
        {
          system("clear");
          break;
        }
        else if (opcao == '2') //encerra o jogo (fecha o programa)
        {
          system("clear");
          return;
        }
        else 
        {
          system("clear");
          printf("Opção inválida\n");
        }
      }
      break;
      
      case '3':
      while(1)
      {
        tjogador j;
        FILE *arq;
        arq = fopen("dados.dat","a+");
        fread(&j, sizeof(j), 1, arq);
        printf("\nO(A) %s é o melhor jogador com um score de %d pontos \n Escholha uma opção:\n 1: Voltar\n 2: Sair\n",j.nome, j.score);
        opcao = getch(); 
        if(opcao == '1')  //volta para o menu principal
        {
          system("clear");
          fclose(arq);
          break;
        }
        else if (opcao == '2') //encerra o jogo (fecha o programa)
        {
          fclose(arq);
          system("clear");
          return;
        }
        else 
        {
          system("clear");
          printf("Opção inválida\n");
        }
      }
      break;
  
      case '4':     //encerra o jogo (fecha o programa)
      return;

      default:  //Caso a opção escolhida seja um número diferente de 1, 2 ou 3
      printf("Opção inválida\n");
      break;
    }
  }
  return;
}

int main(void) {

  FILE *arq;
  arq = fopen("dados.dat","a");
  fclose(arq);
  system("clear");
	srand(time(NULL));

  Menu();  //Chama a função Menu para o jogador escolher uma opção
  
  printf("\n*************************************");
  printf("\n* ESPERAMOS QUE VOCÊ VOLTE EM BREVE *");
  printf("\n*************************************");

  return 0;
}