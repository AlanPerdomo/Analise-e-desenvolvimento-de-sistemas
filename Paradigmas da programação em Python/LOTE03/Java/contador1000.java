package Java;
class contador1000{
    public static void main(String[] args)throws InterruptedException{
        long startTime = System.nanoTime();
        for(int i=1; i<=1000; i++){
            System.out.println(i);
        }
        long endTime = System.nanoTime();
        long timeElapsed = endTime - startTime;
        System.out.println("Tempo de execução em nanosegundos: " + timeElapsed);
        System.out.println("Tempo de execução em milissegundos: " + timeElapsed / 1000000);
        System.out.println("Tempo de execução em segundos: " + (timeElapsed / 1000000)/1000);
    }
}
