// Lista de exercicios 1

// calculadora 

#include <iostream>
#include <locale.h>
#include <math.h>
using namespace std;
int main(){
	setlocale(LC_ALL, "Portuguese");
	
	int op=7;
	double n1,n2;
	
	while(op!=0){
		op = 7;
		
		cout<<"========Calculadora========"<<endl;
		cout<<"Escolha a opera��o que deseja realizar: \n(0)-Sair (1)-Adi��o (2)-Subtra��o (3)-Multiplica��o (4)-Divis�o (5)-Potencia��o.\n";
		while(op<0 or op>5){
			cin>>op;
			if(op==0){
				return 0;
			}
			if(op<0 or op>5){
				cout<<"Escolha a opera��o que deseja realizar: \n(0)-Sair (1)-Adi��o (2)-Subtra��o (3)-Multiplica��o (4)-Divis�o (5)-Potencia��o.\n";
			}
		}
		cout<<" Digite o primeiro valor - ";cin>>n1;
		cout<<" Digite o segundo valor - ";cin>>n2;
		
		switch(op){
			case 0: break;
			case 1: cout<<n1<<" + "<<n2<<" = "<<n1+n2<<".\n\n";break;
			case 2: cout<<n1<<" - "<<n2<<" = "<<n1-n2<<".\n\n";break;
			case 3: cout<<n1<<" * "<<n2<<" = "<<n1*n2<<".\n\n";break;
			case 4: cout<<n1<<" / "<<n2<<" = "<<n1/n2<<".\n\n";break;
			case 5: cout<<n1<<" ^ "<<n2<<" = "<<pow(n1,n2)<<".\n\n";break;
		}
	}
}
