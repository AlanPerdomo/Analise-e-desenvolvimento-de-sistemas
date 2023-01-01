#include <iostream>
using namespace std;

void show_table(){
	cout << "  \tA   B   C   D   E   F   G   H   i";
    cout << "\n  \t|   |   |   |   |   |   |   |   |"; 
    for (int i = 0; i < 9; i++ ){
        cout << "\n\n" << i << "--\t";
        for ( int j = 0; j < 9; j++){
            cout << table[i][j] << "   ";
        }
    }
}

int main(){
    int start, aux, table[9][9]={
    {0,0,0,0,0,0,6,9,0},
    {0,2,8,1,0,0,0,0,0},
    {0,0,0,0,0,0,0,0,5},
    {6,0,0,4,0,0,3,0,1},
    {0,0,0,0,0,0,0,0,0},
    {0,0,0,0,0,0,0,8,0},
    {1,0,0,0,3,0,0,4,0},
    {3,9,6,5,0,7,0,0,0},
    {0,8,0,0,0,0,0,0,0}};

    cout << " ==================================================================== \n";
    cout << " Bem vindo ao sudoku! \n Digite | 0 - para sair | 1 - para jogar | - ";cin >> start;

    while(start != 1 and start != 0){
        cout << " Por favor digite 0 (para sair) ou 1 (Para Jogar) - "; cin >> start;
    }
    if(start == 0){return 0;}
    show_table();
}


/*

void show_table(int table[9][9]){
    for (int i = 0; i < 9; i++ ){
        cout << "\n\n";
        for ( int j = 0; j < 9; j++){
            cout << "\n" << table[i][j] << "\t";
        }
    }
}



int main(){
    int table[9][9];
    show_table(table[9][9]);
}




    int show_table(){
        int table[9][9];
        for (int i = 0; i < 9; i++ ){
            for ( int j = 0; j < 9; j++){
                cout << "\n" << table[i][j] << "\t";
            }
        }
    }
*/
