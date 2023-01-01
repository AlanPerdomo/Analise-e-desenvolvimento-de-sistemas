// faça um algoritmo que leia 3 vetores. o 1 com x nomes de alunos, o 2 com x notas de av1
//  e o 3 com x notas av2. ao final mostre cada aluno, suas notas e sua media simples.

#include <iostream>
using namespace std;
int main() {
    string nome[5];
    float av1[5],av2[5],media[5];

    for (int i = 0; i < 5; i++){
        cout << "Digite o nome do " << i+1 <<"º aluno - ";cin >> nome[i];
        cout << "Digite a nota da AV1 do(a) "<< nome [i] << " - ";cin >> av1[i];
        cout << "Digite a nota da AV2 do(a) "<< nome [i] << " - ";cin >> av2[i];
        media[i] = (av1[i]+av2[i])/2;
    }
    for (int i = 0; i < 5; i++){
        cout << nome[i] << " ficou com " << av1[i] << " na AV1 e com " << av2[i] << " na AV2. Sua media ficou " << media[i] << endl;
    }
}

int lucas(){
    float av1,av2;
    int vet[3],i=0,x,p=1;
    string nome,cdalu[3],a;
    for (i=0;i<2;i++){
        cout << "digite nome do" << p << "º aluno : \t";cin>>nome;p++;
        cout << "notas da av1 :\t"; cin >> av1;
        cout << "notas da av2 :\t"; cin >> av2;
        cout << nome << "ficou com media :\t"<<(av1+av2)/2 << endl;
        cout << "=====================================================\n";
        cout << cdalu[0]; 
    }
}