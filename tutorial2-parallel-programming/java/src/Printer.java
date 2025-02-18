import java.util.Arrays;



public class Printer {
    public static void main(String[] args) {
        double[][] array = new double[100000000][2];
        for (int i = 0; i < array.length; i++) {
            array[i][0] = Math.random();
            array[i][1]= Math.random();
        }
        long tempoinicial= System.currentTimeMillis();
        double cont = Arrays.stream(array)
                .filter(array_n -> ((array_n[0]*array_n[0])+ (array_n[1]* array_n[1])) <= 1).count();
        System.out.println(cont/array.length*4);
        System.out.println("Serial execution");
        long tempofinal= System.currentTimeMillis();
        

        long tempoinicial2= System.currentTimeMillis();
       
        System.out.println("Parallel execution");
        double cont2 = Arrays.stream(array)
                .filter(array_n -> ((array_n[0]*array_n[0])+ (array_n[1]* array_n[1])) <=1).count();
        System.out.println(cont2/array.length*4);
        long tempofinal2 = System.currentTimeMillis();
        System.out.println("Tempo Serial:" + (tempofinal-tempoinicial));
        System.out.println("Tempo Paralelo:" + (tempofinal2-tempoinicial2));
    }
}
