#include <stdio.h>
#include <stdlib.h>

int main(void) {
  float num1, num2, res;
  char op;
  system("clear");
  printf("      CALCULADORA      ");
  printf("\n* * * * * * * * * * *");
  printf("\n* 7   8   9   +     *");
  printf("\n* 4   5   6   -     *");
  printf("\n* 1   2   3   *     *");
  printf("\n* 0           /     *");
  printf("\n* * * * * * * * * * *");

  while (op != 's'){
    printf("\n\nDigite o número 1: ");
    scanf("%f", &num1);
    printf("Digite o número 2: ");
    scanf("%f", &num2);
    printf("Digite o operador: ");
    scanf(" %c", &op);
    
    switch (op) {
    case '+':
    res=num1+num2;
    printf("\n* * * * * * * * * * *");
    printf("\nResultado: %.2f", res);
    printf("\n* * * * * * * * * * *");
    break;

    case '-':
    res=num1-num2;
    printf("\n* * * * * * * * * * *");
    printf("\nResultado: %.2f", res);
    printf("\n* * * * * * * * * * *");
    break;

    case '*':
    res=num1*num2;
    printf("\n* * * * * * * * * * *");
    printf("\nResultado: %.2f", res);
    printf("\n* * * * * * * * * * *");
    break;

    case '/':
      if (num2==0){
        printf("\n* * * * * * * * * * * * * * * * *");
        printf("\nDivisão por 0 não permitida!");
        printf("\n* * * * * * * * * * * * * * * * *");
      }
      else{
        res=num1/num2;
        printf("\n* * * * * * * * * * *");
        printf("\nResultado: %.2f", res);
        printf("\n* * * * * * * * * * *");
      }
      break;

      default:
      printf("Operador inválido!");
  }

  }
  system("clear");
  printf("\n* * * * * * * * * * *");
  printf("\nPrograma encerrado");
  printf("\n* * * * * * * * * * *");
  
  return 0;
}