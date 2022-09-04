#include <stdio.h>

int main(void) {
  int num;
  scanf("%d", &num);
  float matriz[num][3];
 
  for(int i= 0; i<num; i++){
    for(int j=0; j<3; j++){

      printf("Digite a nota: [%d][%d]", i, j);
      scanf("%f", &matriz[i][j]);
    }

  }
  float media;
  for(int i= 0; i<num; i++){
    media = (matriz[i][0] + matriz[i][1] +matriz[i][2]) /3.0;
    printf("A media é %.1f\n", media);

    }
 
 
  return 0;
}