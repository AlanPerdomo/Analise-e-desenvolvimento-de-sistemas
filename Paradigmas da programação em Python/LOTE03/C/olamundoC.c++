#include <iostream>
#include <time.h>
using namespace std;
int main(){
    double time_spent = 0.0;
    clock_t begin = clock();
    cout << "Ola Mundo";
    clock_t end = clock();
    time_spent += (double)(end - begin)/CLOCKS_PER_SEC;
    cout << "o tempo decorrido foi de "<< time_spent <<" segundos ";
}