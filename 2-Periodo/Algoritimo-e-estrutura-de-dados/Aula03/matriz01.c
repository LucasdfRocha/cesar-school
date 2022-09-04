#include <stdio.h>

/********************

1. Faça um programa que leia o id e a idade de 5 funcionários 
de uma empresa. Utilize uma matriz para os dados. Imprima o id
do funcionário mais jovem e o mais velho.

*******************/
int main() {

    int mtr [5][2];
    int idMaior, idMenor, idadeMaior = 0, idadeMenor=500;

    for(int i= 0; i<5; i++){
        
        printf("Digite o id do funcionario e logo depois a idade: ");
        scanf("%d", &mtr[i][0]);
        scanf("%d", &mtr[i][1]);
    }

    for(int i= 0; i<5; i++){

        if(idadeMaior < mtr[i][1]){

            idMaior = mtr[i][0];
            idadeMaior = mtr[i][1];
        }

        if(idadeMenor > mtr[i][1]){

            idMenor = mtr[i][0];
            idadeMenor = mtr[i][1];
        }     
    }

    printf("id do mais velho: %d\n", idMaior);
    printf("id do mais novo %d", idMenor);

    return 0;
}