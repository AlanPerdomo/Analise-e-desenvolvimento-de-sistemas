import java.util.Scanner;

public class Aula2{
    public static class Gatos{
        public String nome;
        public String raca;
        public float peso;

        public void andar(){}
        public void comer(){}
        public void dormir(){}    
    }
    public static class Conta_bancaria{

       public String nome;
       public int agencia; 
       public int conta;
       public double saldo;

       public void saque(){}
       public void transferencia(){}
    }
    public static class Pessoa{
       public String nome;
       public int idade;
       public float peso;
       
       public void andar(){}
       public void dormir(){}
    }
    public static class Humano{
        public String nome;
        public String cor_olhos;
        public double altura;
        public float peso;
    }
        public static void main(String[] args){
            Scanner data = new Scanner(System.in);

            Humano humano1 = new Humano();
            humano1.nome = "a";
            humano1.cor_olhos = "preto";
            humano1.altura = 1.8;
            humano1.peso = 20;

            Humano humano2 = new Humano();
            humano2.cor_olhos = "b";
            humano2.nome = "branco";
            humano2.altura = 10;
            humano2.peso = 20; 

            Humano humano3 = new Humano();
            humano3.nome = "c";
            humano3.cor_olhos = "amarelo";
            humano3.altura = 1.6;
            humano3.peso = 20; 

            Humano humano4 = new Humano();
            humano4.nome = "d";
            humano4.cor_olhos = "azul";
            humano4.altura = 1.0;
            humano4.peso = 20; 

            Gatos gato1 = new Gatos();
            gato1.raca = "Vira-lata";
            gato1.peso = 2;
            gato1.nome = "Vichano";
            
            Gatos gato2 = new Gatos();
            gato2.raca = "Siames";
            gato2.peso = 4;
            gato2.nome = "Bichano";

            Gatos gato3 = new Gatos();
            gato3.raca = "Sames";
            gato3.peso = 10;
            gato3.nome = "Bhano";

            if(humano1.altura > 1.7){
                System.out.printf("Altura do humano 1 é maior que 1.7\n");
            }
            if(humano2.altura > 1.7){
                System.out.printf("Altura do humano 2 é maior que 1.7\n");
            }
            if(humano3.altura > 1.7){
                System.out.printf("Altura do humano 3 é maior que 1.7\n");
            }
            if(humano4.altura > 1.7){
                System.out.printf("Altura do humano 4 é maior que 1.7\n");
            }

            System.out.printf("Nome Gato 1: %s\n", gato1.nome);
            System.out.printf("Nome Gato 2: %s\n", gato2.nome);
            System.out.printf("Nome Gato 3: %s\n", gato3.nome);
            
            System.out.println("Hello World\n");
    }
}
