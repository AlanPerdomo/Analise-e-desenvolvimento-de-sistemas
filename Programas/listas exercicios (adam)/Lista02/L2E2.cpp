#include <iostream>
using namespace std;
int main(){
	string num,mun;
	int aux;
	while(true){
		cout << "Entrada - "; cin >> num;
		mun = "";
		
		if(num[0] != 45){
			for(int i=num.length()-1; i>=0; i-- ){
			mun += num[i];
			}
		
			if(num == mun){
				cout << "VERDADEIRO \n";
			}
			else{
				cout << "FALSO \n";
			} 
		}
		
		else{
			break;
		}
	}
}
