package Exercicios;
public class Automovel {
    public void nome(String nome){
        return nome;
    }
}
public class Carro extends Automovel{
    @Override public void nome(String nome){
        return ¿O carro é¿+super.nome(nome);
    }
}
public class Executa {public static void main(String[] args){
    Carro carro = new Carro();
        System.out.println(carro.nome(¿Corsa¿));
}}
