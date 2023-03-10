import java.util.Scanner;

public class Aula3 {
    public static class Conta{
        public String nome;
        public int agencia;
        public int nconta;
        public double saldo;

        public void saque(){}
        public void transfer(){}
        public static void main(String[]args){
            Scanner ler = new Scanner(System.in);
            Conta clientes[] = new Conta[4];
        
            for(int i = 0; i < clientes.length; i++){
                clientes[i] = new Conta();   
            }
            System.out.println("-- Tela de cadastro --");
            for(int i = 0; i < clientes.length; i++){
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
            for(int i= 0; i< clientes.length; i++){
                if (clientes[i].saldo > 5000){
                    System.out.printf("O saldo de %s é maior que 5000 \n", clientes[i].nome);
                }
            }
            System.out.println("Funcionamento ok");
        }
    }
}
