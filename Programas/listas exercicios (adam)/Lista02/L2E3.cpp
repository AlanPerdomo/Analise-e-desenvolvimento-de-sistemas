#include <iostream>
using namespace std;

int main(){
	int entry;
	while(true){
		cout << "\nEntrada - "; cin >> entry;
		if(entry >= 0){
			int bin = 0, x = 1;
			while(entry > 0){
				bin += ((entry % 2) * x);
				entry /= 2;
				x *= 10;
			}
			cout <<"Saida - "<< bin << endl;
		}
		else{
			break;
		}
	}
}