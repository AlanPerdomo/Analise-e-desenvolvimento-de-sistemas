#include <iostream>
#include <locale.h>
#include <math.h>
#include <sstream>

using namespace std;


int main(){
	setlocale(LC_ALL, "Portuguese");
	
	string entrada;
	
	cout<<"numero que deseja converter -> ";cin>>entrada;
	
	int tipo,soma,inte_entrada, resultado, x;
	int num_caracteres= entrada.length();
	
	cout<<"(1)-Bin�rio *(2)-Decimal *(3)-hexadecimal"<<endl;
	cout<<"Em qual o sistema num�rico o seu n�mero esta? -> ";cin>>tipo;
	
	switch(tipo){
		//Numero Bin�rio
		case 1:{
			//convers�o para decimal.
			cout<<"\nDecimal = ";
			resultado=0;
			x=num_caracteres-1;
			for(int i=0;i<num_caracteres;i++){
				if(entrada[i]>=48 and entrada[i]<=57){
					resultado+=((entrada[i]-48)*pow(2,x));	
				}
				if(entrada[i]>=65 and entrada[i]<=70){
					resultado+=((entrada[i]-55)*pow(2,x));	
				}
				if(entrada[i]>=97 and entrada[i]<=102){
					resultado+=((entrada[i]-87)*pow(2,x));
				}
				x--;				
			}
			cout<<resultado<<endl;
			//convers�o para hexadecimal.
			cout<<"Hexadecimal = ";
			while(num_caracteres%4!=0){
				entrada="0"+entrada;
				num_caracteres=entrada.length();
			}
			int y=0,soma_hexa[num_caracteres/4];
			resultado=0;
			x=3;			
			//limpar valores da soma_hexa[]
			for(int i=0;i<=num_caracteres/4;i++){
				soma_hexa[i]=0;
			}			
			for(int i=0;i<num_caracteres;i++){
				if(entrada[i]>=48 and entrada[i]<=57){
					soma_hexa[y]+=((entrada[i]-48)*pow(2,x));	
				}
				if(entrada[i]>=65 and entrada[i]<=70){
					soma_hexa[y]+=((entrada[i]-55)*pow(2,x));
				}
				if(entrada[i]>=97 and entrada[i]<=102){
					soma_hexa[y]+=((entrada[i]-87)*pow(2,x));
				}	
				x--;		
				if(x==-1){
					x=3;
					y++;
				}				
			}
			for(int i=0;i<num_caracteres/4;i++){
				if(soma_hexa[i]<10){
					cout<<soma_hexa[i];
				}
				else{
					switch(soma_hexa[i]){
						case 10:{cout<<"A";break;}
						case 11:{cout<<"B";break;}
						case 12:{cout<<"C";break;}
						case 13:{cout<<"D";break;}
						case 14:{cout<<"E";break;}
						case 15:{cout<<"F";break;}
					}
				}
			}
			break;
		}
		//Numero Decimal
		case 2:{
			//convers�o para bin�rio.
			cout<<"\nBinario = ";
			resultado=0;
			x=1;
			stringstream inte_entrada(entrada);
			inte_entrada>>soma;
			cout<< "\n !! SOMA =  "<<soma<<"\n";
			
			while(soma >0){
				resultado+=((soma%2)*x);
				soma=soma/2;
				x*=10;
			}
			cout<<resultado<<endl;
			
			//conversao para hexadecimal.
			cout<<"Hexadecimal = ";
			resultado=0;
			
			cout<<resultado<<endl;
			break;
		}	
		//Numero Hexadecimal
		case 3:{
			//convers�o para binario.
			cout<<"\nBinario = ";
			cout<<resultado<<endl;
			
			//convers�o para decimal.
			cout<<"Decimal = ";
			cout<<resultado<<endl;
			break;
		}
	}
}

