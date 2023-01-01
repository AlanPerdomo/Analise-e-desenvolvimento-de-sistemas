package Java; 
class olamundo{
    public static void main(String[] args) throws InterruptedException{
        long startTime = System.nanoTime();
        System.out.println("Ola Mundo");
        long endTime = System.nanoTime();
        long timeElapsed = endTime - startTime;
        System.out.println("tempo de execução em nanosegundos: " + timeElapsed);
        System.out.println("tempo de execução em milissegundos: " + timeElapsed / 1000000);
        System.out.println("tempo de execução em segundos: " + (timeElapsed / 1000000)/1000);
    }
}
