#include <stdio.h>

int main(){
    int n;
    printf("Quantos itens voce deseja inserir? ");
    scanf("%d",&n);

    int soma = 0;
    float valor = 0;
    float matriz[n][2];


    for (int i = 0; i<n;i++){
        for (int j = 0; j<2;j++){

            scanf("%f",&matriz[i][j]);
            soma += matriz[i][1];

            if(matriz[i][1] > 100){

                valor += (matriz[i][1] * matriz[i][0])/100;
                
            }
        }
    }
    printf("O total de gramas foi de %dg e o valor total foi de %.2f reais",soma,valor);
    
    
    return 0;
}