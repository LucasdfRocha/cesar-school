#include <stdio.h>
 #include <string.h>
 #include <math.h>
 #include <stdlib.h>

char calculo(char valor[],int x){   

    for(int i = 0; i<strlen(valor);i++){

        if (valor[i] - 48 ==  x + 1 || valor[i] - 48 == x - 1){
            
            printf("sim");             
            exit(1);
        }     
    }     
    printf("nao"); 
} 

int main(){ 

  int x;
  char valor[50];

   scanf("%s %d",&valor,&x);          
  calculo(valor,x);           
}