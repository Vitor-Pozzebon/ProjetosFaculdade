#include <stdio.h>
#include <time.h>
#include <unistd.h>

void bubbleSort(int *v, int s){
	int i, j, aux;
	for(i = 0; i < s-1; i++){
		for(j = 0; j < s-1; j++){
			if(v[j] > v[j+1]){
				aux = v[j];
				v[j] = v[j+1];
				v[j+1] = aux;
			}
		}
	}
	printf("\nVetor Ordenado Bubble Sort: ");
	for(i = 0; i < s; i++){
		printf(" %d", v[i]);
	}
}

void insertion_sort(int *v, int s) {
    int i, key, j;
    for (i = 1; i < s; i++) {
        key = v[i];
        j = i - 1;

        // Move os elementos do v[0..i-1] que são maiores que a key
        // para uma posição à frente de sua posição atual
        while (j >= 0 && v[j] > key) {
            v[j + 1] = v[j];
            j = j - 1;
        }
        v[j + 1] = key;
    }
    printf("\nVetor Ordenado Insertion Sort: ");
    for(i = 0; i < s; i++){
    	printf(" %d", v[i]);
	}
}

int main(){
	
	int vector1[6] = {10,18,5,3,90,33};
	int vector2[6] = {20,30,40,50,60,88};
	int vector3[6] = {1,2,3,4,6,5};
	int vector4[18] = {10,18,5,3,90,33,1,2,3,4,6,5,30,40,50,60,88,0};
	
	clock_t start, end;
	double cpuTime = 0;
	
	//contagem de tempo do vetor 1
	printf("==== VETOR 1 ====");
	int sizeV = sizeof(vector1)/sizeof(vector1[0]);
	start = clock();
	bubbleSort(vector1, sizeV);
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Bubble Sort para o vetor 1: %f ms", cpuTime);
    
    start = clock();
	insertion_sort(vector1, sizeV);
	sleep(1);
	end = clock();
	
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Insertion Sort para o vetor 1: %f ms", cpuTime);
    printf("\n---------------------------------------------------------------------------");
    
    //contagem de tempo do vetor 2
	printf("\n==== VETOR 2 ====");
	sizeV = sizeof(vector2)/sizeof(vector2[0]);
	start = clock();
	bubbleSort(vector2, sizeV);
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Bubble Sort para o vetor 2: %f ms", cpuTime);
    
    start = clock();
	insertion_sort(vector2, sizeV);
	sleep(1);
	end = clock();
	
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Insertion Sort para o vetor 2: %f ms", cpuTime);
    printf("\n---------------------------------------------------------------------------");
    
    //contagem de tempo do vetor 3
	printf("\n==== VETOR 3 ====");
	sizeV = sizeof(vector3)/sizeof(vector3[0]);
	start = clock();
	bubbleSort(vector3, sizeV);
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Bubble Sort para o vetor 3: %f ms", cpuTime);
    
    start = clock();
	insertion_sort(vector3, sizeV);
	sleep(1);
	end = clock();
	
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Insertion Sort para o vetor 3: %f ms", cpuTime);
    printf("\n---------------------------------------------------------------------------");
    
    //contagem de tempo do vetor 4
	printf("\n==== VETOR 4 ====");
	sizeV = sizeof(vector4)/sizeof(vector4[0]);
	start = clock();
	bubbleSort(vector4, sizeV);
	sleep(1);
	end = clock();
	
	// Calcula o tempo de CPU usado pela função em segundos
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Bubble Sort para o vetor 4: %f ms", cpuTime);
    
    start = clock();
	insertion_sort(vector4, sizeV);
	sleep(1);
	end = clock();
	
    cpuTime = (((double)(end - start)) - 1000)/ CLOCKS_PER_SEC;
    printf("\nTempo usado em Insertion Sort para o vetor 4: %f ms", cpuTime);
    printf("\n---------------------------------------------------------------------------");
    
	return 0;
}
