#include <iostream>
using namespace std;

int somar(int x, int y){
    return x + y;
}

int main(){
    int a,b;
    cout << "Digite o valor de x - ";cin >> a;
    cout << "Digite o valor de y - ";cin >> b;
    cout << somar(a,b);

}
