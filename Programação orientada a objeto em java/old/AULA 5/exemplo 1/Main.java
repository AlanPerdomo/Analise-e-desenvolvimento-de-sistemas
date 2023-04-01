import java.util.Scanner;
public class Main{
    public static class ContaBancaria{
        private String nome;
        private int idade;
        private double peso;
        private String escolaridade;

        public void setNome(String nome){
            this.nome = nome;
        } 
        public void setIdade(int idade){
            this.idade = idade;
        }
        public void setPeso(double peso){
            this.peso = peso;
        }
        public void setEscolaridade(String escolaridade){
            this.escolaridade = escolaridade;
        }
        public String getNome(){
            return this.nome;
        }
        public int getIdade(){
            return this.idade;
        }
        public double getPeso(){
            return this.peso;
        }
        public String getEscolaridade(){
            return this.escolaridade;
        }
    }
    public static void main(String[]args){
        Scanner ler = new Scanner(System.in);
        ContaBancaria[] conta = new ContaBancaria[3];
        
        for (int i = 0; i < 3; i++){
            conta[i] = new ContaBancaria();
        }

        System.out.println("\n----------------------------------");
        for (int i = 0;i < 3; i++){
            System.out.printf("\nInforme o nome da %dª pessoa: ", i+1);
            String nome = ler.next();
            conta[i].setNome(nome);

            System.out.printf("Informe o ano em que a %dª pessoa nasceu: ", i+1);
            int ano = ler.nextInt();
            int idade = 2023 - ano;
            conta[i].setIdade(idade);

            System.out.printf("Informe o peso da %dª pessoa: ", i+1);
            double peso = ler.nextDouble();
            conta[i].setPeso(peso);
            
            System.out.printf("Informe a escolaridade da %dª pessoa: ", i+1);
            String escolaridade = ler.next();
            conta[i].setEscolaridade(escolaridade);
        }
        System.out.println("----------------------------------\n");

        for (int i = 0; i < 3; i++){
            System.out.printf("A idade da(o) %s é %d anos.\n", conta[i].getNome(), conta[i].getIdade());
        }

    }
}