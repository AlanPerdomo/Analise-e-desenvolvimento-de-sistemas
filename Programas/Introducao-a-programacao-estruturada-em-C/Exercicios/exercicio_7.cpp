// Lista de exercicios 1

// 7. Faça um algoritmo para ler e imprimir o nome e a idade de várias pessoas, 
//    até encontrar alguém com 65 anos, quando deverá ser impresso, além do nome e
//    da idade, uma mensagem informando o fato.

#include <iostream>
#include <locale.h>

using namespace std;

int main(){
	setlocale(LC_ALL, "Portuguese");
	
	int i=1, idade;
	string nome;
	
	while(idade != 65){
		cout<<"Digite o nome da "<<i<<"ª pessoa: ";cin>>nome;
		cout<<"Digite a idade da "<<i<<"ª pessoa: ";cin>>idade;
		cout<<"Nome: "<<nome<<" - idade: "<<idade<<endl;
		cout<<"====================================================="<<endl;
		i++;
	}
}
