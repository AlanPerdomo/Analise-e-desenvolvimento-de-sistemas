#include <iostream>
using namespace std;
int main(){
	int aux, list1[5], list2[5], list3[5];
	
	for(int i=0;i<5;i++){
		cout << "Digite o " << i+1 << "º valor da 1ª lista - "; cin >> list1[i];
		cout << "Digite o " << i+1 << "º valor da 2ª lista - "; cin >> list2[i];
		if(list1[i]>list2[i]){
			list3[i]=list1[i];
		}
		else{
			list3[i]=list2[i];
		}
	}	
	for(int i=0;i<5;i++){
		cout << "\nO " << i+1 << "º valor da lista 1 é " << list1[i];
		cout << "\tO " << i+1 << "º valor da lista 2 é " << list2[i];
		cout << "\tO " << i+1 << "º valor da lista 3 é " << list3[i];
	}
	for(int i=0;i<5;i++){
		for(int j=i+1;j<5;j++){
			if(list3[i]>list3[j]){
				aux = list3[i];
				list3[i] = list3[j];
				list3[j] = aux;
			}
		}
	}
	cout << "\nA lista 3 ordena é: ";
	for(int i=0;i<5;i++){
		cout << list3[i] << "\t";
	}	
}
