import javax.net.ssl.CertPathTrustManagerParameters;

public class Main3 {
    public static class Transporte{
        //  atributos
        public String nome;
        public int velocidade_max;
        public int capacidade;
        //  construtor
        public Transporte(String nome,int velocidade_max,int capacidade ){
            this.nome = nome;
            this.velocidade_max = velocidade_max;
            this.capacidade = capacidade;
        }
        public void consome(){}
    }   
    public static class Bicicleta extends Transporte{
        public Bicicleta(String nome,int velocidade_max,int capacidade ){
            super(nome, velocidade_max, capacidade );
        }
        public void consome(){
            System.out.print("consome ATP e se move! \n");
        }
    } 
    public static class Carro extends Transporte{
        public Carro(String nome,int velocidade_max,int capacidade ){
            super(nome,velocidade_max, capacidade );
        }
        public void consome(){
            System.out.print("consome gasolina e acelera! \n");
        }
    } 
    public static class Aviao extends Transporte{
        public Aviao(String nome,int velocidade_max,int capacidade ){
            super(nome, velocidade_max, capacidade) ;
        }
        public void consome(){
            System.out.print("consome gasolina de aviação e voa! \n");
        }
    } 
    public static void main(String[] arg){
        Aviao aviao1 = new Aviao("cesna", 1000, 300);
        Carro carro1 = new Carro("opala", 200, 4);
        Bicicleta bicicleta1 = new Bicicleta("caloi", 30, 1);

        System.out.printf("\nAvião = nome: %s, Velocidade Maxima: %d, capacidade: %d \n", aviao1.nome,aviao1.velocidade_max,aviao1.capacidade);
        
    }
}
