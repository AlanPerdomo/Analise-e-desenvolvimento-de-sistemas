import java.util.Scanner;

public class Main {
    public static class Pessoa{
        public String nome;
        public long cpf;
        public int ano_nascimento;
        //  Construtor
        public Pessoa(String nome, long cpf, int ano){
            this.nome = nome;
            this.cpf = cpf;
            this.ano_nascimento = ano;
        }
    }
    //  Subclasse Aluno
    public static class Aluno extends Pessoa{
        public Aluno(String nome, long cpf, int ano){
            super(nome,cpf,ano);
        }
    }
    //  Subclasse Professor
    public static class Professor extends Pessoa{
        public Professor(String nome, long cpf, int ano){
            super(nome,cpf,ano);
        }
    }

    public static void main(String[] args){
        Scanner data = new Scanner(System.in);
        System.out.println("Informe o nome  do Professor: ");
        String nome = data.next();
        System.out.println("Informe o cpf  do Professor: ");
        long cpf = data.nextLong();
        System.out.println("Informe o ano de nascimento do Professor: ");
        int ano = data.nextInt();
        Professor professor1 = new Professor(nome,cpf,ano);

        System.out.println("Informe o nome  do aluno: ");
        String nome1= data.next();
        System.out.println("Informe o cpf  do aluno: ");
        long cpf1 = data.nextLong();
        System.out.println("Informe o ano de nascimento do aluno: ");
        int ano1 = data.nextInt();       
        Aluno aluno1 = new Aluno(nome1,cpf1,ano1);

        System.out.printf("Nome Professor(a): %s\n",professor1.nome);
        System.out.printf("CPF professor(a): %d \n", professor1.cpf);
        System.out.printf("Ano Nascimento do Professor(a): %d \n",professor1.ano_nascimento);
        
    }
}

