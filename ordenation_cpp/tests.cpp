#include <iostream>
#include <cstdlib>
#include <ctime>


int* MakeRandomArray(int size, int min, int max);
void Bubblesort(int *v, int n);


int main(void) {

    int size_array = 1000;

    int* array1 = MakeRandomArray(size_array, 0, 100);

    std::clock_t start_time = std::clock();
    Bubblesort(array1, size_array);
    std::clock_t end_time = std::clock();

    double duration = static_cast<double>(end_time - start_time) / CLOCKS_PER_SEC;
    std::cout << "Tempo de execução: " << duration << " segundos." << std::endl;

    for (int i = 0; i < size_array; i++) {
        std::cout << array1[i] << " ";
    }

    return 0;
}


int* MakeRandomArray(int size, int min, int max) {

    int *array = new int[size];

    srand(time(NULL));

    for (int i = 0; i < size; i++) {
        array[i] = rand() % (max - min + 1) + min;
    }

    return array;
}


void Bubblesort(int *v, int n) {
    int i, j, aux;
    for (i = 0; i < n; i++) {
        // activate/deactivate lower bound:
        // is_sorted = 1;
        for (j = 0; j < n - 1 - i; j++) {
            if (v[j] > v[j + 1]) {
                aux = v[j];
                v[j] = v[j + 1];
                v[j + 1] = aux;
                // activate/deactivate lower bound:
                // is_sorted = 0;
            }
            // if is_sorted {break;}
        }
    }
}
