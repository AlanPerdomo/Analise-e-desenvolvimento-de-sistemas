public class Main2 {
    public static class Funcionario{
        //  atributos
        public String nome;
        public float salario;
        //  construtor
        public Funcionario(String nome,float salario){
            this.nome = nome;
            this.salario = salario;
        }
    }   
    public static class Engenheiro extends Funcionario{
        public Engenheiro(String nome,float salario){
            super(nome,salario);
        }
    } 
    public static class Diretor extends Funcionario{
        public Diretor(String nome,float salario){
            super(nome,salario);
        }
    } 
    public static class Secretario extends Funcionario{
        public Secretario(String nome,float salario){
            super(nome,salario);
        }
    } 
    public static class Gerente extends Funcionario{
        public Gerente(String nome,float salario){
            super(nome,salario);
        }
    } 
}
