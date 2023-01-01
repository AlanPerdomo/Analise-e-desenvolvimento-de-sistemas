// Lista de exercicios

// 24. 


#include <iostream>
#include <locale.h>
using namespace std;
int main(){
	setlocale(LC_ALL, "Portuguese");
	
	int h_s,h_n,m_s,m_n;
	string resposta[10],sexo[10];
	
	for(int i=0;i<10;i++){
		cout<<i+1<<"ª pessoa."<<endl;
		cout<<"Digite o sexo - ";cin>>sexo[i];
		cout<<"Gostou do produto? ";cin>>resposta[i];
		if(sexo[i]=="masculino"){
			if(resposta[i]== "sim" or "s"){
				h_s++;
			}
			if(resposta[i]== "nao" or "n"){
				h_n++;
			}
		}
		if(sexo[i]=="feminino"){
			if(resposta[i]== "sim" or "s"){
				m_s++;
			}
			if(resposta[i]== "nao" or "n"){
				m_n++;
			}			
		}		
	}
	cout<<h_s+m_s<<" pessoas responderam sim."<<endl;
	cout<<h_n+h_n<<" pessoas responderam não."<<endl;
	cout<<m_s<<" mulheres responderam sim."<<endl;
	cout<<(h_n/(h_n+h_s))*100<<"% dos homens responderam que não."<<endl;	
}
