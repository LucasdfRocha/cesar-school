#include <stdio.h>

/************************************************************************************
 
1° Questao:

a)
na versao 1 comecaremos da direita pra esquerda. comecamos peloo
ultimo indice. O 3 troca de lugar com o nove porque 3 < 9.
depois o 3 troca com o 4, o 3 troca denovo so que agora com o 7.
o 3 nao troca de lugar com o 1, o 1 troca de lugar com o 6,
depois o 8 troca de lugar com o 1,e por fim o 4 troca de lugar com o 1.

Como o 9 ja esta no ultimo, iremos comecar agora pelo penultimo indice, que é o valor 4.
4 é menor que 7, entao eles trocam de lugar, o 4 nao troca com o 3 porque ele é maior,
ja no 3, ele troca com o seu antecessor que é 6, e logo em seguida troca com o 8 e com 
o 4 tambem, parando so do lado do 1 (o 1 esta no index 0).

O 7 nao esta no lugar dele ainda, entao comparamos com seu antecessor que é o 4, e ele se mantem la,
ja quando comparamos o quatro com o 6, eles trocam de lugar, e logo depois o 4 troca denovo com o 8.
como 4 = 4, eles nao trocam de lugar.

o 7 continua nao trocando, o 6 troca de lugar com o 8 e nao acontece mais nada.

o 8 troca de lugar com o 7 e o vetor final fica assim:

1-3-4-4-6-7-8-9.


b)
que nem dito na letra a, comecaremos da direita pra esquerda.

comparando 23 e 53, notamos que 23 < 53 logo eles trocam de lugar. 53 < 72 , logo eles se mantem.
16 é menor que 72 entao havera a troca de lugaar. Como 4<72 entao eles trocam tambem. no resumo, o 72 
so para no index 1, depois do numero 78.

na proxima iteracao, o 23 se mantem porque é menor que 53, o 16 vai para o lugar do 53, e o 4 vai 
para o lugar do  53 tambem.depois de trocar com esses 2 numeros,o 53 tmb troca com o 47.So parando 
na ultima troca com o 32.

agora o 23 troca de lugar com o 23, o 4 troca de lugar com o 23 e o 23 fica parado depois da troca.
o 32 troca com o 47, que so faz 1 troca.

 e por fim, o 4 troca com o 16, ficando no ultimo index.

 vetor final fica:

 78-32-47-4-16-72-23-53.
------------------------------------------------------------------------------------
2)
************************************************************************************/
int main(){

 int vetor[9] = {4,8,6,1,7,4,9,3,5};


 for(int n= 1; n<=9 ; n++) {

    for(int j=0; j<9-1; j++) {
        if (vetor[j] > vetor[j+1] ) {

            int aux = vetor[j];
            vetor[j] = vetor[j+1];
            vetor[j+1] = aux;
            printf("indice: %d de valor %d -> indice:%d valor: %d\n",j,vetor[j + 1],j+1,vetor[j]);
        }
    }  
 }
printf("Vetor final:");
for(int i= 0; i<=8 ; i++) {
    printf(" %d ",vetor[i]);
}

    
}