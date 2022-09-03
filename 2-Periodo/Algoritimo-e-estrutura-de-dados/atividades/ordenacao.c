#include <stdio.h>

/************************************************************************************
 
1° Questao:

Algoritimo de ordenacao nada mais é que um manipulador de dados 
que põem elementos de uma sequencia em uma certa ordem (crescente ou decrescente).

É importante pelo fato de que o algoritimo muitas das vezes é capaz de 
diminuir a complexidade do codigo, tornando-o algo mais compacto do que ter
que ficar repetindo varias condicionais.
---------------------------------------------------------------------------------
2° Questao:

insertion sort nada mais é do que um algoritimo que percorre um vetor
da esquerda da direita e  sempre vai comecar do index > 0 porque ele compara
o valor com o seu antecessor. se o valor for menor, ele troca de lugar com
seu antecessor ate chegar na posicao que o seu antecessor for menor que ele,
criando assim, uma ordenacao.

a)  Pularemos o 10 porque ele esta no indice 0.

    iremos comparar o valor 23 com seu antecessor, o 10
    como 23>10 logo o 23 nao sai do seu index.

    ja no 8, ele ira trocar de posicao com o 23 e logo
    depois com o 10 tambem, porque 8<23 e 8<10, resultando
    no 8 estando no index 0, 10 no index 1 e o 23 no index 2.

    Comparando o 73 com o 23, ele é maior, logo continuara
    no index 3.

    por fim, o 44 ira trocar de lugar com o 73 e ficando no 
    index 3, pelo fato dele ser maior que o 23 e menor que o 73.

    o vetor ficou: [0]:8;[1]:10;[2]:23;[3]:44;[4]:73.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
b)  vamos pular o 9.

    54 vai para o indice 0 porque 54>9.

    32 vai para o lugar do 9 (index 1) e
    nao troca de lugar com o 54 porque 32<54.

    o 87 troca com o 9, depois com o 32 e por ultimo
    com o 54, porque 87 maior q todos os numeros citados,
    com o vetor atualmente ficando: 87,54,32,9...

    59 troca de lugar com o 9,depois com o 32 e por fim 
    com o 54, visto que é maior que 54 e menor que o 87.

    o 75 vai trocar com o 9, depois com o 32, depois o 54,
    troca com o 59 e fica no index 1 porque é menor que 87.

    com isso, o vetor ficou: [0]:87;[1]:75;[2]:59;[3]:54;[4]:32;[5]:9.


************************************************************************************/



int  main(){

  int vetor[7], vetor2[7];

    for(int i = 0; i < 7; i++){

        printf("Digite o %d salario : ",i + 1);
        scanf("%d", &vetor[i]);

    }

    for(int i=0;i<7;i++){

        int j=i;

        while((vetor[j] < vetor[j-1]) && j > 0){

        int aux = vetor[j-1];
        vetor[j-1] = vetor[j];
        vetor[j] = aux;
        --j;
        }
    }

  printf("Crescente: "); 

  for(int i = 0; i < 7; i++){

    printf("%d ", vetor[i]);
  }
  for(int i = 0; i < 7; i++) {

      vetor2[i] = vetor[7-i-1];
  }
  printf("\nDecrescente: ");

  for(int i = 0; i < 7; i++) {

    printf("%d ", vetor2[i]);
  }
}