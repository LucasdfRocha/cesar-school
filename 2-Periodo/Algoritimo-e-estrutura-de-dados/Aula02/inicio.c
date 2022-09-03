#include <stdio.h>


/****************************************************************************************
01. Considere cada operação:
a) x > 3 && x >= 10 || (! (x > 5)).
Quando x = 7, qual será a saída? 

resolução:
     7 > 3 && 7 >= 10 || (!(7>5))
           1 && 0 || 0
           0 || 0
              0
----------------------------------------------------------
b) (y == 7 && x > 3) || x < 9 && x + ++y < 3.
Quando x = 9 e y = 2, qual será a saída?

resolução:
(2 == 7 &&  9 > 3) || 9 < 9 && 9 + ++2 < 3
            (0 && 1) || 0 && 1
            0 || 0
--------------------------------------------------
02. Faça um programa em C que leia dois números inteiros (A e B), realize e exiba o
resultado dos seguintes cálculos.
a) A parte inteira da divisão entre os valores de A e B
b) O resto da divisão entre os valores de A e B
c) 35% do valor de B
****************************************************************************************/
int main(void) {

  int A,B,resultado,resto;
  float porcentagem;

  printf("Digite o valor de A: ");
  scanf("%d",&A);
  printf("Digite o valor de B: ");
  scanf("%d",&B);

  resultado = A/B;
  resto = A%B;
  porcentagem = 0.35 * B;

  printf("Divisao inteira igual a %d",resultado);
  printf("\nresto igual a %d ",resto);
  printf("\n35 porcento de B resulta em %f porcento",porcentagem); 
}