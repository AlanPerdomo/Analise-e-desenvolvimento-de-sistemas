public class Main1 {
    public static class Mamifero{
        //  atributos
        public String nome;
        //  construtor
        public Mamifero(String nome){
            this.nome = nome;
        }
        //  metodo
        public void locomover(){}
    }
    public static class Macaco extends Mamifero{
        public Macaco(String nome){
            super(nome);
        }
        public void locomover(){
            System.out.print("Pular de galho em galho! \n");
        }
    }
    //  Subclass Homem
    public static class Homem extends Mamifero{
        public Homem(String nome){
            super(nome);
        }
        public void locomover(){
            System.out.print("Andar\n");
        }
    }
    public static class Baleia extends Mamifero{
        public Baleia(String nome){
            super(nome);
        }
        public void locomover(){
            System.out.print("Nadar\n");
        }
    }
    public static void main(String[] arg){
        Mamifero animal;
        animal = new Macaco("Mico leão dourado");
        animal.locomover();
        animal = new Baleia("Baleia azul");
        animal.locomover();
        animal = new Homem("Maria");
        animal.locomover();
    }
}