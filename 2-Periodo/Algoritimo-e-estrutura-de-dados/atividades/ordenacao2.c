    #include <stdio.h>

    int main(){

        int vetor[13] = {80,2,26,9,80,2,39,23,44,22,13,14,4};
        int maior = 0;
        int contador = 0,contadorMen = 0;
        int menor = 2000;

        for (int i = 0; i < 13; i++){

            int j = i;

            while (vetor[j] < vetor[j-1] && j > 0)
            {
                int aux = vetor[j-1];
                vetor[j-1] = vetor[j];
                vetor[j] = aux;
                --j;
            }

            if (vetor[j] > maior){
                maior = vetor[j];
                
            }
            else if (vetor[j] == maior){
                contador = contador + 1; 
                }
             if (vetor[j] < menor){
                menor = vetor[j];
                
            }
            else if (vetor[j] == menor){
                contadorMen = contadorMen + 1; 
                }
             
        }

        for (int i = 0; i < 13; i++)
        {

            printf("%d ",vetor[i]);
        }

        printf("\nO maior numero %d repete  %d vezes",maior,contador + 1);
        printf("\nO menor numero %d repete %d vezes\n",menor,contadorMen + 1);
        printf("numero central do vetor: %d", vetor[6]);

        return 0;
    }