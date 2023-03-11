import java.util.Scanner;

public class Aula3 {
    public static class Conta {
        public String nome;
        public int agencia;
        public int nconta;
        public double saldo;

        public void saque() {
        }

        public void transfer() {
        }

        public static void main(String[] args) {
            Scanner ler = new Scanner(System.in);
            Conta clientes[] = new Conta[4];

            for (int i = 0; i < clientes.length; i++) {
                clientes[i] = new Conta();
            }
            System.out.println("-- Tela de cadastro --");
            for (int i = 0; i < clientes.length; i++) {
                System.out.println("Nome:");
                clientes[i].nome = ler.next();
                System.out.println("Agencia: ");
                clientes[i].agencia = ler.nextInt();
                System.out.println("Numero da Conta: ");
                clientes[i].nconta = ler.nextInt();
                System.out.println("Saldo: ");
                clientes[i].saldo = ler.nextDouble();
                System.out.println("---------------------");
            }
            for (int i = 0; i < clientes.length; i++) {
                if (clientes[i].saldo > 5000) {
                    System.out.printf("O saldo de %s é maior que 5000 \n", clientes[i].nome);
                }
            }
            System.out.println("Funcionamento ok");
        }
    }

    public static class Pessoa {
        public String nome;
        public int idade;
        public double peso;

        public void Andar() {
        }

        public void Dormir() {
        }

        public static void main(String[] args) {
            Scanner ler = new Scanner(System.in);
            Pessoa pessoa[] = new Pessoa[5];

            for (int i = 0; i < pessoa.length; i++) {
                pessoa[i] = new Pessoa();
            }

            for (int i = 0; i < pessoa.length; i++) {
                System.out.println("Nome:");
                pessoa[i].nome = ler.next();
                System.out.println("Idade: ");
                pessoa[i].idade = ler.nextInt();
                System.out.println("peso: ");
                pessoa[i].peso = ler.nextDouble();
            }

            for (int i = 0; i < pessoa.length; i++) {
                if (pessoa[i].idade < 12) {
                    System.out.printf("%s é uma crianca. \n", pessoa[i].nome);
                }
            }
        }
    }

    public static class Animais{
        public String classificacao;
        public int idade;
        public String loc_encontrado;

        public void Andar(){}
        public void Comer(){}
        
        static int contador = 0;
        public static void main(String[]args){
            Scanner ler = new Scanner(System.in);
            Animais animal[] = new Animais[10];

            for(int i = 0; i < animal.length; i++){
                animal[i] = new Animais();
            }
            for(int i = 0; i < animal.length; i++){
                System.out.println("Classificação: ");
                animal[i].classificacao = ler.next();
                System.out.println("Idade: ");
                animal[i].idade = ler.nextInt();
                System.out.println("peso: ");
                animal[i].loc_encontrado = ler.next();
                if(animal[i].idade > 50){
                    contador += 1;
                
                }
            System.out.printf("%d animais possuem idade superior a 50 anos. \n" , contador);
            }
        }
    }
    public static class Automovel{
        public String tipo;
        public String marca;
        public int fabricaco;
        
        public void main(String[] args){
            Scanner ler = new Scanner(System.in);
            Automovel automovel[] = new Automovel[15];
            for(int i = 0; i < automovel.length; i++){
                automovel[i]= new Automovel();
            }
        }
    }
}
