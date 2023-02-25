package Exercicios;
package ciga;
import javax.swing.JOptionPane;
public class QuestaoB{
    public static void main(String[] args){
        String repetir = "SIM";
        int valorA, valorB, x=0, calculo;
        while(repetir == "SIM"){
            valorA=Integer.parseInt(JOptionPane.showInputDialog("A: "));
            valorB=Integer.parseInt(JOptionPane.showInputDialog("B: "));
            calculo = valorA * valorB;
            JOptionPane.showInputDialog(null, "Valor: "+ calculo);
            repetir = JOptionPane.showInputDialog("Digite <<SIM>> para CONTINUAR");
        }
        JOptionPane.showMessageDialog(null, "PROGRAMA ENCERRADO");
        System.exit(0);            
        }
    }
}

public class Exercicio 3 {
    
}
