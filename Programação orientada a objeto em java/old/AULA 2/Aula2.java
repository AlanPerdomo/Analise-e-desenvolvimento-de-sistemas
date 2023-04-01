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
            Humano[] humano = new Humano[5];
            for (int i = 0; i < 5; i++){
                humano[i] = new Humano();
            }
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

        for (int i = 0; i < 5; i++){
            if(humano[i].altura > 1.7){
                System.out.printf("Altura do humano %d é maior que 1.7\n", i+i);
            }
        System.out.printf("Nome Gato 1: %s\n", gato1.nome);
        System.out.printf("Nome Gato 2: %s\n", gato2.nome);
        System.out.printf("Nome Gato 3: %s\n", gato3.nome);
        System.out.println("Hello World\n");
        }
    }
}